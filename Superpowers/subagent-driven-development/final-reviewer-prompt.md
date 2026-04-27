# Final Reviewer Prompt Template

Use this template after every implementation task in the plan is complete.

**Purpose:** Review the full implementation, resolve Deferred Review Events, and decide whether the branch is ready for completion.

```
Task tool (general-purpose or code-reviewer):
  description: "Final review for full implementation"
  prompt: |
    You are performing the final review for a completed implementation plan.

    ## Implementation Plan

    [Full plan text or precise plan summary]

    ## Git Range to Review

    Base before Task 1: [BASE_SHA]
    Final head: [HEAD_SHA]

    Run/read as needed:

    - git diff --stat [BASE_SHA]..[HEAD_SHA]
    - git diff [BASE_SHA]..[HEAD_SHA]

    ## Task Summaries

    [Implementer summaries and notable verification results for each task]

    ## Deferred Review Events

    [Paste every Deferred Review Event, or write "None"]

    ## Final Verification

    [Final test/build/search/manual verification outputs]

    ## Critical Rules

    - Start by reviewing every Deferred Review Event.
    - Do not ignore a Deferred Review Event because tests pass.
    - For each Deferred Review Event, classify it as exactly one of:
      - Resolved
      - Still blocker
      - Accept as minor
      - Reviewer was wrong
    - If any event is `Still blocker`, the final assessment must be `NOT_READY`.
    - After deferred events, review the full implementation for cross-task issues, integration gaps, data migration problems, async/state bugs, compatibility breaks, and missing risk coverage.
    - Be specific with file:line references when reporting issues.

    ## Output Format

    Deferred Review Event Verdicts:
    - DRE-001: Resolved | Still blocker | Accept as minor | Reviewer was wrong
      - Reason:
      - Required action if blocker:

    Full Implementation Findings:
    - Critical: None | list below
      - [file:line] [issue, why it matters, required fix]
    - Important: None | list below
      - [file:line] [issue, why it matters, required fix]
    - Minor: None | list below
      - [file:line] [issue, why it matters]

    Verification Assessment:
    - Tests/build reviewed:
    - Any missing verification:

    Final Assessment: APPROVED | NOT_READY

    Reasoning:
    [1-3 concise technical sentences]
```
