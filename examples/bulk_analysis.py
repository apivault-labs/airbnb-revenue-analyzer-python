from airbnb_revenue_analyzer import AirbnbRevenueAnalyzerClient

client = AirbnbRevenueAnalyzerClient()
payload = {'mode': 'market', 'searchLocation': 'Austin, Texas', 'maxComparableListings': 10}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
