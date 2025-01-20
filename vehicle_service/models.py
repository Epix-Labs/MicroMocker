from pydantic import BaseModel, condecimal
from typing import List, Optional
from enum import Enum
from uuid import UUID
from decimal import Decimal

class StatusEnum(str, Enum):
    available = "available"
    booked = "booked"
    in_maintenance = "in_maintenance"

class LicenseTypeEnum(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    BC = "BC"
    E = "E"

class VehicleRequirement(BaseModel):
    license_type: List[LicenseTypeEnum]
    experience: int  # in months

class PaymentTypeEnum(str, Enum):
    hour = "hour"
    day = "day"
    week = "week"
    month = "month"
    year = "year"
    milage = "milage"

class PaymentType(BaseModel):
    type: PaymentTypeEnum
    amount: condecimal(max_digits=12, decimal_places=2)

class Vehicle(BaseModel):
    is_booked: bool
    deposit: condecimal(max_digits=12, decimal_places=2)
    milage: condecimal(max_digits=12, decimal_places=2)
    status: StatusEnum
    visible: bool
    vehicle_requirements: List[VehicleRequirement]
    payment_types: List[PaymentType]
