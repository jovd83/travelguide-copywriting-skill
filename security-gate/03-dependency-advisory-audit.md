# Pre-Ship Security Gate — Check 3/3: Dependency Advisory Audit

- **Check:** npm audit (or language-equivalent advisory scan)
- **Status:** **Satisfied by-substep** of check 1/3 (modern-dependency-guard)
- **Skill:** travelguide-copywriter
- **Version:** 1.0.0
- **Date:** 2026-05-31

## Dedup rationale

The pre-ship gate requires an advisory scan (`npm audit`, or for non-npm stacks a
`pip-audit` / `safety`-style scan). Per the gate's dedup rule, a check may be skipped
as a direct step only when it is already covered as a substep of another. Check 1/3
established by direct evidence that this skill has **no third-party dependency
manifest and imports only the Python standard library**. An advisory scan resolves
its findings from a dependency set; with an empty project dependency set there is no
advisory surface to scan.

## Tooling note

- This is not an npm project (no `package.json`), so `npm audit` is not applicable.
- `pip-audit 2.10.0` is available in the environment. There is **no project
  dependency manifest** (`requirements.txt` / `pyproject.toml`) to scope it to, and
  the runtime imports are all stdlib, so a project-scoped audit has no packages to
  resolve advisories against.

## Verdict

**PASS — no advisory surface.** No known-vulnerable dependency can be present because
the skill declares and imports no third-party dependencies. Satisfied by-substep; no
separate scan artifact is meaningful.

## Gate summary

| # | Check | How satisfied | Verdict |
|---|---|---|---|
| 1 | modern-dependency-guard | Direct | PASS |
| 2 | api-contract-sentinel | Direct | PASS |
| 3 | dependency advisory (npm/pip-audit) | By-substep of #1 | PASS |
