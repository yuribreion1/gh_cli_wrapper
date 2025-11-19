"""
API Client Class created to assist handling
HTTP requests to GitHub
"""

import json
import requests
from requests.exceptions import HTTPError


class APIClient:
    """
    Class responsible to handle generic HTTP requests
    """

    def __init__(self, base_url, bearer_token):
        self.base_url = base_url
        self.bearer_token = bearer_token

        print(f"GitHub HTTP Client started to connect with: {self.base_url}")

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
            return json.dumps(response.json(), indent=4)
        except HTTPError as http_err:
            print(f"HTTP Error occurred: {http_err}")
            if http_err.response is not None:
                print(f"Status: {http_err.response.status_code}")
                print(f"Server Response: {http_err.response.text}")
            return None
