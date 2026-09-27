# Changelog

All notable changes to `travelguide-copywriting-skill` are documented here.

This project adheres to [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2.0.0 - 2026-09-27

### Changed

- **BREAKING:** the skill is named `travelguide-copywriting-skill`, matching its folder and repository (it was `travelguide-copywriter`). The trigger is now `$travelguide-copywriting-skill`. README, `agents/openai.yaml`, evals and the validator follow.
- `travelguide-composer` refers to it by this name.

## 1.0.0 - 2026-05-31

### Added

- Format adaptivity: output is now sized to the request. Open-ended asks get the full roadbook; "keep it short" asks get a trimmed deliverable, trimming scaffolding rather than rigor (`SKILL.md` Step 1 scope cue and Step 6).
- Honest-degradation guidance for thin live data: when a review page is blocked or a town has sparse coverage, the skill surfaces what it could verify instead of fabricating a rating or quote (`SKILL.md` Step 4).
- Quote-dating discipline: dining review quotes must carry the real source plus month and year.
- Repository-local validator in `scripts/validate_skill.py`.
- GitHub Actions validation workflow in `.github/workflows/validate.yml`.
- Codex/OpenAI UI metadata in `agents/openai.yaml`.
- GitHub-ready README, MIT license, and Keep-a-Changelog history.
- `author` and `version` metadata in `SKILL.md` frontmatter.

### Changed

- The dining rating bar moved from a hard ">= 4.3" gate to guidance with an explicit small-town fallback: recommend the best genuinely verifiable option and be transparent about a low score rather than inventing a higher-rated place (`references/dining_and_demographics.md`).

### Security

- The geocoding script no longer disables TLS certificate verification. Nominatim and Overpass serve valid certificates, so verification is restored to prevent man-in-the-middle tampering of geocoding and landmark data (`scripts/geocode_and_trail_miner.py`).

### Validation

- `python scripts/validate_skill.py .`
- JSON parse checks for eval metadata.
- Pre-ship dependency and contract review (see release artifacts).
