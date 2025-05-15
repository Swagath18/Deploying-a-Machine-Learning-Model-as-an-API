from pydantic import BaseModel
from typing import Literal

class ClaimInput(BaseModel):
    age: float
    gender: Literal[0, 1]
    claim_amount: float
    claim_dayofweek: int
    claim_month: int
    diag_A10: int
    diag_B20: int
    diag_C30: int
    diag_D40: int
    diag_E50: int
    age_young: int
    age_adult: int
    age_middle_aged: int
    age_senior: int

