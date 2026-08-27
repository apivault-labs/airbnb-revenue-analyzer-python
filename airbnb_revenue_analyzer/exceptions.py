"""Public exception hierarchy for the Airbnb Revenue, Occupancy & ROI Analyzer SDK."""

class AirbnbRevenueAnalyzerError(Exception):
    """Base SDK error."""

class AuthenticationError(AirbnbRevenueAnalyzerError):
    """The Apify token is missing or rejected."""

class ActorRunError(AirbnbRevenueAnalyzerError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(AirbnbRevenueAnalyzerError):
    """The client stopped waiting before the Actor completed."""
