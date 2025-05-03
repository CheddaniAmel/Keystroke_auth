from pydantic import BaseModel
from typing import List

class KeystrokeSequence(BaseModel):
    username: str
    sequence: List[List[int]]  # [[dwell, flight], ...]
