import requests
import unittest

class BaseApiTest(unittest.TestCase):
    """
    Base class for API tests.
    """

    # Set the base URL of the API to be tested
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Define default headers for API requests
    headers = {
        'Content-Type': 'application/json'
    }

    # Define default authentication credentials (if required)
    auth = None

    def setUp(self):
        """
        Runs before each test case.
        """
        self.session = requests.Session()

    def tearDown(self):
        """
        Runs after each test case.
        """
        self.session.close()

    def api_request(self, method, endpoint, params=None, data=None, headers=None, auth=None):
        """
        Makes an API request using the requests module.
        """
        url = self.base_url + endpoint
        headers = headers or self.headers
        auth = auth or self.auth

        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers=headers,
            auth=auth
        )

        return response

    def assertStatusCode(self, response, expected_status_code):
        """
        Asserts that the status code of the API response matches the expected status code.
        """
        self.assertEqual(response.status_code, expected_status_code, f'Expected status code {expected_status_code}, but got {response.status_code}')

    def assertJsonResponse(self, response, expected_data):
        """
        Asserts that the JSON response of the API matches the expected data.
        """
        response_data = response.json()
        self.assertEqual(response_data, expected_data, f'Expected response data {expected_data}, but got {response_data}')
