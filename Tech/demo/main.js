let nextFlight = null;
let userFlightsData = [];
let flightCounter = 0;
const FLIGHT_CLASSES = ["Economy", "Business", "First"];

function randomize() {
  const nextFlightTable = document.getElementById("next_flight");
  const randomValue = Math.random();
  let flightClass;

  if (randomValue < 0.6) {
    flightClass = 0; // Economy (60% chance)
  } else if (randomValue < 0.9) {
    flightClass = 1; // Business (30% chance)
  } else {
    flightClass = 2; // First (10% chance)
  }

  const priceScale = [1, 5, 20];
  const ticketCost = 20000 + Math.floor(Math.random() * 10000 * priceScale[flightClass]);
  nextFlight = {
    flightClass: flightClass,
    ticketCost,
    timeFromLastFlight: 4 + Math.floor(Math.random() * 100),
    environmentScore: Math.floor(Math.random() * 100),
  };

  nextFlightTable.innerHTML = `
  <tr><th>Class</th><td>${FLIGHT_CLASSES[nextFlight.flightClass]}</td></tr>
  <tr><th>Ticket Cost</th><td>${nextFlight.ticketCost}</td></tr>
  <tr><th>Time From Last Flight</th><td>${nextFlight.timeFromLastFlight}</td></tr>
  <tr><th>Environment Score</th><td>${nextFlight.environmentScore}</td></tr>
  <tr><th>Prediction</th><td>?</td></tr>
`;
}

function removeFlight(flightNumber) {
  userFlightsData = userFlightsData.filter(
    (flight) => flight.flightNumber !== flightNumber
  );
  renderUserFlights();
}

function renderUserFlights() {
  const userFlightsTable = document.getElementById("user_flights");
  userFlightsTable.innerHTML = userFlightsData
    .map(
      (flight) => `
<tr>
  <td>${flight.flightNumber}</td>
  <td>${FLIGHT_CLASSES[flight.flightClass]}</td>
  <td>${flight.ticketCost}</td>
  <td>${flight.timeFromLastFlight}</td>
  <td>${flight.environmentScore}</td>
  <td>${flight.missed}</td>
  <td><button onclick="removeFlight(${flight.flightNumber})">X</button></td>
</tr>
`
    )
    .join("");
}

function addPassed() {
  if (!nextFlight) {
    alert("Please randomize the next flight first!");
    return;
  }

  const newFlight = {
    flightNumber: flightCounter,
    flightClass: nextFlight.flightClass,
    ticketCost: nextFlight.ticketCost,
    timeFromLastFlight: nextFlight.timeFromLastFlight,
    environmentScore: nextFlight.environmentScore,
    missed: 0,
  };

  userFlightsData.push(newFlight);
  flightCounter++;

  renderUserFlights();
}

function addMissed() {
  if (!nextFlight) {
    alert("Please randomize the next flight first!");
    return;
  }

  const newFlight = {
    flightNumber: flightCounter,
    flightClass: nextFlight.flightClass,
    ticketCost: nextFlight.ticketCost,
    timeFromLastFlight: nextFlight.timeFromLastFlight,
    environmentScore: nextFlight.environmentScore,
    missed: 1,
  };

  userFlightsData.push(newFlight);
  flightCounter++;

  renderUserFlights();
}

async function predict() {
  const body = JSON.stringify({
    flightsHistory: userFlightsData,
    feed: nextFlight,
  });

  try {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: body,
    });

    const prediction = await response.json();
    document.getElementById("next_flight").rows[4].cells[1].innerText =
      prediction.chance;
  } catch (error) {
    console.error("Error:", error);
  }
}
