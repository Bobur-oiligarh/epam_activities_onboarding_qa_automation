"""The module with three fixtures to test flask api endpoints"""
from typing import Dict

import pytest
from test_framework.clients.flask_client import FlaskClient
from test_framework.clients.http_responce import HttpResponse
from test_framework.constants import FlaskConstant


@pytest.fixture()
def flask_app() -> FlaskClient:
    """Creates an instance of FlaskClient."""
    return FlaskClient(urls_set=FlaskConstant())


@pytest.fixture()
def root_status(flask_app) -> int:
    """Fixture which returns status_code of request to root.
    :param: flask_app: fixture with FlaskClient object.
    :return: status_code of root page response.
    """
    root_response = flask_app.root_request()
    status = HttpResponse(root_response).get_status()
    return status


@pytest.fixture()
def root_json(flask_app) -> Dict:
    """Fixture which returns json of content of root page response.

    :param: flask_app: fixture, FlaskClient object.
    :return: Dictionary. json of response of request to root page.
    """
    root_response = flask_app.root_request()
    json = HttpResponse(root_response).get_json()
    return json


@pytest.fixture()
def health_status(flask_app) -> int:
    """Fixture which returns status_code of request to health page.
    :param: flask_app: fixture with FlaskClient object.
    :return: status_code of response of health page.
    """
    health_response = flask_app.health_request()
    status = HttpResponse(health_response).get_status()
    return status


@pytest.fixture()
def health_json(flask_app) -> Dict:
    """Fixture which returns json of content of health page response.

    :param: flask_app: fixture, FlaskClient object.
    :return: Dictionary. json of response of request to health page.
    """
    health_response = flask_app.health_request()
    json = HttpResponse(health_response).get_json()
    return json
