from time import time

import requests

from models import Sendung

BASE_URL: str = "http://127.0.0.1:8000/"


def create_sendung(neueSendung: Sendung):
    # TODO: How do you react if something goes wrong?
    response = requests.post(BASE_URL + "sendungen/", neueSendung.json())
    return response.status_code


def update_sendung(geaenderteSendung: Sendung):
    # TODO: How do you react if something goes wrong?
    response = requests.put(BASE_URL + "sendungen/", geaenderteSendung.json())
    return response.status_code


def get_sendung(sendung_id: int):
    response = requests.get(BASE_URL + "sendungen/" + str(sendung_id))
    # TODO: Change the data format so you can work with it
    # TODO: Filter for relevant information
    return response.content


if __name__ == '__main__':
    sendung = Sendung(sendung_id=1, erfassungszeitpunkt=time().__str__())
    print(create_sendung(sendung))
    print(get_sendung(1))
