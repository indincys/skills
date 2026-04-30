# Planning And Rubric

Use this reference when preparing the first confirmation plan for a web-collection task.

## Execution Plan Template

```markdown
**Execution Plan**

**1. Task Interpretation**
- User goal:
- Intended use of the collection:
- Assumptions:

**2. Scope**
- Target quantity:
- Inclusion criteria:
- Exclusion criteria:
- Expected breadth:
- Expected depth:

**3. Output Schema**
| Field | Why it matters |
| --- | --- |
| ... | ... |

**4. Source Discovery Reasoning**
- Source types to explore, derived from the task:
- Languages/regions to include, if useful:
- Audience or ecosystem angles:
- Recency and evidence needs:

**5. Search Strategy**
- Direct query families:
- Adjacent/lateral query families:
- Reverse/problem-driven query families:
- Platform-native or source-native searches:
- Expansion plan if a direction is weak:

**6. Tool And Agent Orchestration**
- Tools to use:
- Subagent tasks, only if allowed and genuinely independent:
- Integration plan:

**7. Quality Rubric**
- Breadth:
- Depth:
- Uniqueness:
- Practical usefulness:
- Evidence/provenance:
- Synthesis:

**8. Stop Conditions**
- Conditions that require asking the user instead of lowering quality:

**9. Final Deliverable**
- Proposed format:
- File or response structure:
```

End with: "Please confirm this plan or tell me what to revise before I start collecting."

## Coverage Rubric

- Breadth: covers distinct subcategories, audience segments, regions/languages, source types, and formats that matter for the task.
- Depth: each item explains the mechanism, why it works, reusable insight, and caveats.
- Evidence: source signals are appropriate for the claim type; time-sensitive or factual claims get links.
- Usefulness: items are actionable, comparable, and not padded.
- Originality: duplicates and obvious variants are merged or excluded.
- Synthesis: final output includes patterns, contrasts, opportunity angles, and gaps.

## Stop Conditions

Stop and ask the user when:

- Required tools or network access repeatedly fail.
- The confirmed quantity cannot be reached without padding low-quality items.
- The planned source class is blocked or inaccessible and no equivalent source class exists.
- The user-requested provenance standard cannot be met.
- A necessary workflow step would exceed available context or tool limits.
- Continuing would require changing the agreed output shape, scope, or quality bar.
