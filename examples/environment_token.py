import os
from airbnb_revenue_analyzer import AirbnbRevenueAnalyzerClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = AirbnbRevenueAnalyzerClient()
print(client.run_one({'mode': 'market', 'searchLocation': 'Austin, Texas', 'maxComparableListings': 10}))
