# Live Dining & Demographics Reference Guide

Use this guide to search, verify, and document live dining recommendations that strictly align with traveler ages, dietary constraints, and specific interest profiles.

---

## 1. Sourcing Live-Verified Restaurant Data

To ensure maximum accuracy, restaurant recommendations must never be generated from pre-training/parametric knowledge. You must perform live web searches during execution to verify the restaurant is open, active, and highly rated.

### Sourcing Target Platforms
- **TripAdvisor**: Excellent for international travelers, detailed dietary filters, and family-friendliness reviews.
- **Google Reviews (via Google Maps)**: Excellent for local active status, up-to-date star ratings, precise addresses, and recent traveler comments.
- **Yelp**: Helpful for US-based urban locations.

### Live Sourced Review Search Patterns
To find high-quality, live listings, execute these search strings:
1. **General/Dietary search**:
   ```
   site:tripadvisor.com/Restaurant_Review "[resolved city/neighborhood]" "[dietary need]" rating reviews
   ```
2. **Recent customer validation**:
   ```
   "restaurants in [resolved city]" "[dietary need]" (celiac OR vegan OR allergy) reviews rating
   ```
3. **Specific family/demographic atmosphere validation**:
   ```
   site:tripadvisor.com OR site:google.com "[restaurant name] [city]" (kids OR stroller OR quiet OR romantic) reviews
   ```

---

## 2. Dietary Requirement Verification Protocol

You must audit reviews to confirm safety, especially for severe restrictions like celiac disease or nut allergies.

```
[Target Restaurant Found]
         │
         ▼
[Step 1: Check Rating] ────────► Aim for ~4.3+ stars on Google/TripAdvisor where the
         │                        destination supports it (see fallback below)
         ▼
[Step 2: Dietary Search] ──────► Query reviews for "[restaurant name] [city] [dietary key]"
         │
         ▼
[Step 3: Extract Live Quote] ──► Extract a recent direct user quote confirming safety
                                  (e.g., "safe for celiacs, separate fryer used")
```

**On the ~4.3 rating bar — guidance, not a gate.** In a city with a deep restaurant scene, holding the line at 4.3+ is easy and worth doing; it filters out the mediocre. But a hard threshold breaks in small or remote places, where the best genuinely-verifiable option for a given diet may simply sit below it. In that situation, do not invent a higher-rated restaurant, and do not silently drop the recommendation the traveler is counting on. Pick the best option you can actually verify, recommend it, and be transparent about the score (e.g., "Hallstatt is tiny, so this is the highest-rated verified vegan option in the village — 3.5/5, with dated reviews confirming labelled vegan mains"). Honesty about a thin field is more useful to a traveler than a fabricated ideal. Match the bar to the place, not the place to the bar.

### Safety Audit Guidelines:
- **Vegan**: Ensure reviews explicitly confirm distinct, plant-based main courses, rather than just "side salads."
- **Gluten-Free / Celiac**: Look for comments verifying a *separate preparation area*, dedicated fryers, or gluten-free menu certification. **Do not recommend bakeries or pizza places with high cross-contamination risk unless celiac-safe practices are specifically praised in live reviews.**
- **Allergies**: Search for keywords like "allergy-friendly," "staff accommodated allergy," or "informed the chef."

---

## 3. Demographics and Interest Sourcing Matrix

Use the matrix below to tailor the dining selection to the group profile:

| Traveler Profile | Atmospherics | Location Preferences | Sourced Review Keywords to Target |
|---|---|---|---|
| **Toddlers / Young Kids** | Casual, spacious, high kid-friendly noise tolerance. Highchairs available. | Near parks, walking streets, or the trailhead. | `"kids," "highchairs," "spacious," "stroller accessible," "play area"` |
| **Seniors (65+)** | Low ambient noise, well-lit, comfortable seating (no high stools), accessible entrance (no steep stairs). | Easy walking distance from drop-off points or parking. | `"quiet," "wheelchair accessible," "comfortable," "excellent service," "easy access"` |
| **Art / History Lovers** | Historic architecture, rustic taverns, quiet bistros, unique lighting, cultural decor. | Located in historic centers or old town quarters. | `"historic," "charming," "traditional," "artistic," "local character," "intimate"` |
| **Outdoor Adventurers** | Hearty portions, casual dress code, late hours, counter or fast service. | Directly on the route or at the trailhead parking lot. | `"hearty," "filling," "casual," "quick," "outdoor seating," "hikers"` |
| **Luxury / Foodies** | Tasting menus, local culinary heritage focus, professional service, fine wines. | Scenic viewpoints or historic estates. | `"tasting menu," "wine pairing," "michelin," "gourmet," "locally sourced"` |

---

## 4. Dining Recommendations Formatting Standard

Always present restaurant recommendations in this structured format:

```markdown
### 🍽️ [Restaurant Name]
- **Sourced Rating**: [e.g., 4.7/5 stars on Google Reviews (based on 340 reviews)]
- **Price Point**: [$, $$, $$$, or $$$$]
- **Primary Cuisine**: [e.g., Traditional Tuscan / Vegan Bistro]
- **Dietary Safety**: [e.g., 100% Certified Gluten-Free / Dedicated Vegan Menu]
- **Atmosphere & Suitability**: [e.g., Quiet, stroller-friendly, low ambient noise]
- **Live Sourced Review ([Source], [Month Year])**: *"Copy exact quote verifying the dietary safety or suitability. E.g., 'The gluten-free pizza base was made in a separate oven. Safe for my celiac son!'"*
- **Location/Address**: [Full physical address or proximity to main site]
```
