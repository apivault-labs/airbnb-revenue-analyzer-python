from airbnb_revenue_analyzer import AirbnbRevenueAnalyzerClient

client = AirbnbRevenueAnalyzerClient()
rows = client.run({'mode': 'market', 'searchLocation': 'Austin, Texas', 'maxComparableListings': 10})
print(rows[0] if rows else "No results")
