import json
from fastapi import FastAPI, HTTPException, Depends
from uuid import UUID
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from decimal import Decimal
from typing import Dict

from .models import User

user_app = FastAPI()

security = HTTPBasic()

URL_FOR_USERS_DATA = 'mock_data/users_data.json'

# Load data from a local JSON file
def load_user_data():
    with open(URL_FOR_USERS_DATA, 'r') as file:
        return json.load(file)

# Save data to the JSON file
def save_user_data(data: Dict[UUID, User]):
    with open(URL_FOR_USERS_DATA, 'w') as file:
        json.dump(data, file, default=str)  # convert UUID and other complex types to string

# In-memory user data loaded from a local file
user_db = load_user_data()

# Basic Auth credentials
VALID_USERNAME = "user_service"
VALID_PASSWORD = "securepassword"

# Authentication function
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == VALID_USERNAME and credentials.password == VALID_PASSWORD:
        return credentials.username
    raise HTTPException(status_code=401, detail="Unauthorized")

@user_app.get("/user/{user_id}", response_model=User)
def get_user(user_id: UUID, _: str = Depends(authenticate)):
    user = user_db.get(str(user_id))  # JSON stores keys as strings
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_app.put("/user/{user_id}")
def update_user(user_id: UUID, update_data: dict, _: str = Depends(authenticate)):
    user = user_db.get(str(user_id))  # JSON stores keys as strings
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update allowed fields
    for field, value in update_data.items():
        if field in user:
            user[field] = value

    user_db[str(user_id)] = user
    save_user_data(user_db)  # Save changes back to the JSON file
    return {"message": "User updated successfully", "user": user}
