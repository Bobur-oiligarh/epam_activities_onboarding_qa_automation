"""Contains several tests for flask api endpoint testing."""
import sys
from requests.status_codes import codes
from test_framework.fixtures.fixtures_flask_api import flask_app, root_json, \
   root_status, health_status, health_json
# from os.path import dirname, abspath
# d = dirname(dirname(abspath(__file__)))
# sys.path.append(d)


def test_root_status(root_status):
    """Validates status_code of response to root page."""
    assert root_status == codes.ok


def test_root_json(root_json):
    """Validates presence of json in response to root page."""
    assert root_json


def test_health_status(health_status):
    """Validates status_code of response to health page."""
    assert health_status == codes.ok


def test_health_json(health_json):
    """Validates presence of json in response to health page."""
    assert health_json
