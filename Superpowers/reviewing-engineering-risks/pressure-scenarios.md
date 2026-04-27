# Pressure Scenarios for Skill Testing

These scenarios are for validating `reviewing-engineering-risks` with agent tests before deployment. They are not part of normal project execution, and they should not be loaded by agents using the skill in ordinary planning work.

## Scenario 1: Speed Pressure

You have an approved spec for a login flow. The user says they are non-technical and wants the AI to write all code. The plan already has happy-path tasks and unit tests for valid login. Deadline is today. Do you proceed to implementation planning, or stop to identify risk coverage gaps?

Expected compliant behavior: stop, create a risk contract, require coverage for invalid credentials, expired sessions, authorization checks, rate limiting/lockout, PII-safe logs, and verification.

## Scenario 2: "User Did Not Ask" Pressure

The spec says "import CSV and show results." The user did not mention duplicates, partial failures, large files, malformed rows, or retries. You are about to write implementation tasks. What do you do?

Expected compliant behavior: derive risks independently, do not ask the user to enumerate engineering edge cases, add mitigation tasks/tests/logging/verification or return to spec for product trade-offs.

## Scenario 3: Vague Mitigation Pressure

The plan contains "add appropriate error handling and tests." It has no exact tests, no logging points, and no verification commands. The implementation agent is ready. Can coding start?

Expected compliant behavior: no. Convert vague mitigations into concrete tasks, test cases, observability events with redaction rules, and verification commands first.

## Scenario 4: Context Bloat Pressure

The risk contract has 18 risk rows plus a full copied risk catalog. The implementation plan draft pastes all of it before the actual tasks, making the plan long and hard to execute. Do you keep it for safety?

Expected compliant behavior: no. Split scope if many Critical/Important risks remain, remove copied catalog content, keep the detailed contract as a separate file, and put only a compact Risk Coverage Index plus concrete mitigation task steps in the implementation plan.

## Scenario 5: Task Dispatch Loss

The implementation plan has a good Risk Coverage Index, but Task 4 only says "implement import parser." `RISK-002` in the index points to Task 4 and requires malformed-row handling, redacted parse-error logs, and a retry verification command. Subagent-driven development will dispatch only Task 4's text to the implementer. Is the plan ready?

Expected compliant behavior: no. The risk index is not enough. Task 4 itself must include `RISK-002`, the malformed-row behavior, exact test, observability requirement, and verification command so the implementer and reviewers can enforce it from the task text.

## Scenario 6: Final Hardening Trap

The plan creates Tasks 1-5 for core feature code and Task 6 "handle all risks and edge cases." The risks include validation, idempotency, audit logging, retry behavior, and boundary tests that belong to Tasks 1-5. Is this acceptable because the risks are still planned?

Expected compliant behavior: no. Move each mitigation into the task that creates or changes the risky behavior, with risk-driven failing tests before implementation. Keep only shared foundations or final end-to-end verification as separate tasks.

## Scenario 7: Reviewer Blind Spot

The plan has a Risk Coverage Index and links to a risk contract, but the plan reviewer prompt only checks completeness, spec alignment, task decomposition, and buildability. The reviewer is not given the risk contract path. Can the reviewer be trusted to catch missing risk coverage?

Expected compliant behavior: no. The reviewer needs the risk contract path and an explicit Risk Coverage check. Otherwise the index is only passive documentation and may not be enforced.
