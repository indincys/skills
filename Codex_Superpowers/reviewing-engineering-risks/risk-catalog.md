# Engineering Risk Catalog

Use this catalog during `reviewing-engineering-risks`. It is intentionally technology-agnostic. Mark each category Applies, Does not apply, or Unknown with a reason.

## Requirements and Scope

- Ambiguous success criteria, hidden roles, conflicting permissions, unclear ownership
- Happy path specified but empty, invalid, repeated, cancelled, offline, timeout, or retry paths absent
- Product decision disguised as engineering detail: data retention, destructive actions, irreversible changes, user notification

## Inputs and Validation

- Empty, null, missing, malformed, duplicate, out-of-order, extremely large, extremely small, unicode, locale-specific, timezone-specific, or precision-sensitive input
- File/path issues: unsupported format, encoding, corrupt files, partial reads, permissions, disk full, unsafe paths
- Client-side validation without server-side validation; validation differs between UI/API/storage layers

## State, Lifecycle, and Concurrency

- Initialization before dependencies are ready; cleanup not called; stale caches; background jobs outliving UI/session
- Race conditions, double-clicks, duplicate submissions, repeated retries, idempotency gaps
- Partial failure: one component succeeds while another fails
- Offline/resume, app restart, page refresh, tab duplication, process crash, worker crash

## Data Integrity and Migrations

- Missing transaction boundaries, rollback gaps, duplicate keys, lost updates, ordering assumptions
- Schema changes without migration, migration without rollback, old data shape still present
- Serialization/deserialization mismatch, type coercion, number precision, timezone/date conversion
- Backfill, import/export, pagination, sorting, filtering, search index consistency

## External Integrations

- Network timeout, retry storm, rate limit, expired credentials, revoked permissions
- Third-party API schema change, unavailable service, partial response, inconsistent error format
- Webhooks delivered twice, out of order, late, or not at all
- Contract tests missing at service boundaries

## Security and Privacy

- Authentication confused with authorization; missing role checks at server/storage layer
- Injection: SQL/NoSQL/command/template/path; XSS; CSRF; SSRF; unsafe deserialization
- Secrets in code, logs, URLs, browser storage, crash reports, screenshots, or test fixtures
- PII over-collection, unredacted logs, missing audit trail for sensitive actions
- Cross-tenant or cross-user data exposure; insecure defaults; overly broad permissions

## Error Handling and Recovery

- Errors swallowed, retried forever, or exposed as raw stack traces
- No user-safe message, no support/debug correlation id, no recovery action
- Retry lacks backoff, jitter, max attempts, cancellation, or idempotency
- Destructive operation lacks confirmation, undo, backup, or recovery path

## Observability and Diagnostics

- No logs at component boundaries: UI -> API, API -> service, service -> database, service -> third party
- Logs omit request/job/import/session id, phase, key counts, duration, outcome, or error category
- Logs include secrets, tokens, file contents, PII, or excessive payloads
- No metric/alert/health signal for failures that users may not report
- No audit trail for permission, payment, admin, deletion, export, or privacy-sensitive actions

## Testing Coverage

- Unit tests cover logic but integration path untested
- Mocks prove mock behavior, not real behavior
- No regression test for known bug or credible failure mode
- Missing tests for empty/invalid/boundary/large/repeated/concurrent/timeout/retry/cancel/recovery paths
- No accessibility, keyboard, mobile/responsive, browser/OS, localization, timezone, or migration checks where relevant
- Tests pass without proving failure first; no red-green evidence for new behavior

## Performance and Resource Use

- N+1 queries, unbounded memory growth, large synchronous work on UI thread, blocked event loop
- Startup, first render, import/export, search, pagination, or background jobs degrade at realistic data size
- Missing cancellation, progress, chunking, streaming, cleanup, or resource limits
- Cache invalidation and eviction undefined

## Platform and Compatibility

- Browser, OS, device, filesystem, shell, locale, timezone, permissions, sandbox, or packaging differences
- Mobile touch/keyboard behavior, viewport changes, safe areas, reduced motion, high contrast, screen readers
- Version skew between client/server, app/database, worker/API, plugin/host, generated files/runtime

## Release, Configuration, and Operations

- Required env vars not validated at startup; unsafe defaults; config differs between dev/test/prod
- Deployment order matters but is undocumented; migrations not coordinated with app rollout
- No rollback, feature flag, data backup, or staged rollout for risky changes
- CI does not run the verification commands the plan relies on

## AI-Authored Code Risks

- Hallucinated APIs, libraries, flags, paths, or config keys
- Tests mirror the implementation instead of the requirement
- Overuse of mocks hides integration bugs
- Generated code compiles but violates existing architecture or product constraints
- Plan leaves "obvious" validation/logging/error handling to the implementation agent
- The human partner cannot detect missing edge cases, so absence of user concern is not evidence of safety
