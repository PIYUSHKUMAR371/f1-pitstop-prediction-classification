# ============================================================
# IMPORTING LIBRARIES
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# ============================================================
# LOADING TRAINED MODEL
# ============================================================

model = joblib.load("xgboost_pitstop_model.pkl")

# Load encoders
label_encoders = joblib.load("label_encoders.pkl")

# ============================================================
# CREATING FASTAPI APP
# ============================================================

app = FastAPI(
    title="F1 Pit Stop Prediction API",
    description="Predicts whether a Formula 1 car will pit on the next lap",
    version="1.0"
)

# ============================================================
# INPUT DATA MODEL
# ============================================================

class PitStopInput(BaseModel):

    Driver: str
    Compound: str
    Race: str
    Year: int
    PitStop: int
    LapNumber: int
    Stint: int
    TyreLife: int
    Position: int
    LapTime_s: float
    LapTime_Delta: float
    Cumulative_Degradation: float
    RaceProgress: float
    Position_Change: int

# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def home():

    return {
        "message": "F1 Pit Stop Prediction API is Running"
    }

# ============================================================
# PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict(data: PitStopInput):

    # Convert input to DataFrame
    input_data = pd.DataFrame([{
        "Driver": data.Driver,
        "Compound": data.Compound,
        "Race": data.Race,
        "Year": data.Year,
        "PitStop": data.PitStop,
        "LapNumber": data.LapNumber,
        "Stint": data.Stint,
        "TyreLife": data.TyreLife,
        "Position": data.Position,
        "LapTime (s)": data.LapTime_s,
        "LapTime_Delta": data.LapTime_Delta,
        "Cumulative_Degradation": data.Cumulative_Degradation,
        "RaceProgress": data.RaceProgress,
        "Position_Change": data.Position_Change
    }])

    # ========================================================
    # APPLY LABEL ENCODING
    # ========================================================

    categorical_cols = [
        "Driver",
        "Compound",
        "Race"
    ]

    for col in categorical_cols:

        encoder = label_encoders[col]

        input_data[col] = encoder.transform(
            input_data[col]
        )

    # ========================================================
    # MODEL PREDICTION
    # ========================================================

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(
        input_data
    )[0][1]

    return {
        "PitNextLapPrediction": int(prediction),
        "Probability": float(probability)
    }