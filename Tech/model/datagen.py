import random
import pandas as pd

genders = ["Male", "Female"]
age_diapason = (16, 80)

cities = [
    "Moscow",
    "Saint Petersburg",
    "Kazan",
    "Yekaterinburg",
    "Novosibirsk",
    "Nizhny Novgorod",
    "Sochi",
    "Rostov-on-Don",
    "Samara",
    "Krasnodar",
    "Ufa",
    "Tyumen",
    "Khabarovsk",
    "Perm",
    "Omsk",
    "Chelyabinsk",
    "Volgograd",
    "Irkutsk",
    "Barnaul",
    "Stavropol",
    "Bryansk",
    "Astrakhan",
    "Voronezh",
    "Surgut",
    "Krasnoyarsk",
    "Magadan",
    "Norilsk",
    "Petropavlovsk-Kamchatsky",
    "Grozny",
    "Vladikavkaz",
    "Mirny",
    "Salekhard",
    "Ulan-Ude",
    "Yakutsk",
    "Nadym",
    "Novy Urengoy",
    "Abakan",
]

from_cities_probability = {
    "Moscow": 0.05,
    "Saint Petersburg": 0.05,
    "Kazan": 0.03,
    "Yekaterinburg": 0.03,
    "Novosibirsk": 0.05,
    "Nizhny Novgorod": 0.03,
    "Sochi": 0.05,
    "Rostov-on-Don": 0.05,
    "Samara": 0.04,
    "Krasnodar": 0.05,
    "Ufa": 0.04,
    "Tyumen": 0.03,
    "Khabarovsk": 0.05,
    "Perm": 0.06,
    "Omsk": 0.06,
    "Chelyabinsk": 0.06,
    "Volgograd": 0.06,
    "Irkutsk": 0.06,
    "Barnaul": 0.06,
    "Stavropol": 0.06,
    "Bryansk": 0.06,
    "Astrakhan": 0.06,
    "Voronezh": 0.06,
    "Surgut": 0.06,
    "Krasnoyarsk": 0.06,
    "Magadan": 0.08,
    "Norilsk": 0.1,
    "Petropavlovsk-Kamchatsky": 0.1,
    "Grozny": 0.08,
    "Vladikavkaz": 0.08,
    "Mirny": 0.1,
    "Salekhard": 0.08,
    "Ulan-Ude": 0.08,
    "Yakutsk": 0.1,
    "Nadym": 0.1,
    "Novy Urengoy": 0.08,
    "Abakan": 0.08,
}
to_cities_probability = {
    "Sochi": 0.1,
    "Nadym": 0.0,
    "Volgograd": 0.03,
    "Stavropol": 0.02,
    "Saint Petersburg": 0.08,
    "Simferopol": 0.1,
    "Gelendzhik": 0.08,
    "Kaliningrad": 0.07,
    "Mineralnye Vody": 0.07,
    "Anapa": 0.08,
    "Moscow": 0.05,
    "Novosibirsk": 0.05,
    "Kazan": 0.05,
    "Yekaterinburg": 0.05,
    "Krasnodar": 0.05,
    "Rostov-on-Don": 0.05,
    "Samara": 0.05,
    "Ufa": 0.05,
    "Tyumen": 0.05,
    "Norilsk": -0.05,
    "Surgut": -0.05,
    "Magadan": -0.05,
    "Yakutsk": -0.05,
    "Voronezh": -0.03,
    "Omsk": -0.03,
    "Perm": -0.03,
    "Chelyabinsk": -0.03,
    "Barnaul": -0.03,
    "Irkutsk": -0.03,
    "Nizhny Novgorod": 0.02,
    "Khabarovsk": 0.02,
    "Bryansk": 0.0,
    "Astrakhan": 0.01,
    "Krasnoyarsk": 0.01,
    "Mirny": -0.01,
    "Salekhard": -0.01,
    "Ulan-Ude": 0.0,
    "Novy Urengoy": 0.0,
    "Abakan": 0.0,
    "Grozny": 0.0,
    "Vladikavkaz": 0.0,
    "Petropavlovsk-Kamchatsky": -0.01,
}

flight_classes = ["Economy", "Business", "First"]
ticket_costs_diapason = (10000, 80000)

is_ticket_returning = [True, False]
passenger_types = ["Regular", "Business"]

flight_frequency_diapason = (0, 10)
baggage_availability = [True, False]

ticket_buying_types = ["Online", "At the airport", "Travel agency"]
reservation_group = ["Alone", "With family", "In a group"]

time_before_buying_diapason = (1, 100)
flight_time_diapason = (0, 24)

source_weathers = ["Snowfall", "Rain", "Clear"]
transfer_availability = [True, False]

time_while_transfer = [True, False]
week_day_diapason = (1, 7)
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

is_public_holiday = [True, False]
passenger_social_status = ["Student", "Working", "Retired"]


def passenger_generator():
    passenger = {}
    stats = 0

    passenger["Gender"] = random.choice(genders)
    stats += 0.05

    passenger["Age"] = random.randint(*age_diapason)
    if passenger["Age"] <= 25:
        stats += 0.2
    elif passenger["Age"] <= 40:
        stats += 0.05
    elif passenger["Age"] <= 60:
        pass
    else:
        stats += -0.1

    passenger["Departure City"] = random.choice(cities)
    stats += from_cities_probability[passenger["Departure City"]]

    cities_upd = cities.copy()
    cities_upd.remove(passenger["Departure City"])

    passenger["Destination City"] = random.choice(cities_upd)
    stats += to_cities_probability[passenger["Destination City"]]

    passenger["Class"] = random.choice(flight_classes)
    if passenger["Class"] == "Economy":
        stats += 0.1
    elif passenger["Class"] == "Business":
        pass
    else:
        stats += -0.1

    passenger["Price"] = random.randint(*ticket_costs_diapason)
    if passenger["Price"] <= 4000:
        stats += 0.15
    elif passenger["Price"] <= 18000:
        stats += 0.05
    else:
        stats += -0.05

    passenger["Refundable"] = random.choice(is_ticket_returning)
    if passenger["Refundable"]:
        passenger["Refundable"] = "Yes"
        stats += 0.1
    else:
        passenger["Refundable"] = "No"
        stats += -0.05

    passenger["Passenger Type"] = random.choice(passenger_types)
    if passenger["Passenger Type"] == "Regular":
        stats += 0.1
    else:
        stats += -0.05

    passenger["Flight Frequency"] = random.randint(*flight_frequency_diapason)
    if passenger["Flight Frequency"] == 0:
        stats += 0.1
    elif passenger["Flight Frequency"] <= 3:
        stats += 0.05
    elif passenger["Flight Frequency"] <= 7:
        pass
    else:
        stats += -0.05

    passenger["Baggage Availability"] = random.choice(baggage_availability)
    if not passenger["Baggage Availability"]:
        passenger["Baggage Availability"] = "No"
        stats += 0.1
    else:
        passenger["Baggage Availability"] = "Yes"
        stats += -0.05

    passenger["Purchase Method"] = random.choice(ticket_buying_types)
    if passenger["Purchase Method"] == "Online":
        stats += 0.05
    elif passenger["Purchase Method"] == "At the airport":
        stats += 0.1
    else:
        stats += -0.05

    passenger["Booking Group"] = random.choice(reservation_group)
    if passenger["Booking Group"] == "Alone":
        stats += 0.1
    elif passenger["Booking Group"] == "With family":
        stats += 0.05
    else:
        stats += -0.05

    passenger["Time Before Flight"] = random.randint(
        *time_before_buying_diapason
    )
    if passenger["Time Before Flight"] <= 5:
        pass
    elif passenger["Time Before Flight"] <= 14:
        stats += 0.05
    elif passenger["Time Before Flight"] <= 30:
        stats += 0.1
    else:
        stats += 0.15

    passenger["Flight Duration"] = random.randint(*flight_time_diapason)
    if passenger["Flight Duration"] <= 6:
        stats += 0.1
    elif passenger["Flight Duration"] <= 12:
        stats += 0.05
    elif passenger["Flight Duration"] <= 18:
        pass
    else:
        stats += -0.05

    passenger["Weather at Departure"] = random.choice(source_weathers)
    if passenger["Weather at Departure"] == "Snowfall":
        stats += 0.15
    elif passenger["Weather at Departure"] == "Rain":
        stats += 0.05
    else:
        stats += -0.05

    passenger["Transfer"] = random.choice(transfer_availability)
    if passenger["Transfer"]:
        passenger["Transfer"] = "Yes"
        stats += 0.1

        passenger["Delay Between Flights"] = random.choice(time_while_transfer)
        if passenger["Delay Between Flights"]:
            passenger["Delay Between Flights"] = "Yes"
            stats += 0.1
        else:
            passenger["Delay Between Flights"] = "No"
    else:
        passenger["Transfer"] = "No"

    passenger_weekday = random.randint(*week_day_diapason)
    if passenger_weekday == 5:
        stats += 0.05
    elif passenger_weekday >= 6:
        stats += 0.1

    passenger["Day of the Week"] = weekdays[passenger_weekday - 1]

    passenger["Public Holiday"] = random.choice(is_public_holiday)
    if passenger["Public Holiday"]:
        passenger["Public Holiday"] = "Yes"
        stats += 0.1
    else:
        passenger["Public Holiday"] = "No"

    passenger["Social Status"] = random.choice(passenger_social_status)
    if passenger["Social Status"] == "Student":
        stats += 0.1
    elif passenger["Social Status"] == "Working":
        pass
    else:
        stats += -0.05

    final = stats > 0.7
    passenger_desc = "\n".join(f"{k}: {v}" for k, v in passenger.items())
    return passenger_desc, final


if __name__ == "__main__":
    data = []
    for _ in range(10000):
      passenger_desc, final = passenger_generator()
      data.append({"desc": passenger_desc, "result": final})

    df = pd.DataFrame(data)
    df.to_csv("passengers.csv", index=False)
