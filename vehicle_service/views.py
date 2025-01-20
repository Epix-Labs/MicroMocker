import json
from fastapi import FastAPI, HTTPException, Depends
from .models import Vehicle
from uuid import UUID
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Dict

vehicle_app = FastAPI()

security = HTTPBasic()

VEHICLE_DATA_URL = 'mock_data/vehicles_data.json'

# Load data from a local JSON file
def load_vehicle_data():
    with open(VEHICLE_DATA_URL, 'r') as file:
        return json.load(file)

# Save data to the JSON file
def save_vehicle_data(data: Dict[UUID, Vehicle]):
    with open(VEHICLE_DATA_URL, 'w') as file:
        json.dump(data, file, default=str)  # convert UUID and other complex types to string

# In-memory vehicle data loaded from a local file
vehicle_db = load_vehicle_data()

# Basic Auth credentials
VALID_USERNAME = "vehicle_service"
VALID_PASSWORD = "securepassword"

# Authentication function
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == VALID_USERNAME and credentials.password == VALID_PASSWORD:
        return credentials.username
    raise HTTPException(status_code=401, detail="Unauthorized")

@vehicle_app.get("/vehicle/{vehicle_id}", response_model=Vehicle)
def get_vehicle(vehicle_id: UUID, _: str = Depends(authenticate)):
    vehicle = vehicle_db.get(str(vehicle_id))  # JSON stores keys as strings
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@vehicle_app.put("/vehicle/{vehicle_id}")
def update_vehicle_put(vehicle_id: UUID, update_data: dict, _: str = Depends(authenticate)):
    # Update entire vehicle resource with the new data
    vehicle = vehicle_db.get(str(vehicle_id))  # JSON stores keys as strings
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    # Update allowed fields
    for field, value in update_data.items():
        if field in vehicle:
            vehicle[field] = value

    vehicle_db[str(vehicle_id)] = vehicle
    save_vehicle_data(vehicle_db)  # Save changes back to the JSON file
    return {"message": "Vehicle updated successfully", "vehicle": vehicle}

@vehicle_app.patch("/vehicle/{vehicle_id}")
def update_vehicle_patch(vehicle_id: UUID, update_data: dict, _: str = Depends(authenticate)):
    # Update part of the vehicle resource (partial update)
    vehicle = vehicle_db.get(str(vehicle_id))  # JSON stores keys as strings
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    # Update allowed fields
    for field, value in update_data.items():
        if field in vehicle:
            vehicle[field] = value

    vehicle_db[str(vehicle_id)] = vehicle
    save_vehicle_data(vehicle_db)  # Save changes back to the JSON file
    return {"message": "Vehicle updated successfully", "vehicle": vehicle}
