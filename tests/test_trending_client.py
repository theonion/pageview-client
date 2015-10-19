import json

from mock import MagicMock
import requests

from pageview_client.clients import TrendingClient


class Response(object):
    pass


mock_content = json.dumps([{
    "content_id": 2,
    "score": 55
}, {
    "content_id": 0,
    "score": 67
}, {
    "content_id": 1,
    "score": 78
}])

mock_byte_content = json.dumps([{
    "content_id": 3,
    "score": 20
}, {
    "content_id": 5,
    "score": 90
}, {
    "content_id": 4,
    "score": 80
}]).encode('utf-8')


def test_trendingclient_get():
    mock_response = Response()
    mock_response.ok = True
    mock_response.content = mock_content
    requests.get = MagicMock(return_value=mock_response)
    client = TrendingClient("example.com", "hello.json")

    content_ids = client.get("example")
    assert len(content_ids) == 3
    assert content_ids[0] == 1
    assert content_ids[1] == 0
    assert content_ids[2] == 2


def test_trendingclient_get_byte_response():
    mock_response = Response()
    mock_response.ok = True
    mock_response.content = mock_byte_content
    requests.get = MagicMock(return_value=mock_response)

    client = TrendingClient("example.com", "hello.json")
    content_ids = client.get("example")
    assert len(content_ids) == 3
    assert content_ids[0] == 5
    assert content_ids[1] == 4
    assert content_ids[2] == 3
