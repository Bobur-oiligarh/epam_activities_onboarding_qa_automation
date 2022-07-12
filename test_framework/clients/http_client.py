"""Contains HttpClient class which is universally connects to any server."""
from urllib.parse import urljoin
import requests
from requests import Response
from requests.exceptions import MissingSchema


class HttpClient:
    """A class for making HTTP connect to any url."""

    def __init__(self, base_url: str):
        """Initializes Base URL for http client.

        :param: base_url: string.
        """
        self.base_url = base_url

    def get_request(self, endpoint_url: str = None) -> Response:
        """Makes a GET request.

        :param endpoint_url: relative URL of endpoint
        :return: Response object
        """
        full_url = urljoin(self.base_url, endpoint_url)
        try:
            return requests.get(full_url)
        except MissingSchema as err:
            print(f"Your inputted url is invalid. {err}")

