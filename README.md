# Travelguide Copywriter Skill

[![version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![status](https://img.shields.io/badge/status-stable-3fb950)](SKILL.md)
[![category](https://img.shields.io/badge/category-creation-0a7ea4)](SKILL.md)
[![validation](https://img.shields.io/badge/validation-GitHub%20Actions-2088ff)](.github/workflows/validate.yml)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

`travelguide-copywriter` turns a location and a traveler profile into a personalized, sensory-rich travel guide or roadbook — with live-verified dining and age-appropriate walking routes, written to read like real travel writing rather than brochure filler.

It resolves coordinates or place names into real geography, mines genuine walking and hiking routes filtered to the physical capacity of the group, sources restaurant recommendations from live web searches (never parametric memory), and drafts copy against a banned-clich&eacute; blocklist and a tone matrix. Output is sized to what the traveler actually asked for: a full multi-section roadbook when the request is open-ended, or a tight couple of paragraphs plus a dining pick when they ask for something short.

## What This Skill Does

- Resolves a location indicator (latitude/longitude, place name, address, or travel link) into administrative region, history, and nearby points of interest, using a dependency-free geocoding script with a live-search fallback.
- Mines real walking and hiking routes and filters them by traveler age tier (toddlers, seniors, active adults), so a route is never beyond the group's physical capacity nor needlessly soft.
- Sources live-verified dining recommendations from TripAdvisor / Google Reviews with numeric ratings and dated, attributed review quotes, and confirms dietary safety (celiac/gluten-free preparation, vegan mains, allergy handling).
- Drafts evocative, sensory copy using a Hook-Story-Experience framework and a tone matrix, auditing every draft against a banned-clich&eacute; blocklist.
- Sizes the deliverable to the request: full roadbook for open-ended asks, trimmed output for "keep it short" asks — trimming scaffolding, never rigor.
- Degrades honestly when live data is thin: surfaces what could be verified instead of fabricating ratings or review quotes.

## When To Use It

Use this skill when:

- A user asks for a travel guide, roadbook, itinerary, or destination write-up from coordinates, a place name, an address, or a maps link.
- The output should be personalized to a group's ages, interests, or dietary needs (e.g., a celiac grandparent, a vegan parent, a toddler, an adventurous couple).
- Restaurant or trail recommendations must be real and verifiable rather than invented from training data.
- The writing needs to be genuinely evocative and free of tourist-brochure clich&eacute;s.

## What This Skill Does Not Do

- It does not book travel, reserve restaurants, or transact anything on the user's behalf.
- It does not invent dining options, ratings, or review quotes — recommendations must come from live verification, and the skill degrades honestly when data is thin.
- It does not recommend routes beyond the stated physical capacity of the group's age tiers.
- It does not provide medical, legal, or safety guarantees; dietary-safety notes summarize live reviews and must still be confirmed on site.

## Install

Install by copying or cloning this folder into an Agent Skills directory supported by your agent.

With the Skills CLI, after this repository is published to GitHub:

```powershell
npx skills add jovd83/travelguide-copywriting-skill
```

For a fork, replace `jovd83` with the GitHub owner or organization that hosts the repository.

For repository-local sharing:

```powershell
New-Item -ItemType Directory -Force .agents\skills
Copy-Item -Recurse . .agents\skills\travelguide-copywriter
```

The skill follows the Agent Skills convention of a required `SKILL.md` file with optional supporting folders.

## Usage

Example prompt:

```text
Write me a travel guide for 41.8902, 12.4922. We're traveling with a 4-year-old, two parents
in their early 30s, and a 70-year-old grandmother who has coeliac disease. We love history.
Warm, storytelling tone please.
```

Best results come from providing:

- A location (coordinates, place name, address, or maps link).
- The traveler ages or group profile.
- Interests (history, adventure, culinary, relaxation, photography).
- Dietary needs (vegan, gluten-free/celiac, allergies).
- A tone preference and the desired length or format.

## Repository Layout

```text
travelguide-copywriting-skill/
|-- .github/
|   `-- workflows/
|       `-- validate.yml
|-- SKILL.md
|-- README.md
|-- CHANGELOG.md
|-- LICENSE
|-- agents/
|   `-- openai.yaml
|-- assets/
|   `-- roadbook_template.md
|-- references/
|   |-- dining_and_demographics.md
|   |-- geographic_lookup_guide.md
|   `-- tone_and_writing_guide.md
|-- scripts/
|   |-- geocode_and_trail_miner.py
|   `-- validate_skill.py
`-- evals/
    `-- evals.json
```

## Evaluation

The eval suite in `evals/evals.json` covers personalization, age-gated routing, dietary-safety verification, clich&eacute;-resistance under pressure, and format adaptivity. The skill was tuned with the `skill-creator` eval loop: a benchmarked iteration moved the with-skill pass rate from 87% to 100% by adding format adaptivity, a small-town dining fallback, and honest degradation under thin data.

Run the repository-local static validator:

```powershell
python scripts/validate_skill.py .
```

The same validator runs in GitHub Actions through `.github/workflows/validate.yml`.

## License

MIT. See [LICENSE](LICENSE).
