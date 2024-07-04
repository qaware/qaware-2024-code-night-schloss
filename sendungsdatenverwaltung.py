from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from models import Sendung

app = FastAPI()
app.data = []  # Enthält eine Liste aller Sendungsinformationen


@app.get("/hello_world/", response_description="Hello World!")
def hello_world():
    """Hello World :D

    :return Hello World!
    """

    response = "Hello World!"
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.post("/sendungen/", response_description="Erstellt eine Sendungsinformation", response_model=Sendung)
def create(data: Sendung):
    """Erstellt eine Sendungsinformation im lokalen Speicher des Verwaltungssystems

    :param data:    Sendungsinformation, die abgespeichert werden soll
    :return Sendungsinformation, die gespeichert wurde
    """

    # TODO: Wurder diese Sendung vielleicht bereits gescanned?
    # TODO: Fehlen Informationen zur Sendung die benötigt werden?
    app.data += [data]
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=data.json())


@app.put("/sendungen/", response_description="Aktualisiert eine Sendungsinformation", response_model=Sendung)
def update(data: Sendung):
    """Aktualisiert eine Sendungsinformation im lokalen Speicher des Verwaltungssystems

    :param data:    Aktualisierte Sendungsinformation, die im Speicher abgelegt werden soll
    :return Gespeicherte, aktualisierte Sendungsinformation
    """

    # TODO: Suche im lokalen Speicher nach der Sendungsinformationen und aktualisiere ihre Daten
    # TODO: Was tun wir, wenn die gegebene Sendung nicht existiert?
    return JSONResponse(status_code=status.HTTP_200_OK, content=data.json())


@app.get("/sendungen/{sendung_id}", response_description="Erhebt eine Sendungsinformation", response_model=Sendung)
def get(sendung_id: int):
    """Erhebt eine Sendungsinformation basierend auf der übergebenen Sendungs-ID

    :param sendung_id:      Sendungs-ID der zu erhebenden Sendungsinformationen
    :return Sendungsinformation mit gegebener Sendungs-ID
    """

    # TODO: Suche im lokalen Speicher nach der korrekten Sendungsinformation
    # TODO: Was tun wir, wenn die gegebene Sendung nicht existiert?
    return JSONResponse(status_code=status.HTTP_200_OK, content=None)
