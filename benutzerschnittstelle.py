from time import time

import requests

from models import Sendung

BASE_URL: str = "http://127.0.0.1:8000/"


def create_sendung(neueSendung: Sendung):
    # TODO: Was tun wir, wenn das Verwaltungssystem nicht/falsch reagiert?
    response = requests.post(BASE_URL + "sendungen/", neueSendung.json())
    return response.status_code


def update_sendung(geaenderteSendung: Sendung):
    # TODO: Was tun wir, wenn das Verwaltungssystem nicht/falsch reagiert?
    response = requests.put(BASE_URL + "sendungen/", geaenderteSendung.json())
    return response.status_code


def get_sendung(sendung_id: int):
    response = requests.get(BASE_URL + "sendungen/" + str(sendung_id))
    # TODO: Passe das Format der Antwort an um die Ergebnisse besser darstellen zu können
    # TODO: Filtere die relevanten Informationen heraus
    # TODO: Biete dem Nutzer eine entsprechende Meldung, falls keine Sendungsinformation gefunden wurde
    return response.content


if __name__ == '__main__':
    sendung = Sendung(sendung_id=1, erfassungszeitpunkt=time().__str__())
    print(create_sendung(sendung))
    print(get_sendung(1))
