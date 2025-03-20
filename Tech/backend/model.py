from pydantic import BaseModel
from typing import List


class FlightData(BaseModel):
    flightClass: int
    ticketCost: float
    timeFromLastFlight: int
    environmentScore: int
    missed: bool

class PredictionFeed(BaseModel):
    flightClass: int
    ticketCost: float
    timeFromLastFlight: int
    environmentScore: int

class PredictionQuery(BaseModel):
    flightsHistory: List[FlightData]
    feed: PredictionFeed
