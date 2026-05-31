# Pre-Ship Security Gate — Check 1/3: Dependency Guard

- **Check:** modern-dependency-guard (run **directly**)
- **Skill:** travelguide-copywriter
- **Version:** 1.0.0
- **Date:** 2026-05-31
- **Reviewer:** Claude (Opus 4.8), on behalf of jovd83

## Scope

Review every third-party library, SDK, framework, or CLI the skill depends on at
runtime for deprecation, known-bad versions, or safer modern alternatives.

## Evidence

| Probe | Result |
|---|---|
| Dependency manifests (`package.json`, `requirements.txt`, `pyproject.toml`, `Pipfile`, `setup.py`) | **None present** |
| Imports in `scripts/geocode_and_trail_miner.py` | `argparse`, `json`, `ssl`, `sys`, `urllib.parse`, `urllib.request` — **all Python standard library** |
| Imports in `scripts/validate_skill.py` | `json`, `re`, `sys`, `pathlib`, `__future__` — **all Python standard library** |
| Bundled/vendored third-party code | None |

The `npx skills add ...` line in the README is end-user install guidance for the
Skills CLI, not a dependency this skill ships or executes.

## Findings

- **No third-party runtime dependency surface.** The skill runs on the Python
  standard library only, so there is nothing to flag as deprecated, abandoned, or
  pinned to a known-bad version, and no modern-alternative substitution is warranted.
- The one external coupling is to two public HTTP APIs (reviewed in check 2/3),
  not to a packaged library.

## Verdict

**PASS — no dependency risk.** No action required.
