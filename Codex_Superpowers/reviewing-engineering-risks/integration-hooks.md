# Integration Hooks

These snippets make `reviewing-engineering-risks` reliable in the Superpowers planning flow.

These are required integration changes, not automatic behavior. If the upstream Superpowers skills are not patched with these hooks, agents may skip `reviewing-engineering-risks` and may not check the Risk Coverage Index.

## Brainstorming

In `superpowers:brainstorming`, change the terminal state from invoking `writing-plans` directly to invoking `reviewing-engineering-risks`.

Recommended wording:

```markdown
After the user approves the written spec, invoke reviewing-engineering-risks before writing-plans. Pass the spec/design path and current project context. Do not invoke writing-plans until the risk contract passes its gate.
```

The next skill after brainstorming becomes:

`brainstorming -> reviewing-engineering-risks -> writing-plans`

## Writing-Plans

In `superpowers:writing-plans`, add the risk contract as a required planning input.

Recommended wording:

```markdown
Before task decomposition, require either:
- a risk contract from reviewing-engineering-risks, or
- an explicit human-approved waiver.

If the risk contract exists, create a compact Risk Coverage Index (`Risk ID -> Task(s) -> Verification`) and make every Critical and Important mitigation appear inside the relevant task text as concrete steps with tests, observability, and verification commands. Link to the full risk contract instead of copying it into the plan. The index alone is not executable. Missing task-level coverage is a plan failure.

Place risk work in the task that owns the risky behavior. Shared logging, audit, validation, or test-fixture foundations may be early prerequisite tasks. Do not defer mitigations to a final hardening task; final tasks may verify coverage, not introduce first-time mitigation.
```

## Plan Reviewer

In `writing-plans/plan-document-reviewer-prompt.md`, add this check:

```markdown
| Risk Coverage | Every Critical and Important risk from the risk contract is represented by implementation task steps, tests, observability, and verification commands |
| Plan Focus | The plan links to the risk contract and uses a compact Risk Coverage Index instead of pasting the full risk analysis |
| Task Self-Containment | Each task dispatched to an implementer includes the risk IDs and risk-driven requirements it owns; the task does not require the implementer to read the index or risk contract |
| TDD Order | Each risk-owning task writes risk-driven failing tests before production code and includes exact verification commands |
```

Approve only if risk coverage is present or the plan includes an explicit accepted waiver.

The reviewer must receive the risk contract path as an input:

```markdown
**Risk contract for reference:** [RISK_CONTRACT_FILE_PATH]
```

Without the risk contract, the reviewer can only check formatting, not whether all important risks were covered.

## Subagent-Driven Development

In `superpowers:subagent-driven-development`, add an execution preflight before dispatching the first implementer:

```markdown
Before dispatching any task, if the plan has a Risk Coverage Index, verify each listed risk ID appears inside the text of at least one implementation task. If any risk ID appears only in the index or linked risk contract, stop and fix the plan before dispatching subagents.
```

When dispatching spec compliance reviewers, include the task text exactly as sent to the implementer. If that task has a `Risk Coverage` block, the reviewer must treat every risk-driven requirement as part of the requested spec.

Do not rely on subagents reading the full plan, the index, or the risk contract.

## Normal File Flow

1. `brainstorming` writes `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`
2. `reviewing-engineering-risks` reads the spec and writes `docs/superpowers/risks/YYYY-MM-DD-<topic>-risk-contract.md`
3. `writing-plans` reads both files and writes `docs/superpowers/plans/YYYY-MM-DD-<topic>.md`
4. The plan links to the risk contract, includes a compact Risk Coverage Index, and embeds tasks/tests/logs/verification for each important risk inside the relevant task text
5. `subagent-driven-development` dispatches each task with its embedded risk requirements; spec reviewers check those requirements from the task text
