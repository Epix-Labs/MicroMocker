from pydantic import BaseModel, condecimal
from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import date

class LicenseTypeEnum(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    BC = "BC"
    E = "E"

class LicensePlate(BaseModel):
    is_verifyed: bool
    issued_date: date
    expiry_date: date
    type: LicenseTypeEnum

class User(BaseModel):
    birth_of_date: date
    is_verifyed: bool
    balance: condecimal(max_digits=12, decimal_places=2)  # type: ignore # tiyinda hisoblanadi
    license_plate: LicensePlate
    