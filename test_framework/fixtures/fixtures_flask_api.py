"""The module with three fixtures to test flask api endpoints"""
import os
from typing import Dict

import pytest
import yaml
import requests
from requests import Response

FLASK_API_EXPECTED_DATA_FILE = 'flask_api_data.yaml'


@pytest.fixture()
def get_data_flask_api_file(request) -> Dict:
    """This tool extracts ec2 datas from .yaml file to python readable type: dictionary
    Here uses the request fixture to get the full path of .yaml file

    :return: dictionary filled with file content
    """
    dir_path = os.path.dirname(request.module.__file__)
    file_path = os.path.join(dir_path, FLASK_API_EXPECTED_DATA_FILE)
    with open(file_path) as file:
        documents = yaml.load(file, Loader=yaml.SafeLoader)
    return documents


@pytest.fixture()
def get_response_from_root(get_data_flask_api_file) -> Response:
    """This fixture gets request for root endpoint and return its response

    :param get_data_flask_api_file: fixture which gives dictionary from data.yaml
    :return: Response object
    """
    response = requests.get(get_data_flask_api_file['root']['link'])
    return response


@pytest.fixture()
def get_response_from_health(get_data_flask_api_file) -> Response:
    """This fixture gets request for health endpoint and return its response

    :param get_data_flask_api_file: fixture which gives dictionary from data.yaml
    :return: Response object
    """
    response = requests.get(get_data_flask_api_file['health']['link'])
    return response


