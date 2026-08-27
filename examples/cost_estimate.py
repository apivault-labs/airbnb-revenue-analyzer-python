from airbnb_revenue_analyzer import AirbnbRevenueAnalyzerClient

for count in (10, 100, 1000):
    print(count, AirbnbRevenueAnalyzerClient.estimate_cost(count), "USD estimated result charges")
