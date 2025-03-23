const genders = ["Male", "Female"];
const ageDiapason = [16, 80];

const cities = [
    "Moscow", "Saint Petersburg", "Kazan", "Yekaterinburg", "Novosibirsk",
    "Nizhny Novgorod", "Sochi", "Rostov-on-Don", "Samara", "Krasnodar",
    "Ufa", "Tyumen", "Khabarovsk", "Perm", "Omsk", "Chelyabinsk",
    "Volgograd", "Irkutsk", "Barnaul", "Stavropol", "Bryansk", "Astrakhan",
    "Voronezh", "Surgut", "Krasnoyarsk", "Magadan", "Norilsk",
    "Petropavlovsk-Kamchatsky", "Grozny", "Vladikavkaz", "Mirny",
    "Salekhard", "Ulan-Ude", "Yakutsk", "Nadym", "Novy Urengoy", "Abakan"
];

const flightClasses = ["Economy", "Business", "First"];
const ticketCostsDiapason = [10000, 80000];
const isTicketReturning = [true, false];
const passengerTypes = ["Regular", "Business"];
const flightFrequencyDiapason = [0, 10];
const baggageAvailability = [true, false];
const ticketBuyingTypes = ["Online", "At the airport", "Travel agency"];
const reservationGroup = ["Alone", "With family", "In a group"];
const timeBeforeBuyingDiapason = [1, 100];
const flightTimeDiapason = [0, 24];
const sourceWeathers = ["Snowfall", "Rain", "Clear"];
const transferAvailability = [true, false];
const timeWhileTransfer = [true, false];
const weekDayDiapason = [1, 7];
const weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
const isPublicHoliday = [true, false];
const passengerSocialStatus = ["Student", "Working", "Retired"];

function getRandomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function infoGenerator() {
    const passenger = {};

    passenger["Gender"] = getRandomElement(genders);
    passenger["Age"] = getRandomInt(...ageDiapason);
    passenger["Departure City"] = getRandomElement(cities);
    const citiesUpd = cities.filter(city => city !== passenger["Departure City"]);
    passenger["Destination City"] = getRandomElement(citiesUpd);
    passenger["Class"] = getRandomElement(flightClasses);
    passenger["Price"] = getRandomInt(...ticketCostsDiapason);
    passenger["Refundable"] = getRandomElement(isTicketReturning) ? "Yes" : "No";
    passenger["Passenger Type"] = getRandomElement(passengerTypes);
    passenger["Flight Frequency"] = getRandomInt(...flightFrequencyDiapason);
    passenger["Baggage Availability"] = getRandomElement(baggageAvailability) ? "Yes" : "No";
    passenger["Purchase Method"] = getRandomElement(ticketBuyingTypes);
    passenger["Booking Group"] = getRandomElement(reservationGroup);
    passenger["Time Before Flight"] = getRandomInt(...timeBeforeBuyingDiapason);
    passenger["Flight Duration"] = getRandomInt(...flightTimeDiapason);
    passenger["Weather at Departure"] = getRandomElement(sourceWeathers);
    passenger["Transfer"] = getRandomElement(transferAvailability) ? "Yes" : "No";
    if (passenger["Transfer"] === "Yes") {
        passenger["Delay Between Flights"] = getRandomElement(timeWhileTransfer) ? "Yes" : "No";
    }
    const passengerWeekday = getRandomInt(...weekDayDiapason);
    passenger["Day of the Week"] = weekdays[passengerWeekday - 1];
    passenger["Public Holiday"] = getRandomElement(isPublicHoliday) ? "Yes" : "No";
    passenger["Social Status"] = getRandomElement(passengerSocialStatus);

    const passengerDesc = Object.entries(passenger).map(([key, value]) => `${key}: ${value}`).join("\n");
    return passengerDesc
}


document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("predictBtn").addEventListener("click", async () => {
    const userInfo = document.getElementById("userInfo").value;

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userInfo }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data);
        document.getElementById("passChance").textContent = data.passChance;
        document.getElementById("missChance").textContent = data.missChance;
      } else {
        console.error("Error:", response.statusText);
      }
    } catch (error) {
      console.error("Fetch error:", error);
    }
  });

  document.getElementById("randomizeBtn").addEventListener("click", () => {
    document.getElementById("userInfo").value = infoGenerator();
  });
});
