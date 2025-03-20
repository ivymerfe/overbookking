from model import FlightData, PredictionFeed, PredictionQuery
import xgboost as xgb
import numpy as np

MAX_FLIGHTS = 10

class FlightMissPredictor:
  def __init__(self):
    self.model = xgb.XGBRegressor(n_estimators = 100, seed = 123)
    self.model.load_model("model.json")
  
  def predict(self, query: PredictionQuery) -> float:
    input_data = np.ndarray(shape=((MAX_FLIGHTS+1)*5 - 1), dtype=np.float32)
    input_data.fill(np.nan)
    for i, flight in enumerate(query.flightsHistory[-MAX_FLIGHTS:]):
      input_data[i*5] = flight.flightClass
      input_data[i*5+1] = flight.ticketCost
      input_data[i*5+2] = flight.timeFromLastFlight
      input_data[i*5+3] = flight.environmentScore
      input_data[i*5+4] = 0.3 if flight.missed else 0
    
    input_data[-4] = query.feed.flightClass
    input_data[-3] = query.feed.ticketCost
    input_data[-2] = query.feed.timeFromLastFlight
    input_data[-1] = query.feed.environmentScore
    
    pred = self.model.predict(input_data.reshape(1, -1))
    return pred.item()

