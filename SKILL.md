---
name: travelguide-copywriter
description: Use when writing high-quality travel guides, roadbooks, or itineraries. Sourced inputs can include coordinates, links, or place names. It supports personalization based on traveler ages, interests, and dietary needs, and uses live-verified TripAdvisor or Google reviews for restaurant recommendations.
license: MIT
metadata:
  author: jovd83
  version: "1.0.0"
  maturity: "stable"
  category: "creation"
---

# Travelguide Copywriter Skill Playbook

This playbook outlines the exact step-by-step procedure to resolve geographic inputs, gather live-verified restaurant data, plan age-appropriate hikes, and draft compelling, sensory-rich copywriting for travel guides or roadbooks.

## Execution Workflow

1. **Parse Input Parameters**
   - Extract the location indicator (latitude/longitude coordinates, place name, address, or travel link).
   - Extract the demographic variables:
     - `ages`: Ages of the traveling group (e.g., seniors, adults, teenagers, toddlers).
     - `interests`: Primary interests (e.g., history, culinary, adventure, photography, relaxation).
     - `dietary_needs`: Food restrictions (e.g., vegan, gluten-free/celiac, vegetarian, allergies).
   - Extract style preferences (e.g., poetic, minimalist, storytelling) and target format.
   - Extract the **requested scope**. This governs how much you produce, and it matters as much as the content itself. Listen for cues like "short," "a couple of paragraphs," "just a dining pick," "quick," "a full roadbook," or "the works." A traveler who asks for two paragraphs and gets a four-section template feels unheard, even if every section is excellent. The full roadbook is the default *when the request is open-ended*, not a fixed deliverable to impose on every prompt.

2. **Resolve Geolocation and Basic Facts**
   - If coordinates are provided, execute the python geocoding script:
     ```powershell
     python ./scripts/geocode_and_trail_miner.py --lat <latitude> --lon <longitude>
     ```
   - If coordinates are not provided, or to enrich resolved data, run a web search to find the municipality, region, and primary historical context:
     ```
     [place name] history landmarks and geography
     ```
   - For detailed lookup guidelines and fallback techniques, read [geographic_lookup_guide.md](./references/geographic_lookup_guide.md).

3. **Mine Trail and Walking Route Information**
   - Query live search or open street map details to find real hiking or walking trails in the resolved region.
   - Filter activities strictly by physical capability dictated by traveler `ages`:
     - Toddlers/Seniors: Limit to flat stroller/wheelchair-accessible paths, paved loops, or short walks (< 3 km).
     - Teenagers/Active Adults: High-energy hikes, scrambles, or longer distances (> 8 km).
   - Read [geographic_lookup_guide.md](./references/geographic_lookup_guide.md) to parse trail stats (distance, elevation change, estimated duration, difficulty) and safety instructions.

4. **Source Live-Verified Dining and Reviews**
   - Execute web searches targeting trusted review aggregators (TripAdvisor, Google Reviews) for the resolved area, appending `dietary_needs` and demographic interest tags:
     ```
     site:tripadvisor.com OR site:google.com restaurants in [city] "[dietary need]" reviews rating
     ```
   - Confirm active status, the specific average rating (e.g., "4.8/5 on Google Reviews"), and extract a live traveler comment verifying dietary safety (e.g., "Safe gluten-free kitchen") or family suitability. Attribute every quote with its source and a real month + year (e.g., "TripAdvisor, April 2026") — that specificity is what makes a quote read as verified rather than invented, so use the actual date from the review, not a vague "2025/26."
   - The whole point of this skill is that the recommendations are *real*. That value evaporates the instant a quote is fabricated. So when live data is thin — a page 403s, a small town has few reviews, you can confirm the restaurant and rating but can't retrieve a clean recent quote — degrade honestly rather than inventing. Widen the search, fall back to the verification you *could* confirm and say the quote couldn't be retrieved, or recommend a verifiable alternative. An honest "I couldn't pull a recent quote, but the kitchen is AIC-certified" beats a plausible-sounding quote that never existed. Never source dining picks or reviews from parametric memory.
   - Read [dining_and_demographics.md](./references/dining_and_demographics.md) for specialized query formats and safety verification rules.

5. **Draft Sensory Copywriting**
   - Open [tone_and_writing_guide.md](./references/tone_and_writing_guide.md) to select the appropriate copywriting framework (e.g., PAS, AIDA, Hook-Story-Offer) and review the tone definitions.
   - Check the **Banned Words & Cliché Checklist** in [tone_and_writing_guide.md](./references/tone_and_writing_guide.md) to ensure all tourist jargon is eliminated.
   - Write evocative, descriptive paragraphs highlighting the sights, sounds, smells, and atmosphere of the destination.

6. **Format and Assemble — Sized to the Request**
   - Decide the format from the scope you captured in Step 1. The quality bars never move — sensory copy free of clichés, age-appropriate routes, and live-verified dining hold regardless of length. What flexes is the *scaffolding*.
     - **Open-ended request** ("write me a travel guide / roadbook"): use the full structure in [roadbook_template.md](./assets/roadbook_template.md) — Location Profile, Sensory Portrait, Walk/Hike, Live-Verified Dining, Practical Logistics.
     - **Bounded request** ("short," "a couple of paragraphs," "just a dining pick"): deliver only what was asked. Drop the profile table, the section headers, the logistics block — keep the writing and the verified dining. A tight two-paragraph piece with one rigorously-sourced restaurant is a *better* answer to "keep it short" than a complete roadbook, because it respects the traveler's stated need.
     - **In between**: take the relevant sections and leave the rest. The template is a palette, not a checklist.
   - When you trim, trim scaffolding, never rigor. It's fine to drop the logistics table; it's not fine to drop the live verification behind a dining pick.
   - Deliver the final Markdown to the user.

---

## Examples

### Example 1: Coordinates + Diverse Ages + Vegan Diet

#### Input
- **Location**: `43.7230, 10.3966`
- **Ages**: Toddler (3 yo), Parents (35 yo), Grandparents (68 yo)
- **Interests**: History and relaxation
- **Dietary Needs**: Vegan
- **Tone**: Elegant and informative

#### Output
```markdown
# Roadbook Entry: Piazza dei Miracoli, Pisa

*A timeless canvas of white marble rising from green lawns, where medieval engineering and Tuscan sun create a mesmerizing architectural ballet.*

---

## 🛈 Location Overview
- **Coordinates**: 43.7230, 10.3966
- **Region**: Pisa, Tuscany, Italy
- **Pacing**: Leisurely (Toddler & Senior Friendly)

The scent of warm grass and freshly baked chestnut flour cakes drafts on the warm Tuscan breeze as you step onto the lawns of the Campo dei Miracoli. Here, the Leaning Tower stands in defiant, gravity-taunting grace beside the Romanesque Duomo and the circular Battistero. Walking here is flat and smooth, making it ideal for strollers and easy strolls.

---

## 🥾 Customized Walk: The Marble and Meadow Loop
- **Distance**: 1.8 km
- **Elevation Change**: +5 m (Flat)
- **Difficulty**: Very Easy / Stroller Accessible
- **Estimated Duration**: 1 hour

1. **Start Point (Porta Nuova)**: Enter the ancient city wall through Porta Nuova, providing a striking first view of the Duomo.
2. **The Baptistery (Battistero di San Giovanni)**: Stroll along the paved path to the circular baptistery. Step inside to listen to the extraordinary, cathedral-like acoustics if timed during the vocal demonstrations.
3. **Piazza Lawns**: Follow the paved walkway alongside the Cathedral. The flat grass borders provide perfect resting points for grandparents and safe play areas for toddlers.
4. **The Leaning Tower**: Conclude at the base of the iconic tower. (Note: Climbing the tower requires scaling 294 steep, spiral steps, which is not recommended for seniors or toddlers; enjoy the optical illusion from the safety of the base).

---

## 🍽️ Live-Verified Dining (Vegan Friendly)

### 🥇 Vegan & Vegetarian Bistro: *Vegan Come Amore*
- **Rating**: 4.8/5 (192 Google Reviews)
- **Price Point**: $$
- **Atmosphere**: Cozy, family-friendly, low-sensory environment.
- **Dietary Safety**: 100% Vegan kitchen.
- **Live Sourced Review (TripAdvisor, May 2026)**: *"Perfect for families! They had highchairs, the staff was extremely gentle with our toddler, and the vegan lasagna was outstandingly rich. Highly recommend the chickpea flour panissa."*
- **Location**: Via Santa Maria, 103 (200m from the Tower)

---

## ⚙️ Practical Logistics
- **Restrooms**: Accessible public restrooms equipped with changing tables are located next to the Museo dell'Opera del Duomo.
- **Best Time to Visit**: Arrive by 8:30 AM to capture the soft morning light on the marble before the tourist buses arrive, or at 6:00 PM for the golden sunset hour.
```

---

## Troubleshooting

| Issue | Root Cause | Corrective Action |
|---|---|---|
| **Python Script fails to geocode** | Invalid coordinate format or network connection to Nominatim API down. | Fall back to manual geocoding. Run a web search: `latitude longitude to address converter` and resolve manually. |
| **No dining options matching dietary needs** | Small or remote town with limited restaurant data. | Expand search radius. Search for `"gluten free" or "vegan" friendly options in [nearest major town]`. Recommend local whole-food ingredients (e.g., "Look for local bakeries serving Cecina/Farinata, a naturally vegan/gluten-free chickpea pancake standard in Tuscany"). |
| **Hike trail unavailable or unsafe** | Severe weather warnings or permanently closed trails found in search. | Query local forums or official park website live notices. Select paved pathways, village walking tours, or museum strolls as safe, low-impact alternatives. |
| **Copywriting feels dry/ encyclopedic** | Too much factual detail copied directly from Wikipedia. | Strip out excessive dates and lists of names. Rewrite using the sensory copywriting instructions in [tone_and_writing_guide.md](./references/tone_and_writing_guide.md). |
| **Output feels bloated / ignores a "keep it short" request** | The full roadbook template was applied to a bounded request. | Re-read the scope cue from Step 1 and re-assemble per Step 6: keep the writing and the verified dining, drop the profile table, section headers, and logistics the traveler didn't ask for. |
| **Can't retrieve a recent dining review quote** | Page blocked (403), or a small town with sparse reviews. | Degrade honestly per Step 4: widen the search, or present the rating/certification you *could* verify and note the quote couldn't be retrieved. Never fabricate a quote or a date. |
