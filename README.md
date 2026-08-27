# Airbnb Revenue, Occupancy & ROI Analyzer — Python SDK

Python client for the [Airbnb Revenue, Occupancy & ROI Analyzer Apify Actor](https://apify.com/apivault_labs/airbnb-revenue-occupancy-roi-analyzer). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/airbnb-revenue-occupancy-roi-analyzer)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Weekly, monthly and annual revenue estimates
- ADR, occupancy, RevPAR and NOI
- Cap rate and cash-on-cash ROI
- Listing and market-comparable modes

The Actor uses public marketplace signals and returns estimates or ranges where a platform does not publish exact figures.

## Install

```bash
pip install git+https://github.com/apivault-labs/airbnb-revenue-analyzer-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from airbnb_revenue_analyzer import AirbnbRevenueAnalyzerClient

client = AirbnbRevenueAnalyzerClient(api_token="apify_api_xxxxxx")
rows = client.run({'mode': 'market', 'searchLocation': 'Austin, Texas', 'maxComparableListings': 10})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | `string` | `listing` | Analyze supplied listing URLs or discover and rank comparable listings for a location. |
| `listingUrls` | `array` | `—` | Public Airbnb room links or numeric listing IDs. One analysis row is returned per successful listing. |
| `searchLocation` | `string` | `` | City, neighborhood or destination used to discover public comparable listings in market mode. |
| `maxComparableListings` | `integer` | `10` | Number of discovered properties to analyze and rank in market mode. |
| `searchBedrooms` | `integer` | `0` | Optional minimum bedroom filter for market comparable discovery. Use 0 for any. |
| `searchGuests` | `integer` | `0` | Optional guest-count filter for market comparable discovery. Use 0 for Airbnb defaults. |
| `calendarMonths` | `integer` | `6` | Analyze 1–12 months of forward availability. Longer windows improve seasonality coverage. |
| `currency` | `string` | `USD` | Three-letter currency requested for published Airbnb prices and used for your financial assumptions. |
| `nightlyRateOverride` | `number` | `0` | Optional ADR assumption. Set 0 to use published forward calendar prices. |
| `bookingShareOfBlockedPercent` | `number` | `75` | Blocked nights may also be owner blocks or maintenance. This assumption converts the public blocked-night rate into estimated occupancy. |
| `averageStayNights` | `number` | `3` | Average booked nights per reservation, used for cleaning revenue and cost modeling. |
| `cleaningFeeRevenuePerStay` | `number` | `0` | Cleaning fee revenue collected from the guest for each estimated reservation. |
| `cleaningCostPerStay` | `number` | `0` | Your cleaning expense for each estimated reservation. |
| `platformFeePercent` | `number` | `3` | Estimated booking-platform fee as a percentage of gross revenue. |
| `managementFeePercent` | `number` | `15` | Property-management cost as a percentage of gross revenue. |
| `maintenancePercent` | `number` | `5` | Maintenance and replacement reserve as a percentage of gross revenue. |
| `utilitiesMonthly` | `number` | `300` | Average monthly utilities paid by the property owner. |
| `insuranceAnnual` | `number` | `1500` | Annual insurance cost for the property. |
| `propertyTaxAnnual` | `number` | `0` | Annual property-tax expense. |
| `hoaMonthly` | `number` | `0` | Monthly homeowners-association or building fee. |
| `mortgageMonthly` | `number` | `0` | Debt service is excluded from NOI and included in annual cash flow and cash-on-cash return. |
| `purchasePrice` | `number` | `0` | Required for cap rate and acquisition return metrics. Set 0 for operations-only analysis. |
| `downPaymentPercent` | `number` | `20` | Down payment as a percentage of purchase price, used to calculate cash invested. |
| `closingCosts` | `number` | `0` | One-time acquisition closing costs included in cash invested. |
| `furnishingCosts` | `number` | `0` | One-time furnishing and launch costs included in cash invested. |
| `emitProjectionRows` | `boolean` | `False` | Also emit each weekly and monthly projection as a separate uncharged Dataset row for CSV and spreadsheet workflows. |
| `previousSnapshots` | `array` | `[]` | Optional prior property metrics used to calculate occupancy, ADR and annual-revenue changes and monitoring alerts. |
| `maxConcurrency` | `integer` | `3` | Parallel property analyses. The default balances speed and upstream reliability. |
| `proxyConfiguration` | `object` | `{"useApifyProxy":true,"apifyProxyGroups":["RESIDENTIAL"],"co` | Residential proxy is recommended for public Airbnb availability. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/airbnb-revenue-occupancy-roi-analyzer).

## Pricing

Pay per delivered result through Apify, starting around **$5/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
