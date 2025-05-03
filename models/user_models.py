from hmmlearn import hmm
import numpy as np
from typing import Dict

user_models: Dict[str, hmm.GaussianHMM] = {}

def train_hmm(username: str, sequence: list):
    X = np.array(sequence)
    model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=100)
    model.fit(X)
    user_models[username] = model
    return model

def authenticate(username: str, sequence: list):
    if username not in user_models:
        return {"authenticated": False, "score": -9999}
    model = user_models[username]
    X = np.array(sequence)
    score = model.score(X)
    
    # Change ici le seuil
    return {"authenticated": score > -80.0, "score": score}
