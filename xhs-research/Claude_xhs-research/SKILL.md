---
name: xhs-research
description: Systematically researches Xiaohongshu/小红书 official public materials and verified official account channels. Use for questions about Xiaohongshu beginner onboarding, creator/account growth, content creation, monetization, 蒲公英, 聚光, 专业号, 千帆, 商家学习中心, 创作者学院, rules, recommendation/search traffic, live commerce, shop operations, official courses, instructor training, livestream classes, or cross-platform official posts. Requires opening source bodies and answering with conclusion-bound citations.
when_to_use: Trigger when the user asks for 小红书/Xiaohongshu official-source research, operational rules, creator or merchant guidance, account growth, content strategy, commercialization, store/live-commerce operations, official courses, policy interpretation, or evidence-backed answers. Do not use for generic social media advice unless Xiaohongshu official evidence is requested or needed.
argument-hint: "[小红书研究问题]"
allowed-tools:
  - WebSearch
  - WebFetch
  - Task
  - TodoWrite
  - Read
  - Grep
---

# XHS Research

Research Xiaohongshu operations topics from official public sources first, then produce traceable Chinese answers. Optimize for evidence quality, source coverage, and claim-level traceability.

## Core Contract

- Use search only to discover candidate sources. Do not cite search-result snippets.
- Open or fetch every relevant page body before using it as evidence.
- Open PDFs, help-center articles, official announcements, course pages, rule pages, and platform documents when they appear in search results or official navigation.
- Prefer official Xiaohongshu sources. Use non-official sources only as discovery pointers or labeled auxiliary context.
- Bind source links to the exact conclusion, evidence sentence, recommendation, or caveat they support. Do not move sources into a detached source list.
- Separate `官方明确说明`, `基于官方资料合理推导`, and `非官方经验或行业共识`.
- If content is login-walled, JavaScript-only, removed, or unavailable after reasonable attempts, record it as a gap and do not treat it as evidence.
- Answer in the user's language. For Chinese user questions, answer in Chinese.

## Workflow

1. Parse the user's numbered questions and requested scope. If questions are not numbered, preserve the user's order and create stable item numbers.
2. Read `references/research-playbook.md` before searching. Use it for source coverage, query families, official identity checks, and conflict handling.
3. Build a short research plan internally: relevant topic buckets, official surfaces to search, likely blocked surfaces, and required evidence fields.
4. Run official-first searches across creator, 蒲公英, 聚光, 专业号, 千帆/商家, 商家入驻, 直播管理, 学习中心, 帮助/规则, 小程序/开放平台, verified official accounts, and official CDN/PDF surfaces.
5. Fetch each relevant candidate source body. Follow clearly relevant official same-domain links such as `规则`, `课程`, `帮助`, `公告`, `新手`, `创作者`, `商家`, `直播`, `店播`, `商品笔记`, `搜索`, and `流量`.
6. Maintain an evidence log while researching: topic, claim, source title, URL, source class, official level, publish/update date, evidence summary, and caveat.
7. Resolve conflicts by authority, specificity, and recency. Rules, agreements, governance pages, and official announcements outrank courses and marketing materials. Specific product docs outrank broad introductions. Newer official materials outrank older ones when they cover the same issue.
8. Answer each user question with the required structure and inline citations.

## Output Format

For each numbered question:

```markdown
### 1. <用户问题>

**结论**
- 结论 A。 （来源：<标题>, <日期如有>, <URL>）
- 结论 B。 （来源：<标题>, <URL>）

**官方依据**
- 官方明确说明：...（来源：<标题>, <URL>）
- 基于官方资料合理推导：...（来源：<标题1>, <URL>; <标题2>, <URL>）
- 非官方经验或行业共识：...（非官方辅助来源：<标题>, <URL>）

**可执行建议**
- 建议 A。依据：...（来源：<标题>, <URL>）

**注意事项**
- 注意事项 A。限制：...（来源：<标题>, <URL>）
```

Add `检索范围与缺口` when relevant. State official surfaces searched, source types opened, and important materials that could not be accessed or verified.

## Evidence Rules

- Mark a conclusion as `官方明确说明` only when an official source directly states it.
- Mark synthesis across multiple official pages as `基于官方资料合理推导`.
- Mark agency blogs, media articles, SEO pages, community posts, reposted course notes, or industry playbooks as `非官方经验或行业共识` unless the original official source is opened and cited.
- If no official evidence is found for a question, say `未检索到可核验的官方公开依据` and avoid filling the gap with common advice.
- If multiple conclusions rely on the same source, repeat the citation inline where needed.
- Prefer paraphrase plus link. Use short quotes only when exact wording matters.

## Reference

- Read `references/research-playbook.md` for the official source map, cross-platform verification rules, query bank, fetching rules, evidence-log template, and broad-coverage checklist.
