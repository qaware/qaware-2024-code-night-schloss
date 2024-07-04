from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from models import Sendung

app = FastAPI()
app.data = []  # Contains a list of PackageInfo


@app.get("/hello_world/", response_description="Hello World!")
def hello_world():
    """Hello World :D

    :return Hello World!
    """

    response = "Hello World!"
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.post("/sendungen/", response_description="Create sendung information", response_model=Sendung)
def create(data: Sendung):
    """Creates package information in the local storage of the server instance

    :param data:    PackageInfo object to store in the storage
    :return PackageInfo which was stored
    """

    # TODO: Check if package was already scanned
    app.data += [data]
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=data.json())


@app.put("/packages/", response_description="Update package information", response_model=Sendung)
def update(data: Sendung):
    """Updates package information in the local storage of the server instance

    :param data:    PackageInfo object to update in the storage
    :return PackageInfo which was updated
    """

    # TODO: Search for a specific package info and update all its data
    # TODO: What to do, if package does not exist?
    return JSONResponse(status_code=status.HTTP_200_OK, content=data.json())


@app.get("/packages/{order_id}", response_description="Get package information of particular order id", response_model=Sendung)
def get(order_id: int):
    """Retrieves package information specified by the given order_id

    :param order_id:    Unique identifier of the package information
    :return PackageInfo corresponding to the given order id
    """

    # TODO: search for the correct order id and return the result
    # TODO: What to do, if package does not exist?
    return JSONResponse(status_code=status.HTTP_200_OK, content=None)
