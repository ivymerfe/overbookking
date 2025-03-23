import random

genders = ["мужчина", "женщина"]
age_diapason = (14, 110)

cities = ['Москва', 'Санкт-Петербург', 'Казань', 'Екатеринбург', 'Новосибирск',
          'Нижний Новгород', 'Сочи', 'Ростов-на-Дону', 'Самара', 'Краснодар',
          'Уфа', 'Тюмень', 'Хабаровск', 'Пермь', 'Омск', 'Челябинск',
          'Волгоград', 'Иркутск', 'Барнаул', 'Ставрополь', 'Брянск',
          'Астрахань', 'Воронеж', 'Сургут', 'Красноярск', 'Магадан',
          'Норильск', 'Петропавловск-Камчатский', 'Грозный', 'Владикавказ',
          'Мирный', 'Салехард', 'Улан-Удэ', 'Якутск', 'Надым',
          'Новый Уренгой', 'Абакан']

from_cities_probability = {
    "Москва": 0.05,
    "Санкт-Петербург": 0.05,
    "Казань": 0.03,
    "Екатеринбург": 0.03,
    "Новосибирск": 0.05,
    "Нижний Новгород": 0.03,
    "Сочи": 0.05,
    "Ростов-на-Дону": 0.05,
    "Самара": 0.04,
    "Краснодар": 0.05,
    "Уфа": 0.04,
    "Тюмень": 0.03,
    "Хабаровск": 0.05,
    "Пермь": 0.06,
    "Омск": 0.06,
    "Челябинск": 0.06,
    "Волгоград": 0.06,
    "Иркутск": 0.06,
    "Барнаул": 0.06,
    "Ставрополь": 0.06,
    "Брянск": 0.06,
    "Астрахань": 0.06,
    "Воронеж": 0.06,
    "Сургут": 0.06,
    "Красноярск": 0.06,
    "Магадан": 0.08,
    "Норильск": 0.1,
    "Петропавловск-Камчатский": 0.1,
    "Грозный": 0.08,
    "Владикавказ": 0.08,
    "Мирный": 0.1,
    "Салехард": 0.08,
    "Улан-Удэ": 0.08,
    "Якутск": 0.1,
    "Надым": 0.1,
    "Новый Уренгой": 0.08,
    "Абакан": 0.08
}
to_cities_probability = {
    "Сочи": 0.1,
    "Надым": 0.0,
    "Волгоград": 0.03,
    "Ставрополь": 0.02,
    "Санкт-Петербург": 0.08,
    "Симферополь": 0.1,
    "Геленджик": 0.08,
    "Калининград": 0.07,
    "Минеральные Воды": 0.07,
    "Анапа": 0.08,
    "Москва": 0.05,
    "Новосибирск": 0.05,
    "Казань": 0.05,
    "Екатеринбург": 0.05,
    "Краснодар": 0.05,
    "Ростов-на-Дону": 0.05,
    "Самара": 0.05,
    "Уфа": 0.05,
    "Тюмень": 0.05,
    "Норильск": -0.05,
    "Сургут": -0.05,
    "Магадан": -0.05,
    "Якутск": -0.05,
    "Воронеж": -0.03,
    "Омск": -0.03,
    "Пермь": -0.03,
    "Челябинск": -0.03,
    "Барнаул": -0.03,
    "Иркутск": -0.03,
    "Нижний Новгород": 0.02,
    "Хабаровск": 0.02,
    "Брянск": 0.0,
    "Астрахань": 0.01,
    "Красноярск": 0.01,
    "Мирный": -0.01,
    "Салехард": -0.01,
    "Улан-Удэ": 0.0,
    "Новый Уренгой": 0.0,
    "Абакан": 0.0,
    "Грозный": 0.0,
    "Владикавказ": 0.0,
    "Петропавловск-Камчатский": -0.01
}

flight_classes = ["Эконом", "Бизнес", "Первый"]
ticket_costs_diapason = (1000, 30000)

is_ticket_returning = [True, False]
passenger_types = ["Турист", "Бизнесman"]

flight_frequency_diapason = (0, 10)
baggage_availability = [True, False]

ticket_buying_types = ["Онлайн", "В аэропорту", "Турагенство"]
reservation_group = ["В одиночку", "С семьёй", "В группе"]

time_before_buying_diapason = (1, 100)
flight_time_diapason = (0, 24)

destination_weathers = ["Снегопад/ливень", "Дождь", "Ясно"]
transfer_availability = [True, False]

time_while_transfer = [True, False]
week_day_diapason = (1, 7)

is_public_holiday = [True, False]
passenger_social_status = ["Студент", "Работающий", "Пенсионер"]


def passenger_generator(amount: int) -> dict:
    result = {}
    for passenger_count in range(amount):
        passenger = {}
        stats = 0

        passenger["Пол"] = random.choice(genders)
        stats += 0.05

        passenger["Возраст"] = random.randint(*age_diapason)
        if passenger["Возраст"] <= 25:
            stats += 0.2
        elif passenger["Возраст"] <= 40:
            stats += 0.05
        elif passenger["Возраст"] <= 60:
            pass
        else:
            stats += -0.1

        passenger["Место отправления"] = random.choice(cities)
        stats += from_cities_probability[passenger["Место отправления"]]

        cities_upd = cities
        cities_upd.remove(passenger["Место отправления"])

        passenger["Место назначения"] = random.choice(cities_upd)
        stats += to_cities_probability[passenger["Место назначения"]]

        passenger["Класс полёта"] = random.choice(flight_classes)
        if passenger["Класс полёта"] == "Эконом":
            stats += 0.1
        elif passenger["Класс полёта"] == "Бизнес":
            pass
        else:
            stats += -0.1

        passenger["Цена билета"] = random.randint(*ticket_costs_diapason)
        if passenger["Цена билета"] <= 4000:
            stats += 0.15
        elif passenger["Цена билета"] <= 18000:
            stats += 0.05
        else:
            stats += -0.05

        passenger["Билет возвратный?"] = random.choice(is_ticket_returning)
        if passenger["Билет возвратный?"]:
            passenger["Билет возвратный?"] = "Да"
            stats += 0.1
        else:
            passenger["Билет возвратный?"] = "Нет"
            stats += -0.05

        passenger["Тип пассажира"] = random.choice(passenger_types)
        if passenger["Тип пассажира"] == "Турист":
            stats += 0.1
        else:
            stats += -0.05

        passenger["Частота полётов пассажира"] = random.randint(*flight_frequency_diapason)
        if passenger["Частота полётов пассажира"] == 0:
            stats += 0.1
        elif passenger["Частота полётов пассажира"] <= 3:
            stats += 0.05
        elif passenger["Частота полётов пассажира"] <= 7:
            pass
        else:
            stats += -0.05

        passenger["Наличие багажа"] = random.choice(baggage_availability)
        if not passenger["Наличие багажа"]:
            passenger["Наличие багажа"] = "Нет"
            stats += 0.1
        else:
            passenger["Наличие багажа"] = "Да"
            stats += -0.05

        passenger["Способ покупки билета"] = random.choice(ticket_buying_types)
        if passenger["Способ покупки билета"] == "Онлайн":
            stats += 0.05
        elif passenger["Способ покупки билета"] == "В аэропорту":
            stats += 0.1
        else:
            stats += -0.05

        passenger["Группа бронирования"] = random.choice(reservation_group)
        if passenger["Группа бронирования"] == "В одиночку":
            stats += 0.1
        elif passenger["Группа бронирования"] == "С семьёй":
            stats += 0.05
        else:
            stats += -0.05

        passenger["За сколько дней до вылета был куплен"] = random.randint(*time_before_buying_diapason)
        if passenger["За сколько дней до вылета был куплен"] <= 5:
            pass
        elif passenger["За сколько дней до вылета был куплен"] <= 14:
            stats += 0.05
        elif passenger["За сколько дней до вылета был куплен"] <= 30:
            stats += 0.1
        else:
            stats += 0.15

        passenger["Время полёта"] = random.randint(*flight_time_diapason)
        if passenger["Время полёта"] <= 6:
            stats += 0.1
        elif passenger["Время полёта"] <= 12:
            stats += 0.05
        elif passenger["Время полёта"] <= 18:
            pass
        else:
            stats += -0.05

        passenger["Погода в пункте назначения"] = random.choice(destination_weathers)
        if passenger["Погода в пункте назначения"] == "Снегопад/ливень":
            stats += 0.15
        elif passenger["Погода в пункте назначения"] == "Дождь":
            stats += 0.05
        else:
            stats += -0.05

        passenger["Есть пересадка?"] = random.choice(transfer_availability)
        if passenger["Есть пересадка?"]:
            passenger["Есть пересадка?"] = "Да"
            stats += 0.1

            passenger["Есть задержка между рейсами?"] = random.choice(time_while_transfer)
            if passenger["Есть задержка между рейсами?"]:
                passenger["Есть задержка между рейсами?"] = "Да"
                stats += 0.1
            else:
                passenger["Есть задержка между рейсами?"] = "Нет"
        else:
            passenger["Есть пересадка?"] = "Нет"

        passenger["День недели"] = random.randint(*week_day_diapason)
        if passenger["День недели"] == 5:
            stats += 0.05
        elif passenger["День недели"] >= 6:
            stats += 0.1

        passenger["Вылет в календарный праздник?"] = random.choice(is_public_holiday)
        if passenger["Вылет в календарный праздник?"]:
            passenger["Вылет в календарный праздник?"] = "Да"
            stats += 0.1
        else:
            passenger["Вылет в календарный праздник?"] = "Нет"

        passenger["Социальный статус пассажира"] = random.choice(passenger_social_status)
        if passenger["Социальный статус пассажира"] == "Студент":
            stats += 0.1
        elif passenger["Социальный статус пассажира"] == "Работающий":
            pass
        else:
            stats += -0.05

        final_stats = random.uniform(0,1) < 0.05 * (stats + 1)
        if final_stats:
            passenger["Будет лететь?"] = "Да"
        else:
            passenger["Будет лететь?"] = "Нет"

        passenger_desc = "\n".join(f"{k}: {v}" for k, v in passenger.items())
        result[passenger_count] = passenger_desc

    return result


test = passenger_generator(5)
for tst in test.values():
    print(tst, "\n")


