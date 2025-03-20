import random
import numpy as np

MAX_FLIGHTS = 10
FLIGHT_DATA_SIZE = 4

# Econom = 0 Business = 1 First = 2

TICKET_COST_COEFF = [1,5, 20]

def random_flight_data():
  # Class, ticket cost, time from last flight, environment score
  flight_class = random.choices([0,1,2], [0.7, 0.2, 0.1])[0]
  ticket_cost = 20000 + random.randint(0, 10000*TICKET_COST_COEFF[flight_class])
  time_from_last_flight = random.randint(4, 160)
  environment_score = int(100*(1 - random.uniform(0.1, 1)**3))
  return [flight_class, ticket_cost, time_from_last_flight, environment_score]

# from 0 to 1 if user didnt miss the flight
def calc_impact_positive(flight_data) -> float:
  flight_class, ticket_cost, time_from_last_flight, environment_score = flight_data
  
  class_impact = [0.2, 0.5, 0.8][flight_class]
  cost_impact = (ticket_cost / 200000) ** (1/(3-flight_class))
  time_impact = 1
  env_impact = (1 - (environment_score/100))**2
  return (class_impact + cost_impact + time_impact + env_impact)/4

# from 0 to 1 if user missed the flight
def calc_impact_negative(flight_data) -> float:
  flight_class, ticket_cost, time_from_last_flight, environment_score = flight_data
  class_impact = [0.8, 0.4, 0.2][flight_class]
  cost_impact = (1 - ticket_cost / 200000) ** (1/(3-flight_class))
  time_impact = 0.5 if time_from_last_flight > 90 else 1
  env_impact = environment_score/100
  return (class_impact + cost_impact + time_impact + env_impact)/4

def calc_miss_chance(flight_data, user_score):
  flight_class, ticket_cost, time_from_last_flight, environment_score = flight_data
  miss_chance = 0.05 # 5%
  miss_chance *= [1.5, 1.3, 1.1][flight_class]
  miss_chance *= (1.4 - ticket_cost / 200000) ** (1/(3-flight_class))
  miss_chance *= 0.5 if time_from_last_flight > 100 else 0.8 if time_from_last_flight > 60 else 1
  miss_chance *= (1.5 - environment_score / 100)
  miss_chance *= (0.8**user_score)*5
  return miss_chance

def generate_user_flights(n: int):
  flights = []
  user_score = 5
  for _ in range(n):
    flight_data = random_flight_data()
    miss_chance = calc_miss_chance(flight_data, user_score)
    miss_chance *= random.uniform(0.8, 1.2)
    missed = random.uniform(0,1) < miss_chance
    expect = random.uniform(0.14, 0.18) if missed else random.uniform(0.03, 0.08)
    if missed:
      user_score -= calc_impact_negative(flight_data)
    else:
      user_score += calc_impact_positive(flight_data)
    flights.append(flight_data + [expect])
  
  flights_np = np.ndarray([(FLIGHT_DATA_SIZE+1)*(MAX_FLIGHTS)], np.float32)
  flights_np.fill(np.nan)
  for i, f in enumerate(flights):
    for j, d in enumerate(f):
      flights_np[i*(FLIGHT_DATA_SIZE+1)+j] = d
  next_flight = np.ndarray([FLIGHT_DATA_SIZE+1], np.float32)
  for i, f in enumerate(flights[-1]):
    next_flight[i] = f
  
  return np.concat([flights_np, next_flight])

def generate_dataset(n_samples: int):
  dataset = np.ndarray([n_samples, (FLIGHT_DATA_SIZE+1)*(MAX_FLIGHTS+1)], np.float32)
  for i in range(n_samples):
    dataset[i] = generate_user_flights(random.randint(1, MAX_FLIGHTS))
  return dataset
