**Project Name: MicroMocker - Fake API for User and Vehicle Services*

*Overview*
This project simulates the User and Vehicle microservices for Booking service development. Since the actual User and Vehicle services are not ready yet, a Fake API has been created using FastAPI to mock both services for quick and simultaneous development. This allows your team to continue working on the Booking service logic, which relies on data from these two services, without waiting for their completion.

Key Features:
- FastAPI: Used to build the Fake API for both User and Vehicle services.
- Basic Authentication: Both services implement Basic Authentication to ensure secure communication.
- Simultaneous Development: Both services are run simultaneously using Python's multiprocessing module, allowing quick integration and testing of the Booking service without relying on the actual services.

*Services Overview*
- User Service: Mocks user data including registration, balance, and license verification.
- Vehicle Service: Mocks vehicle data including booking status, payment types, and vehicle requirements.

*Project Setup*
Prerequisites: 
- Python 3.7 or higher
- FastAPI: Web framework for building the Fake API
- uvicorn: ASGI server for serving the FastAPI app
- multiprocessing: For running both services concurrently
- requests (for testing): Simple HTTP library to make requests to the services

*Installation*

1. Clone the repository to your local machine:
```git clone https://github.com/Epix-Labs/MicroMocker.git
cd micro-mocker
```
2. Install the required dependencies:
```pip install -r requirements.txt
```

*Running the Fake API*
To run both the User and Vehicle Fake APIs simultaneously, use the provided script:
```python main.py
```
- The User Service will run on http://127.0.0.1:8001.
- The Vehicle Service will run on http://127.0.0.1:8002.
Both services will be started concurrently via the multiprocessing module, simulating communication for the Booking Service.

*Service Endpoints*
*User Service*
- GET /user/{user_id}: Retrieve user details by user_id.
- PUT /user/{user_id}: Update user details by user_id.
Sample Request
```curl -X 'GET' 'http://127.0.0.1:8001/user/{user_id}' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic <base64_encoded_credentials>'
```

*Vehicle Service*
- GET /vehicle/{vehicle_id}: Retrieve vehicle details by vehicle_id.
- PUT /vehicle/{vehicle_id}: Update vehicle details by vehicle_id.
Sample Request
```curl -X 'PUT' 'http://127.0.0.1:8002/vehicle/{vehicle_id}' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic <base64_encoded_credentials>' \
  -H 'Content-Type: application/json' \
  -d '{
        "is_booked": true,
        "milage": 1200.5,
        "status": "available",
        "visible": true
      }'
```

*Authentication*
Both services use Basic Authentication. The format of the Authorization header is:
```Authorization: Basic <base64_encoded_string>
```
You can encode your username and password in base64 (for example, username:password), and include it in the header.

*Mock Data*
The User and Vehicle services use JSON formatted mock data instead of a database for easy testing. These files represent the data used by the services during development.

*Project Structure*
```
├── user_service/
│   ├── views.py             # FastAPI application for user service
│   ├── mock_data.json       # Mock data for user service
│   └── __init__.py
├── vehicle_service/
│   ├── views.py             # FastAPI application for vehicle service
│   ├── mock_data.json       # Mock data for vehicle service
│   └── __init__.py
├── run_services.py          # Script to run both services concurrently
├── requirements.txt         # List of dependencies
├── README.md                # Documentation file
└── .gitignore               # Git ignore file
```

**Contribution**
Feel free to fork this repository, submit issues, and create pull requests. Contributions are welcome!
