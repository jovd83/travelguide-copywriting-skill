#!/usr/bin/env python3
"""
Geocode & Trail Miner Script
Sourced for the travelguide-copywriting-skill agent skill.
Performs dependency-free geocoding and nearby landmark/trail queries using standard libraries.
"""

import argparse
import json
import ssl
import sys
import urllib.parse
import urllib.request

USER_AGENT = "TravelguideCopywriterAgentSkill/1.0 (contact: support@agentskills.io)"

def fetch_url(url, data=None):
    """Fetches raw data from a URL with a standard User-Agent header."""
    req = urllib.request.Request(url, data=data)
    req.add_header("User-Agent", USER_AGENT)

    # Verify TLS certificates. Nominatim and Overpass both serve valid certs, so there is
    # no reason to disable verification — doing so would expose these requests to
    # man-in-the-middle tampering of the geocoding/landmark data the guide is built on.
    ctx = ssl.create_default_context()

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        raise RuntimeError(f"HTTP request failed: {e}")

def reverse_geocode(lat, lon):
    """Queries Nominatim to resolve coordinates into administrative details."""
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
    raw_response = fetch_url(url)
    return json.loads(raw_response)

def query_overpass_nearby(lat, lon, radius=500):
    """Queries OSM Overpass API to find named trails, parks, and historic spots within radius."""
    overpass_url = "https://overpass-api.de/api/interpreter"
    
    # Overpass QL query to find historic sites, parks, and paths
    query = f"""[out:json][timeout:15];
(
  node["highway"~"path|footway|cycleway"](around:{radius}, {lat}, {lon});
  way["highway"~"path|footway|cycleway"](around:{radius}, {lat}, {lon});
  node["leisure"="park"](around:{radius}, {lat}, {lon});
  way["leisure"="park"](around:{radius}, {lat}, {lon});
  node["historic"](around:{radius}, {lat}, {lon});
  way["historic"](around:{radius}, {lat}, {lon});
);
out tags center 30;"""
    
    encoded_data = urllib.parse.urlencode({"data": query}).encode("utf-8")
    try:
        raw_response = fetch_url(overpass_url, data=encoded_data)
        data = json.loads(raw_response)
        elements = data.get("elements", [])
        
        trails = []
        historic = []
        parks = []
        
        for elem in elements:
            tags = elem.get("tags", {})
            name = tags.get("name")
            if not name:
                continue
                
            center = elem.get("center", {})
            lat_pt = center.get("lat") or elem.get("lat")
            lon_pt = center.get("lon") or elem.get("lon")
            
            item = {
                "name": name,
                "type": elem.get("type"),
                "lat": lat_pt,
                "lon": lon_pt,
                "highway": tags.get("highway"),
                "historic": tags.get("historic"),
                "leisure": tags.get("leisure")
            }
            
            if tags.get("highway"):
                trails.append(item)
            elif tags.get("historic"):
                item["description"] = tags.get("description")
                historic.append(item)
            elif tags.get("leisure") == "park":
                parks.append(item)
                
        return {
            "trails": trails[:8],      # Limit to top 8
            "historic": historic[:8],  # Limit to top 8
            "parks": parks[:5]         # Limit to top 5
        }
    except Exception as e:
        # Fallback gracefully if Overpass is down
        return {
            "error": f"Overpass query failed: {e}",
            "trails": [],
            "historic": [],
            "parks": []
        }

def main():
    parser = argparse.ArgumentParser(description="Reverse geocodes coordinates and mines nearby OSM data.")
    parser.add_argument("--lat", required=True, type=float, help="Latitude coordinate")
    parser.add_argument("--lon", required=True, type=float, help="Longitude coordinate")
    
    args = parser.parse_args()
    
    result = {
        "status": "success",
        "coordinates": {"latitude": args.lat, "longitude": args.lon},
        "address": None,
        "nearby": None
    }
    
    try:
        # Step 1: Reverse Geocode
        address_info = reverse_geocode(args.lat, args.lon)
        result["address"] = {
            "display_name": address_info.get("display_name"),
            "details": address_info.get("address", {})
        }
    except Exception as e:
        result["status"] = "partial_success"
        result["error"] = f"Geocoding failed: {e}"
        
    # Step 2: Query nearby highlights (always attempt even if geocoding failed)
    nearby_data = query_overpass_nearby(args.lat, args.lon)
    result["nearby"] = nearby_data
    
    # Step 3: Print result as a clean JSON
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
