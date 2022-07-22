"""Contains custom HttpResponse class."""
from typing import Dict

from requests import Response
import logging

logger = logging.getLogger()


class HttpResponse:
    """Class which manipulates http responses."""

    def __init__(self, response: Response):
        """Initializes methods and attributes from HttpClient."""
        self.response = response

    def get_status(self) -> int:
        """Gets status_code of response object for requested endpoint.

        :return: integer, status_code of response
        """
        try:
            return self.response.status_code
        except AttributeError as err:
            print(f"Connection was not created. Please check your inputted url value. {err}")
            logger.warning(f"Warning")

    def get_json(self) -> Dict:
        """Gets json of response object for requested endpoint.

        :return: string, Response.json
        """
        try:
            return self.response.json()
        except AttributeError as err:
            print(f"Connection was not created. Please check your inputted url value. {err}")

