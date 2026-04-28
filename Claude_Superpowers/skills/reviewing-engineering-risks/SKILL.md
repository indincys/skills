---
name: reviewing-engineering-risks
description: Use when an approved design or spec is about to become an implementation plan and engineering risks such as edge cases, failures, observability, security, data integrity, or verification gaps may be missed before coding.
---

# Reviewing Engineering Risks

## Overview

Before implementation planning, identify credible ways the software could fail and force each important risk into concrete work. The human partner must not be expected to name engineering risks; the agent owns risk discovery.

**Core principle:** A risk is not handled until it maps to task, test, observability, and verification.

## Hard Gate

Do not write code, scaffold projects, or finalize implementation tasks until this review passes.

Every Critical or Important risk must be one of:

- **Mitigated:** Covered by a specific task, test or verification, and observability when diagnosis would otherwise be hard.
- **Eliminated:** Removed by a spec or architecture change.
- **Accepted:** Explicitly accepted by the human partner after impact and trade-offs are shown.

Vague "test edge cases", "add logging", "handle errors", or "not applicable" without a reason means the review fails.

## When to Use

Use after brainstorming produces an approved spec/design and before writing-plans decomposes implementation tasks. Use especially when the user is non-technical, code is AI-authored, or the change touches state, data, auth, external services, platform behavior, migrations, async work, UI workflows, release configuration, or user-visible failures.

Do not use as a substitute for systematic-debugging after a bug exists. This is pre-implementation risk discovery.

## Required Inputs

- Approved spec/design and acceptance criteria
- Current project files, tests, logging, docs, and deployment assumptions
- Target users, platforms, permissions, data sensitivity, and failure tolerance
- Known external dependencies: APIs, databases, files, auth providers, queues, browsers, operating systems

## Output

Write a risk contract to:

`docs/superpowers/risks/YYYY-MM-DD-<feature-name>-risk-contract.md`

If the project has a different docs convention, follow it and state the chosen path.

The risk contract is an input to writing-plans. The implementation plan should link to it, include a compact Risk Coverage Index, and embed every relevant mitigation directly inside the task text that will be dispatched to an implementer. Do not copy the raw risk catalog into the plan.

## Process

### 1. Build the Risk Inventory

Review the spec and codebase against `risk-catalog.md`. For each category, mark Applies, Does not apply, or Unknown with a short reason.

Never ask the human partner to provide the risk list. Ask them only for product choices, tolerance, or trade-offs you cannot infer.

### 2. Rank Severity

| Severity  | Use When                                                                                                                                                |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Critical  | Could cause data loss, security/privacy breach, payment/permission error, unrecoverable state, outage, crash loop, or blocked core workflow             |
| Important | Likely regression, confusing failure, missed edge case, hard-to-debug production issue, accessibility/compatibility break, performance/resource problem |
| Minor     | Low-impact issue with clear workaround and low likelihood                                                                                               |

If uncertain between Important and Minor, choose Important.

### 3. Map Mitigations

Every Critical or Important risk needs a row:

| Field           | Required Content                                                      |
| --------------- | --------------------------------------------------------------------- |
| Risk ID         | Stable label, e.g. `RISK-003`                                         |
| Scenario        | Concrete failure story, not a generic category                        |
| Severity        | Critical, Important, or Minor                                         |
| Mitigation task | Exact task that prevents or handles it                                |
| Test coverage   | Specific unit/integration/e2e/regression/contract/manual test         |
| Observability   | Logs, metrics, audit trail, traces, or explicit reason none is needed |
| Verification    | Exact command or scenario that proves mitigation works                |

Observability is required when a failure would be hard to reproduce, crosses component boundaries, depends on external systems, affects user data, or would need diagnosis after release. Logs must name event points and redaction rules.

### 4. Control Scope and Context

The risk contract must be triaged, not exhaustive prose.

- Include detailed rows only for Critical and Important risks.
- Keep Minor, Eliminated, and Does not apply items in a short appendix or omit them if they add no planning value.
- Do not paste `risk-catalog.md` into the risk contract or implementation plan.
- If there are more than 10-12 Critical/Important risks, or risk handling would dominate the plan, stop and decompose the spec into smaller deliverables.
- Combine related risks only when they share the same mitigation, test, observability, and verification.

The goal is not a larger plan. The goal is that no important failure mode depends on the implementer remembering it later.

### 5. Feed Writing-Plans

When invoking writing-plans, pass both files:

- Spec/design path
- Risk contract path

Writing-plans must create:

- A compact Risk Coverage Index: `Risk ID -> Task(s) -> Verification`
- Self-contained implementation tasks that include every relevant Critical and Important mitigation, test, observability item, and verification command

The Risk Coverage Index is for traceability and review, not execution. It is effective only if writing-plans, plan review, and subagent-driven-development explicitly check it. Each task must carry the risk requirements it owns because subagent-driven-development dispatches task text to a fresh implementer. Do not rely on implementers reading the index, the full plan, or the risk contract.

Place mitigations by code ownership:

- Put each mitigation in the task that creates or changes the risky behavior.
- Do not create one final "risk hardening" task for mitigations that belong in earlier feature tasks.
- Cross-cutting foundations, such as logging helpers, audit schema, test fixtures, or shared validation utilities, may be their own early task before dependent feature tasks.
- A final verification task may check end-to-end risk coverage, but it must not be where missing mitigations are first implemented.

For every task that mitigates risk, include a small block:

```markdown
**Risk Coverage:**
- `RISK-003`: [scenario this task must handle]

**Risk-Driven Requirements:**
- [behavior, test, log/audit/metric, verification command]
```

Within each risk-owning task, follow TDD order: write the risk-driven failing test first, verify it fails for the expected reason, implement the behavior/logging/validation/recovery path, then verify it passes. Observability that cannot be asserted in an automated test still needs an explicit verification step before the task can be reported done.

The plan should link to the full risk contract for detail instead of embedding it unless the contract is very small. If a mitigation changes product behavior or architecture, return to the spec/design and get approval before planning.

### 6. Gate Decision

The review passes only when:

- All Critical and Important risks are mitigated, eliminated, or explicitly accepted.
- Each mitigation appears inside the relevant task text, not only in the Risk Coverage Index.
- Tests cover normal, boundary, invalid, empty, repeated, concurrent, external-failure, and recovery paths wherever relevant.
- Observability covers component boundaries and sensitive data is redacted.
- Verification commands or manual scenarios are exact enough for another agent to run.

## Example Risk Contract Row

| Risk ID  | Scenario                                                                          | Severity | Mitigation Task                                              | Test Coverage                                                         | Observability                                                                  | Verification                          |
| -------- | --------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------- |
| RISK-001 | Import is interrupted after writing half the records, leaving duplicates on retry | Critical | Implement idempotent import transaction with stable row keys | Integration test retries same file after simulated mid-import failure | Log import id, phase, row counts, rollback/retry outcome; redact file contents | `npm test -- import-idempotency.test` |

## Common Mistakes

| Mistake                                       | Fix                                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------------- |
| Listing risks without mapping work            | Add task, test, observability, verification columns                               |
| Asking the non-technical user for edge cases  | Derive risks yourself; ask only for tolerance or product trade-offs               |
| Treating happy-path tests as enough           | Add negative, boundary, retry, recovery, and regression tests                     |
| "No logging needed" because tests exist       | Add observability for failures that only appear in real environments              |
| Leaving risks outside the plan                | Convert each important risk into task steps before coding                         |
| Accepting vague mitigations                   | Replace with exact file/task/test/command details during writing-plans            |
| Dumping the whole risk contract into the plan | Link to the contract; put only the Risk Coverage Index and task steps in the plan |
| Putting risks only in the index               | Embed each owned risk directly in the task text dispatched to implementers        |
| Saving risk work for a final hardening task   | Put mitigations in the tasks that create or modify the risky behavior             |

## Red Flags - Stop Planning

- "We'll handle edge cases during implementation"
- "Tests can be added after"
- "The user did not mention this risk"
- "This is probably fine"
- "Add appropriate error handling"
- "Add logging where needed"
- "Manual testing should be enough"
- "The index points to the task, so the task does not need to repeat the risk"
- "The reviewer will infer risk coverage from the index"
- "Subagent-driven-development will automatically enforce linked risk contracts"
- "We'll add all risk handling in a final hardening task"
- A task writes production behavior before its risk-driven failing test
- The risk section overwhelms the implementation tasks
- A Critical or Important risk has no task, test, observability, or verification

All of these mean the risk review has failed. Fix the spec or plan before implementation.
