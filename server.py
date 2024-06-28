from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from models import PackageInfo

app = FastAPI()
app.data = []  # Contains a list of PackageInfo


@app.get("", response_description="Hello World!")
def hello_world():
    """Hello World :D

    :return Hello World!
    """

    response = "Hello World!"
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.post("/packages/", response_description="Create package information", response_model=PackageInfo)
def create(data: PackageInfo):
    """Creates package information in the local storage of the server instance

    :param data:    PackageInfo object to store in the storage
    :return PackageInfo which was stored
    """

    # TODO: Check if package was already scanned
    app.data += [data]
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=data.json())


@app.put("/packages/", response_description="Update package information", response_model=PackageInfo)
def update(data: PackageInfo):
    """Updates package information in the local storage of the server instance

    :param data:    PackageInfo object to update in the storage
    :return PackageInfo which was updated
    """

    # TODO: Search for a specific package info and update all its data
    # TODO: What to do, if package does not exist?
    return JSONResponse(status_code=status.HTTP_200_OK, content=data.json())


@app.get("/packages/{order_id}", response_description="Get package information of particular order id", response_model=PackageInfo)
def get(order_id: int):
    """Retrieves package information specified by the given order_id

    :param order_id:    Unique identifier of the package information
    :return PackageInfo corresponding to the given order id
    """

    # TODO: search for the correct order id and return the result
    # TODO: What to do, if package does not exist?
    return JSONResponse(status_code=status.HTTP_200_OK, content=None)


@app.get("/packages/", response_description="List all package information", response_model=list[PackageInfo])
def list_all():
    """Retrieves all package information specified in the local storage of the server instance

    :return List of PackageInfos
    """

    # TODO: Is all relevant data displayed?
    response = [package_info.to_dict() for package_info in app.data]
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@app.delete("/packages/{order_id}", response_description="Delete package information of particular order id")
def delete(order_id: int):
    """Deletes package information specified by the given order_id

    :param order_id:    Unique identifier of the package information
    """

    # TODO: search for the correct order id and delete it
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)


@app.delete("/packages/", response_description="Delete all package information")
def clear():
    """Deletes all package information"""

    # TODO: Are you sure, that everything should be deleted?
    app.data = []
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
