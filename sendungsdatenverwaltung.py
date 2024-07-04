from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from models import Sendung

app = FastAPI()
app.data = []  # Contains a list of Sendung


@app.get("/hello_world/", response_description="Hello World!")
def hello_world():
    """Hello World :D

    :return Hello World!
    """

    response = "Hello World!"
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.post("/sendungen/", response_description="Create sendung information", response_model=Sendung)
def create(data: Sendung):
    """Creates shipment information in the local storage of the server instance

    :param data:    Sendung object to store in the storage
    :return Sendung which was stored
    """

    # TODO: Check if shipment was already scanned
    app.data += [data]
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=data.json())


@app.put("/sendungen/", response_description="Update shipment information", response_model=Sendung)
def update(data: Sendung):
    """Updates shipment information in the local storage of the server instance

    :param data:    Sendung object to update in the storage
    :return Sendung which was updated
    """

    # TODO: Search for a specific shipment info and update all its data
    # TODO: What to do, if shipment does not exist?
    return JSONResponse(status_code=status.HTTP_200_OK, content=data.json())


@app.get("/sendungen/{sendung_id}", response_description="Get shipment information of particular sendung id", response_model=Sendung)
def get(sendung_id: int):
    """Retrieves shipment information specified by the given order_id

    :param sendung_id:    Unique identifier of the shipment information
    :return Sendung corresponding to the given sendung id
    """

    # TODO: search for the correct order id and return the result
    # TODO: What to do, if shipment does not exist?
    return JSONResponse(status_code=status.HTTP_200_OK, content=None)
