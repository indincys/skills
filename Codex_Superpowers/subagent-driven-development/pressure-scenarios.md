# Pressure Scenarios

These scenarios guard the compact review flow for `subagent-driven-development`.

## Scenario 1: Default review dispatch

**Pressure:** A task completes and the controller is trying to move quickly.

**Old failure:** The controller dispatches a spec reviewer and then a separate code quality reviewer, burning two reviewer subagents per task.

**Expected behavior:** Dispatch exactly one combined reviewer for the task. That reviewer must run spec compliance first and code quality second.

## Scenario 2: Quality review before spec approval

**Pressure:** The controller wants to save time by reviewing quality while spec gaps remain.

**Old failure:** The two-reviewer flow can encourage separate review decisions and extra loops.

**Expected behavior:** The combined reviewer must stop after Phase 1 when spec compliance fails. Code quality review only runs after spec compliance passes.

## Scenario 3: Reviewer finds issues after first implementation

**Pressure:** The reviewer finds valid issues and the controller is tempted to continue or start an unbounded loop.

**Old failure:** The skill says to repeat until approved.

**Expected behavior:** The implementer fixes once, then the same combined reviewer performs one re-review.

## Scenario 4: Re-review still has unresolved findings

**Pressure:** The human partner cannot evaluate code and does not want per-task loops to explode.

**Old failure:** The controller either loops indefinitely or escalates technical judgment to the human.

**Expected behavior:** Record a Deferred Review Event with enough detail for final review, run a continuation gate, then continue only if the branch can still build/test and the next task can proceed.

## Scenario 5: Final review with deferred events

**Pressure:** All implementation tasks are done and the controller wants to finish quickly.

**Old failure:** Deferred issues can be lost in chat history or context compaction.

**Expected behavior:** The final reviewer receives every Deferred Review Event and must classify each one before the implementation can be considered approved.
