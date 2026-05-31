# Pre-Ship Security Gate — Check 2/3: API Contract Sentinel

- **Check:** api-contract-sentinel (run **directly**)
- **Skill:** travelguide-copywriter
- **Version:** 1.0.0
- **Date:** 2026-05-31
- **Reviewer:** Claude (Opus 4.8), on behalf of jovd83

## Scope

Audit the skill's API-consuming code against authoritative contracts for endpoint
drift, missing operations, and schema mismatches.

## Surface

The skill is a **client** of two public, read-only APIs via `scripts/geocode_and_trail_miner.py`:

| Endpoint | Method | Purpose | Auth |
|---|---|---|---|
| `https://nominatim.openstreetmap.org/reverse` | GET | Reverse geocode lat/lon to administrative detail | None (User-Agent required) |
| `https://overpass-api.de/api/interpreter` | POST (urlencoded Overpass QL) | Find nearby trails, parks, historic sites | None |

The skill publishes **no API of its own**, so there is no owned contract that
clients could break, and no OpenAPI/AsyncAPI/Protobuf spec is shipped or bound.

## Findings

- **No formal contract to drift against.** Nominatim and Overpass do not publish a
  versioned machine contract this skill is pinned to; they are queried as a best-effort
  enrichment source.
- **Drift is handled gracefully, not assumed away.** Both calls run under a 15s timeout
  and are wrapped so that a schema change, outage, or non-200 response degrades to the
  skill's documented live-search fallback (`SKILL.md` Step 2, `references/geographic_lookup_guide.md`)
  rather than crashing or fabricating data. `query_overpass_nearby` returns an explicit
  `error` field on failure.
- **Compliant request hygiene.** A descriptive `User-Agent` is sent (Nominatim usage
  policy requirement); requests are read-only; no credentials or PII are transmitted.
- **TLS verification restored this release** (see check 1 / CHANGELOG Security note),
  removing a man-in-the-middle exposure on these calls.

## Verdict

**PASS — no contract drift risk.** Client usage is correct, read-only, and
fails safe. No action required.
