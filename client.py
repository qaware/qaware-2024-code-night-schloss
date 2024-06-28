from time import time

import requests

from models import PackageInfo

BASE_URL: str = "http://127.0.0.1:8000/"


def create_package_info(data: PackageInfo):
    # TODO: How do you react if something goes wrong?
    response = requests.post(BASE_URL + "packages/", data.json())
    return response.status_code


def update_package_info(data: PackageInfo):
    # TODO: How do you react if something goes wrong?
    response = requests.put(BASE_URL + "packages/", data.json())
    return response.status_code


def get_package_info(order_id: int):
    response = requests.get(BASE_URL + "packages/" + str(order_id))
    # TODO: Change the data format so you can work with it
    # TODO: Filter for relevant information
    return response.content


def get_all_package_info():
    response = requests.get(BASE_URL + "packages/")
    # TODO: Change the data format so you can work with it
    # TODO: Filter for relevant information
    return response.content


def delete_package_info():
    # TODO: Implement this method
    return


def clear_all_package_info():
    # TODO: Implement this method
    return


if __name__ == '__main__':
    package_info = PackageInfo(order_id=1, timestamp=time().__str__())
    print(create_package_info(package_info))
    print(get_all_package_info())
