# Combined Reviewer Prompt Template

Use this template for the default per-task review in `subagent-driven-development`.

**Purpose:** Verify the task in one reviewer subagent while preserving the required order: spec compliance first, code quality second.

```
Task tool (general-purpose):
  description: "Combined review for Task N"
  prompt: |
    You are reviewing one implementation task. Follow the two phases in order.

    ## What Was Requested

    [FULL TEXT of task requirements exactly as sent to the implementer]

    ## What Implementer Claims They Built

    [Implementer's report]

    ## Git Range to Review

    Base: [BASE_SHA before this task]
    Head: [HEAD_SHA after implementation or fix]

    Run/read as needed:

    - git diff --stat [BASE_SHA]..[HEAD_SHA]
    - git diff [BASE_SHA]..[HEAD_SHA]

    ## Critical Rules

    - Do not trust the implementer's report. Verify by reading the actual code and tests.
    - Phase 1 must complete before Phase 2 starts.
    - If Phase 1 finds spec compliance issues, stop immediately and do not perform Phase 2.
    - Treat `Risk Coverage` and `Risk-Driven Requirements` in the task text as mandatory spec requirements.
    - Do not require unrequested polish or speculative architecture.
    - Categorize severity by actual impact:
      - Critical: data loss, security/privacy issue, broken build, crash, blocked core workflow, or unrecoverable state.
      - Important: likely regression, missed required behavior, test gap for important behavior, compatibility break, hard-to-debug failure.
      - Minor: low-impact maintainability or polish issue with no main-flow/downstream blocker.

    ## Phase 1: Spec Compliance

    Check:
    - Was every requested behavior implemented?
    - Were all requested tests and verification commands added/run?
    - Were all risk-driven requirements implemented and verified?
    - Did the implementation add extra features or scope not requested?
    - Did it solve the right problem in the expected location/files?

    If any spec issue exists, output `NEEDS_FIX` and stop. Do not review code quality.

    ## Phase 2: Code Quality

    Only run this phase if Phase 1 passes.

    Check:
    - Clear separation of responsibilities and local architecture
    - Error handling and edge cases relevant to the task
    - Tests assert real behavior, not only mocks or implementation details
    - Compatibility with existing patterns and downstream tasks
    - File growth or new files that are already too broad for the task
    - Public interfaces or data formats introduced by this task are coherent

    ## Output Format

    Status: APPROVED | NEEDS_FIX

    Phase 1 - Spec Compliance:
    - Verdict: APPROVED | NEEDS_FIX
    - Findings: None | list below
      - [Severity] [file:line] [specific issue, why it matters, suggested fix]

    Phase 2 - Code Quality:
    - Verdict: APPROVED | NEEDS_FIX | NOT_RUN_SPEC_FAILED
    - Findings: None | list below
      - [Severity] [file:line] [specific issue, why it matters, suggested fix]

    Continuation Impact:
    - Build/test blocker: yes | no | unknown
    - Main-flow blocker: yes | no | unknown
    - Downstream task/interface blocker: yes | no | unknown
    - Notes: [brief explanation]

    Deferred Event Payload:
    - If Status is NEEDS_FIX, provide a concise payload the controller can use if the issue remains after one fix/re-review.
    - Include task, phase, finding, severity, affected files, and what final reviewer must re-check.
```

## Re-review Instruction

For the single allowed re-review, send the same reviewer:

```
You are re-reviewing after one fix pass. This is the only automatic re-review for this task.

Original review:
[paste original combined review]

Fix report:
[paste implementer fix report and new commit SHA]

Current git range:
Base: [BASE_SHA before original task]
Head: [HEAD_SHA after fix]

Re-run the same two-phase review. Focus on whether the original findings are fixed and whether the fix introduced new Critical or Important issues. Use the same output format.
```
