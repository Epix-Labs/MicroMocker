import uvicorn
from multiprocessing import Process

from user_service.views import user_app
from vehicle_service.views import vehicle_app


def run_user_service():
    uvicorn.run(user_app, host='0.0.0.0', port=8001)


def run_vehicle_service():
    uvicorn.run(vehicle_app, host='0.0.0.0', port=8002)


if __name__ == "__main__":
    service1 = Process(target=run_user_service)
    service2 = Process(target=run_vehicle_service)

    service1.start()
    service2.start()

    service1.join()
    service2.join()