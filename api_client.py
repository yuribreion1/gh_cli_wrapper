"""
API Client Class created to assist handling
HTTP requests to GitHub
"""

import json
import requests
from requests.exceptions import HTTPError
from logger import get_logger


class APIClient:
    """
    Class responsible to handle generic HTTP requests
    """

    def __init__(self, base_url, bearer_token):
        self.base_url = base_url
        self.bearer_token = bearer_token
        self.logger = get_logger(name="APIClient")
        self.logger.info(
            "GitHub HTTP Client started to connect with: %s", self.base_url
        )

    def get(self, endpoint):
        """
        Function dedicated to retrieve
        information from GitHub
        """

        full_url = f"{self.base_url}{endpoint}"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.bearer_token}",
        }

        requests_args = {"url": full_url, "timeout": 5, "headers": headers}

        try:
            response = requests.get(**requests_args)
            response.raise_for_status()
            self.logger.info(
                "Successful GET request to %s - Status %s",
                full_url,
                response.status_code,
            )
            return json.dumps(response.json(), indent=4)
        except HTTPError as http_err:
            self.logger.error("HTTP Error occurred: %s", http_err)
            if http_err.response is not None:
                self.logger.error("Status: %s", http_err.response.status_code)
                self.logger.error("Server Response: %s", http_err.response.text)
            return None
