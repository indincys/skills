#!/usr/bin/env python3
"""Validate social atmosphere product prompt Markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^###\s+\d{2}\s+\|", re.MULTILINE)
PROMPT_BLOCK_RE = re.compile(r"```prompt\s*(.*?)```", re.DOTALL | re.IGNORECASE)

REQUIRED_PHRASES = [
    ("3:4 vertical framing", [r"3:4", r"竖版", r"竖款", r"vertical"]),
    ("product reference source", [r"reference image", r"参考图", r"输入.*产品", r"supplied product"]),
    ("product fidelity lock", [r"Product fidelity lock", r"产品保真锁定", r"保留.*卡套", r"不得重绘"]),
    ("real photography", [r"真实", r"photography", r"photo", r"摄影", r"照片"]),
    ("anti-ad constraint", [r"不要.*广告", r"避免.*广告", r"no advertising", r"not an ad", r"非广告"]),
    ("anti-poster constraint", [r"不要.*海报", r"避免.*海报", r"no poster", r"not a poster", r"非海报"]),
    ("anti-ecommerce constraint", [r"不要.*电商", r"避免.*电商", r"no ecommerce", r"not ecommerce", r"非电商"]),
    ("no redesign constraint", [r"不得.*改", r"不要.*改", r"do not.*redesign", r"do not.*change", r"不得.*重绘"]),
]

CROSS_PRODUCT_PHRASES = [
    r"do not.*mix.*other",
    r"do not.*borrow.*other",
    r"不要.*混入.*其他",
    r"不得.*混入.*其他",
    r"不要.*借用.*其他",
    r"当前.*参考图",
]

REALISM_PHRASES = [
    r"自然光",
    r"窗光",
    r"环境光",
    r"混合光",
    r"阴影",
    r"瑕疵",
    r"痕迹",
    r"灰尘",
    r"指纹",
    r"划痕",
    r"褶皱",
    r"颗粒",
    r"texture",
    r"shadow",
    r"dust",
    r"fingerprint",
    r"scratch",
    r"imperfection",
]

PROMO_TERMS = [
    "促销",
    "优惠",
    "折扣",
    "爆款",
    "点击购买",
    "立即购买",
    "主视觉",
    "banner",
    "CTA",
    "price tag",
]


def has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def near_negation(text: str, term: str) -> bool:
    pattern = re.compile(r"(不要|避免|禁止|不得|拒绝|no|not|without|非|不是)[^。\n]{0,24}" + re.escape(term), re.IGNORECASE)
    return bool(pattern.search(text))


SECTION_RE = re.compile(r"(^###\s+\d{2}\s+\|.*?)(?=^###\s+\d{2}\s+\||\Z)", re.DOTALL | re.MULTILINE)


def validate(path: Path, min_prompts: int, max_prompts: int, min_chars: int, allow_legacy: bool) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    headings = HEADING_RE.findall(text)
    sections = SECTION_RE.findall(text)
    blocks = [block.strip() for block in PROMPT_BLOCK_RE.findall(text)]

    if not (min_prompts <= len(headings) <= max_prompts):
        errors.append(f"Expected {min_prompts}-{max_prompts} prompt headings, found {len(headings)}.")
    if len(blocks) != len(headings):
        errors.append(f"Prompt heading count ({len(headings)}) does not match ```prompt blocks ({len(blocks)}).")

    if not allow_legacy:
        if not any(marker in text for marker in ["### Product Profile", "### 产品画像", "## Product A", "## 产品"]):
            errors.append("Missing product-specific profile section.")
        if not any(marker in text for marker in ["### Current Product Lock", "### 当前产品锁定", "Current Product Lock", "当前产品保真"]):
            errors.append("Missing current product lock section.")
    elif "## Global Product Lock" not in text and "## 全局产品保真" not in text:
        errors.append("Missing global product lock section.")

    if len(sections) != len(headings):
        errors.append(f"Prompt section count ({len(sections)}) does not match prompt headings ({len(headings)}).")

    for index, block in enumerate(blocks, start=1):
        label = f"Prompt {index:02d}"
        section = sections[index - 1] if index - 1 < len(sections) else block

        if len(block) < min_chars:
            errors.append(f"{label} is too short: {len(block)} chars, minimum {min_chars}.")

        if not allow_legacy and not has_any(section, [r"Product fit reason", r"适配理由", r"产品适配"]):
            errors.append(f"{label} missing product fit reason.")

        for name, patterns in REQUIRED_PHRASES:
            if not has_any(block, patterns):
                errors.append(f"{label} missing {name}.")

        if not allow_legacy and not has_any(block, CROSS_PRODUCT_PHRASES):
            errors.append(f"{label} missing no cross-product mixing constraint.")

        realism_hits = sum(1 for pattern in REALISM_PHRASES if re.search(pattern, block, re.IGNORECASE))
        if realism_hits < 2:
            errors.append(f"{label} needs at least two real light/material/imperfection cues.")

        for term in PROMO_TERMS:
            if re.search(re.escape(term), block, re.IGNORECASE) and not near_negation(block, term):
                errors.append(f"{label} uses promotional term without negation: {term!r}.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt_file", type=Path)
    parser.add_argument("--min-prompts", type=int, default=24)
    parser.add_argument("--max-prompts", type=int, default=36)
    parser.add_argument("--min-chars", type=int, default=420)
    parser.add_argument("--allow-legacy", action="store_true", help="Allow the older one-product global-lock template.")
    args = parser.parse_args()

    if args.min_prompts > args.max_prompts:
        parser.error("--min-prompts cannot be larger than --max-prompts")

    if not args.prompt_file.exists():
        print(f"ERROR: file not found: {args.prompt_file}", file=sys.stderr)
        return 2

    errors = validate(args.prompt_file, args.min_prompts, args.max_prompts, args.min_chars, args.allow_legacy)
    if errors:
        print("Prompt validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Prompt validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
