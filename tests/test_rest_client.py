"""This module contains test cases for the RESTClient class.

The test cases are written using the pytest library and use the mock library to
mock the API responses.

"""
import json
from unittest.mock import patch
from rest_client import RESTClient


class TestRESTClient:
    @classmethod
    def setup_class(cls):
        """Set up the test environment.

        This method is run once before any test functions are called.
        """
        cls.client = RESTClient("https://jsonplaceholder.typicode.com")

    def test_get_request(self):
        """Test that a GET request to the API returns the correct response.

        This test case calls the `get()` method on the `RESTClient` object, and
        asserts that the `id` field of the response is equal to 1.
        """
        response = self.client.get("/posts/1")
        assert response["id"] == 1

    @patch("rest_client.requests.post")
    def test_post_request(self, mock_post):
        """Test that a POST request to the API returns the correct response.

        This test case mocks the API response using the `mock_post` object, and
        calls the `post()` method on the `RESTClient` object. It then asserts
        that the `id` field of the response is equal to 101.
        """
        mock_response = {"id": 101}
        mock_post.return_value.json.return_value = mock_response

        response = self.client.post("/posts", json={"title": "Test"})
        assert response["id"] == 101

    @patch("rest_client.requests.put")
    def test_put_request(self, mock_put):
        """Test that a PUT request to the API returns the correct response.

        This test case mocks the API response using the `mock_put` object, and
        calls the `put()` method on the `RESTClient` object. It then asserts
        that the `title` field of the response is equal to "Test".
        """
        mock_response = {"id": 1, "title": "Test"}
        mock_put.return_value.json.return_value = mock_response

        response = self.client.put("/posts/1", json={"title": "Test"})
        assert response["title"] == "Test"

    @patch("rest_client.requests.delete")
    def test_delete_request(self, mock_delete):
        """Test that a DELETE request to the API returns the correct response.

        This test case mocks the API response using the `mock_delete` object,
        and calls the `delete()` method on the `RESTClient` object. It then
        asserts that the response is an empty dictionary.
        """
        mock_response = {}
        mock_delete.return_value.json.return_value = mock_response

        response = self.client.delete("/posts/1")
        assert response == {}

    @patch("rest_client.requests.patch")
    def test_patch_request(self, mock_patch):
        """Test that a PATCH request to the API returns the correct response.

        This test case mocks the API response using the `mock_patch` object,
        and calls the `patch()` method on the `RESTClient` object. It then
        asserts that the `title` field of the response is equal to "Test".
        """
        mock_response = {"id": 1, "title": "Test"}
        mock_patch.return_value.json.return_value = mock_response

        response = self.client.patch("/posts/1", json={"title": "Test"})
        assert response["title"] == "Test"
