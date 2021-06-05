from src.clients.http_client import HTTPClient
from unittest import mock


client = HTTPClient(BASE_PATH="https://api.binance.com/api/v3/", suported_codes=[7777])

@mock.patch("src.clients.http_client.requests.get")
def test_request_get(mock_request_get, type=HTTPClient.RequestType.GET, path=""):
    mock_request_get.return_value = mock.Mock(**{"status_code": 7777})
    assert client.request(type=type, path=path) == mock_request_get(
        type=type, path=path
    )


@mock.patch("src.clients.http_client.requests.post")
def test_request_post(
    mock_request_post, type=HTTPClient.RequestType.POST, path="", body={}, params={}
):
    mock_request_post.return_value = mock.Mock(**{"status_code": 7777})
    assert client.request(
        type=type, path=path, body=body, params=params
    ) == mock_request_post(type=type, path=path, body=body, params=params)


@mock.patch("src.clients.http_client.requests.put")
def test_request_put(
    mock_request_put, type=HTTPClient.RequestType.PUT, path="", body={}, params={}
):
    mock_request_put.return_value = mock.Mock(**{"status_code": 7777})
    assert client.request(
        type=type, path=path, body=body, params=params
    ) == mock_request_put(type=type, path=path, body=body, params=params)


@mock.patch("src.clients.http_client.requests.delete")
def test_request_delete(
    mock_request_delete, type=HTTPClient.RequestType.DELETE, path=""
):
    mock_request_delete.return_value = mock.Mock(**{"status_code": 7777})
    assert client.request(type=type, path=path) == mock_request_delete(
        type=type, path=path
    )


@mock.patch("src.clients.http_client.requests.patch")
def test_request_patch(
    mock_request_patch, type=HTTPClient.RequestType.PATCH, path="", body={}, params={}
):
    mock_request_patch.return_value = mock.Mock(**{"status_code": 7777})
    assert client.request(
        type=type, path=path, body=body, params=params
    ) == mock_request_patch(type=type, path=path, body=body, params=params)

