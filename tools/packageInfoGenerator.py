import random
import time

import requests

BASE_URL: str = "http://127.0.0.1:8000/"

LOCATIONS = ["Berlin", "Bremen", "Dresden", "Duesseldorf", "Erfurt", "Hamburg", "Hannover", "Kiel", "Magdeburg",
             "Mainz", "Muenchen", "Potsdam", "Saarbruecken", "Schwerin", "Stuttgart", "Wiesbaden"]
STATUS = ["UNKNOWN", "SIGNED_IN", "SIGNED_OUT"]
DATE_SENT = ["UNKNOWN", "01.07.2023", "02.07.2023", "03.07.2023"]
DATE_ARRIVAL = ["UNKNOWN", "05.07.2023", "06.07.2023", "07.07.2023"]
PACKAGE_TYPE = ["UNKNOWN", "Food", "Technology", "Luxury", "Medicine", "Sports Equipment"]
INFO = ["-", "FRAGILE", "PERISHABLE", "CRITICAL"]


def send(data: dict):
    response = requests.post(BASE_URL + "packages/", str(data).replace("\'", "\""))
    return response.status_code, response.content


def get_random_element(data: list) -> str:
    return data[random.randint(0, len(data) - 1)]


def generate_info() -> dict:

    order_id = random.randint(0, 100)
    location_start = get_random_element(LOCATIONS)
    location_end = location_start
    while location_end == location_start:
        location_end = get_random_element(LOCATIONS)
    status = get_random_element(STATUS)
    date_sent = get_random_element(DATE_SENT)
    date_arrival = get_random_element(DATE_ARRIVAL)
    package_type = get_random_element(PACKAGE_TYPE)
    info = get_random_element(INFO)

    return {
        "order_id": order_id,
        "time_stamp": time.time().__str__(),
        "location_start": location_start,
        "location_end": location_end,
        "status": status,
        "date_sent": date_sent,
        "expected_arrival": date_arrival,
        "package_type": package_type,
        "info": info
    }


if __name__ == '__main__':
    while True:
        package_info = generate_info()
        response = send(package_info)
        print(f"Sent package info: {package_info}")
        time.sleep(2)

