"""Contains FlaskClient class."""
from requests import Response
from test_framework.clients.http_client import HttpClient
from test_framework.constants import FlaskConstant


class FlaskClient(HttpClient):
    """Class to initialize flask api endpoints."""

    def __init__(self, urls_set: FlaskConstant):
        """Initializes flask api instance and its superclass."""
        self.urls = urls_set
        super().__init__(self.urls.BASE_URL)

    def root_request(self) -> Response:
        """Does request to root page.

        :return: response of request
        """
        return self.get_request(self.urls.ROOT)

    def health_request(self) -> Response:
        """Does request to health page.

        :return: response of request
        """
        return self.get_request(self.urls.HEALTH)
