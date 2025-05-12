# models.py

from pydantic import BaseModel
from typing import Literal

class MBTIQuestion(BaseModel):
    id: int
    text: str
    dichotomy: Literal["E/I", "S/N", "T/F", "J/P"]
    polarity: Literal["E", "I", "S", "N", "T", "F", "J", "P"]
    weight: float = 1.0
