import json
from airbnb_revenue_analyzer import AirbnbRevenueAnalyzerClient

rows = AirbnbRevenueAnalyzerClient().run({'mode': 'market', 'searchLocation': 'Austin, Texas', 'maxComparableListings': 10})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
