from fastapi import FastAPI
from schemas.keystroke_schema import KeystrokeSequence
from models.user_models import train_hmm, authenticate
from database.db import save_data, load_user_data

app = FastAPI()
#   uvicorn main:app --reload --host 0.0.0.0 --port 8000
@app.post("/register")
def register(data: KeystrokeSequence):
    save_data(data.username, data.sequence)
    all_sequences = load_user_data(data.username)
    train_hmm(data.username, all_sequences)
    return {"message": f"Modèle HMM entraîné pour {data.username}"}

@app.post("/authenticate")
def auth(data: KeystrokeSequence):
    result = authenticate(data.username, data.sequence)
    return result
