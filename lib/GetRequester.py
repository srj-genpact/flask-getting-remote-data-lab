import requests
import json

class GetRequester:
    """
    A generic requester class to retrieve remote data from an HTTP API endpoint.
    On initialization, it stores the target URL and can fetch raw response bodies
    or deserialize JSON payloads.
    """

    def __init__(self, url):
        """Initializes the GetRequester with a target endpoint URL."""
        self.url = url

    def get_response_body(self):
        """
        Queries the stored URL endpoint via an HTTP GET request.
        Returns the raw response content as bytes.
        """
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """
        Retrieves the raw HTTP response body and deserializes it into Python
        data structures (e.g. lists, dicts).
        """
        return json.loads(self.get_response_body())