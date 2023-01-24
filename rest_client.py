"""This module provides a `RESTClient` class for making REST API calls.

The `RESTClient` class can be used to make GET, POST, PUT, PATCH and DELETE
requests to a REST API. When initializing the class, pass in the base URL of
the API, and other optional parameters such as `auth`, `timeout` and `verify`.
Then, call the appropriate method (`get()`, `post()`, `put()`, `patch()` or
`delete()`) and pass in the endpoint you want to call, along with any necessary
data or parameters. The methods return the JSON response from the API.

This module also supports authentication, timeouts and certificate validation.
The `auth`, `timeout` and `verify` parameters can be passed to the class
constructor to set authentication credentials, a timeout for all API calls and
validate the SSL certificate.

"""

import requests


class RESTClient:
    def __init__(self, base_url, auth=None, timeout=None, verify=True):
        """Initialize a new RESTClient.

        Args:
            base_url (str): The base URL of the API.
            auth (Optional[Tuple[str,str]]): Authentication credentials
                (optional).
            timeout (Optional[int]): Timeout for API calls in seconds
                (optional).
            verify (bool): Verify SSL certificate (default True)
        """
        self.base_url = base_url
        self.auth = auth
        self.timeout = timeout
        self.verify = verify

    def get(self, endpoint, params=None):
        """Make a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint.
            params (Optional[Dict[str, str]]): Query parameters (optional).

        Returns:
            dict: JSON response from the API.
        """
        url = self.base_url + endpoint
        response = requests.get(
            url,
            auth=self.auth,
            timeout=self.timeout,
            verify=self.verify,
            params=params,
        )
        return response.json()

    def post(self, endpoint, data=None, json=None):
        """Make a POST request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint.
            data (Optional[Dict[str, Any]]): Data to be sent in the request
                body (optional).
            json (Optional[Dict[str, Any]]): JSON data to be sent in the
                request body (optional).

        Returns:
            dict: JSON response from the API.
        """
        url = self.base_url + endpoint
        response = requests.post(
            url,
            auth=self.auth,
            timeout=self.timeout,
            verify=self.verify,
            data=data,
            json=json,
        )
        return response.json()

    def put(self, endpoint, data=None):
        """Make a PUT request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint.
            data (Optional[Dict[str, Any]]): Data to be sent in the request
                body (optional).

        Returns:
            dict: JSON response from the API.
        """
        url = self.base_url + endpoint
        response = requests.put(
            url,
            auth=self.auth,
            timeout=self.timeout,
            verify=self.verify,
            data=data,
        )
        return response.json()

    def delete(self, endpoint):
        """Make a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint.

        Returns:
            dict: JSON response from the API.
        """
        url = self.base_url + endpoint
        response = requests.delete(
            url, auth=self.auth, timeout=self.timeout, verify=self.verify
        )
        return response.json()

    def patch(self, endpoint, data=None):
        """Make a PATCH request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint.
            data (Optional[Dict[str, Any]]): Data to be sent in the request
                body (optional).

        Returns:
            dict: JSON response from the API.
        """
        url = self.base_url + endpoint
        response = requests.patch(
            url,
            auth=self.auth,
            timeout=self.timeout,
            verify=self.verify,
            data=data,
        )
        return response.json()
