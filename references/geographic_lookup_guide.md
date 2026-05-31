# Geographic Lookup & Trail Mining Reference Guide

Use this guide to govern the resolution of coordinates or place names into rich spatial context and to extract real, safe, and age-appropriate hiking and walking itineraries.

---

## 1. Coordinate Resolution & Geocoding Protocol

When given coordinate pairs (e.g., `45.8327, 6.8651`), execute the following resolution layers to prevent geographic hallucination.

```
[Raw Coordinates]
       │
       ▼
[Layer 1: Deterministic Script] ──► Runs ./scripts/geocode_and_trail_miner.py
       │                            Queries Nominatim API
       ▼ (If network fails)
[Layer 2: Search Verification]  ──► Search: "45.8327, 6.8651 address city"
       │                            Extracts exact administrative borders
       ▼
[Layer 3: Regional Profiling]   ──► Search: "[Resolved Town] history landmarks"
```

### Fallback Search Suffixes for Reverse Geocoding
If the geocoding script fails to resolve details, run a live search with these specific patterns:
- `"[latitude], [longitude] location address"`
- `"[latitude], [longitude] nearest town city country"`

---

## 2. Trail Mining & Verification Sourcing

Do not rely on parametric memory to construct hiking paths. Every walk or hike must represent an actual, physically verifiable route.

### Live Search String Patterns for Trails
1. **Nature Hikes**:
   ```
   site:alltrails.com OR site:komoot.com OR site:hikingproject.com "[resolved place name]" trail hike
   ```
2. **City Walking Tours**:
   ```
   "walking tour itinerary" OR "historic walk" in "[resolved place name]" route waypoints
   ```
3. **National Park/Official Trails**:
   ```
   site:.gov OR site:.org "[resolved place name]" hiking trails map status
   ```

### Critical Trail Attributes to Extract:
- **Trailhead Coordinates**: Exact starting point.
- **Distance**: Precise length in kilometers or miles (out-and-back, point-to-point, or loop).
- **Elevation Change**: Cumulative elevation gain/loss in meters or feet.
- **Difficulty Rating**: Easy, Moderate, Strenuous, or Technical.
- **Terrain Type**: Paved, hard-packed gravel, single-track dirt, rocky scramble, muddy bog.

---

## 3. Demographically Adapted Trail Metrics

Hike selection must match the physical capabilities of the traveler ages. Refer to the table below before recommending any path:

| Traveler Age Group | Max Distance | Max Elevation Gain | Allowed Terrain Types | Safety Exclusions |
|---|---|---|---|---|
| **Toddlers (Under 5)** | < 2 km | < 20 m | Paved concrete, boardwalks, packed flat gravel. | No cliff drop-offs, no water crossings, must have barrier railings. Proximity to toilets (< 1km). |
| **Seniors (65+)** | < 4 km | < 80 m | Flat, firm surfaces, wide double-track dirt. | No steep stairs, no loose scree, slope grades strictly under 8%. Must include resting benches. |
| **Active Adults / Teens** | No limit | No limit | Single-track, steep scree, talus, bogs, scrambling. | No exclusions, except general weather/local avalanche or rockfall warnings. |

---

## 4. Trail Formatting Standard

When presenting a hiking or walking itinerary, always structure it in the following uniform format to maintain professional roadbook standards:

```markdown
### 🥾 Route Name: [Descriptive Title]
- **Route Type**: [Loop / Out-and-back / Point-to-point]
- **Distance**: [X.X] km / miles
- **Elevation Gain**: [+/- X] meters / feet
- **Difficulty**: [Very Easy / Easy / Moderate / Strenuous]
- **Estimated Duration**: [X hours Y minutes]
- **Trailhead Location**: [Coordinates or Address description]
- **Terrain**: [e.g., Hard-packed dirt, sandstone blocks]

#### Waypoints & Key Highlights
1. **[Waypoint 1] (0.0 km)**: Describe the start, parking, and initial direction.
2. **[Waypoint 2] (X.X km)**: Highlight a view, junction, or physical sensation.
3. **[Waypoint 3] (X.X km)**: Turn-around point, summit, or unique flora/fauna.
4. **[Waypoint 4] (X.X km)**: Concluding instructions.
```
