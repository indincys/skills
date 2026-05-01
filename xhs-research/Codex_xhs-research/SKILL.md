---
name: xhs-research
description: Use when Codex must systematically research Xiaohongshu/小红书 official public materials and verified official account channels for beginner onboarding, creator/account growth, content creation, monetization, 蒲公英, 聚光, 专业号, 千帆, 商家学习中心, 创作者学院, rules, recommendation/search traffic, live commerce, shop operations, official instructor courses, training, livestream classes, public courses, or 微信公众号/视频号/微博/B站/抖音等跨平台官方发布. Answer with conclusion-bound citations that distinguish official statements, reasoned inferences, and non-official experience. Requires opening/fetching relevant page bodies, PDFs, course pages, help articles, announcements, rules, and verified official account posts instead of relying on search-result summaries.
---

# XHS Research

## Purpose

Research Xiaohongshu operations topics from official public sources first, then produce traceable Chinese answers. Use this skill for questions about creator growth, account operations, notes, livestreams, shop/store operations, content ecommerce, search traffic, recommendation mechanisms, policy violations, traffic support, official courses, and commercialization.

## Non-Negotiables

- Use search only to discover candidate URLs; open or fetch every relevant page body before using it.
- Open PDFs, help-center articles, official announcements, course pages, rule pages, and platform documents when they appear in search results or official navigation.
- Prefer official Xiaohongshu sources. Use non-official sources only as discovery pointers or auxiliary context, and label them as non-official.
- Do not make generic account-growth recommendations unless they are tied to official evidence or clearly labeled as inference/non-official experience.
- Bind source links to the exact conclusion or evidence sentence they support. Do not put all sources in a detached "具体来源链接" block.
- Cite a source link for every key conclusion. If a source has a publish or update date, include it inline with that conclusion.
- If content is login-walled, JS-only, removed, or unavailable after reasonable fetch/browser attempts, record it as unverified and do not treat it as evidence.
- Answer in the user's language. For Chinese user questions, answer in Chinese.

## Workflow

1. Parse the user's numbered questions and the requested scope. If questions are not numbered, preserve the user's order and create stable item numbers.
2. Read [research-playbook.md](references/research-playbook.md) before doing the live research.
3. Run official-first searches across creator, 蒲公英, 聚光, 专业号, 千帆/商家, 商家入驻, 直播管理, 学习中心, 帮助/规则, 小程序/开放平台, official account channels, and official CDN/PDF surfaces.
4. For each relevant result, open/fetch the page body. Follow same-domain official links when they are clearly relevant to the question.
5. Build an evidence log with: topic, claim, source title, URL, source class, official level, publish/update date, quoted/paraphrased evidence, and caveats.
6. Resolve conflicts by authority, specificity, and recency. Rules/terms/official announcements outrank courses and marketing materials; specific product docs outrank broad introductions; newer official materials outrank older ones when they cover the same issue.
7. Answer each user question with the required structure and citations.

## Tool Mapping

If the environment exposes tools named `WebSearch` and `WebFetch`, use them directly. In Codex, use the available web search/open tools for discovery and body reading; use a browser automation or PDF extraction tool when a page requires rendering or a PDF needs text extraction. Search snippets are not evidence.

## Answer Format

For each numbered user question, include these sections. Put the source immediately after the conclusion/evidence it supports, using `（来源：<title>, <date if available>, <URL>）`.

```markdown
### 1. <user question>

**结论**
- 结论 A。 （来源：<source title>, <date if available>, <URL>）
- 结论 B。 （来源：<source title>, <date if available>, <URL>）

**官方依据**
- 官方明确说明：...（来源：<source title>, <URL>）
- 基于官方资料合理推导：...（来源：<source title 1>, <URL>; <source title 2>, <URL>）
- 非官方经验或行业共识：...（非官方辅助来源：<source title>, <URL>）

**可执行建议**
- 建议 A。理由/依据：...（来源：<source title>, <URL>）

**注意事项**
- 注意事项 A。触发条件/限制：...（来源：<source title>, <URL>）
```

Add a short "检索范围与缺口" section before or after the answers when relevant. State which official surfaces were searched and which important materials could not be accessed.

## Evidence Standards

- Treat a conclusion as "官方明确说明" only when it is directly stated in an official source.
- Treat synthesis across multiple official pages as "基于官方资料合理推导".
- Treat agency blogs, media articles, SEO pages, community posts, course notes reposted by third parties, or industry playbooks as "非官方经验或行业共识" unless the original official source is opened and cited.
- If no official evidence is found for a question, say "未检索到可核验的官方公开依据" and avoid filling the gap with common advice.
- If multiple conclusions rely on the same source, repeat the citation inline where needed; optimize for traceability over compactness.
- Use short quotes only when necessary; prefer paraphrase plus link.
