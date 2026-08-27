import csv
from airbnb_revenue_analyzer import AirbnbRevenueAnalyzerClient

rows = AirbnbRevenueAnalyzerClient().run({'mode': 'market', 'searchLocation': 'Austin, Texas', 'maxComparableListings': 10})
if rows:
    scalar_keys = [k for k, v in rows[0].items() if not isinstance(v, (dict, list))]
    with open("results.csv", "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=scalar_keys)
        writer.writeheader()
        writer.writerows({k: row.get(k) for k in scalar_keys} for row in rows)
