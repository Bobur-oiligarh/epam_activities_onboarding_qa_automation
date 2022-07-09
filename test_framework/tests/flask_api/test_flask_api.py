"""Contains several tests for flask api endpoint testing"""
from requests.status_codes import codes

from test_framework.fixtures.fixtures_flask_api import get_data_flask_api_file, \
    get_response_from_root, get_response_from_health


def test_root_status(get_response_from_root):
    """Validate status_code of root endpoint"""
    status_code = get_response_from_root.status_code
    assert status_code == codes.ok


def test_root_json(get_response_from_root):
    """Validate  the presence of json in root endpoint response"""
    assert get_response_from_root.json()


def test_health_status(get_response_from_health):
    """Validate status_code of root endpoint"""
    status_code = get_response_from_health.status_code
    assert status_code == codes.ok


def test_health_json(get_response_from_health):
    """Validate  the presence of json in health endpoint response"""
    assert get_response_from_health.json()

