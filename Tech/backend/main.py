from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import FlightData, PredictionFeed, PredictionQuery

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/")
async def predict(query: PredictionQuery):
    
    return {"chance": 0}
