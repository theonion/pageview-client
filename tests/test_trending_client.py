import json

from mock import MagicMock
import requests

from pageview_client.clients import TrendingClient


class Response(object):
    pass


mock_content = json.dumps([{
    "content_id": 2,
    "score": 100
}, {
    "content_id": 0,
    "score": 97
}, {
    "content_id": 1,
    "score": 96
}])
mock_response = Response()
mock_response.ok = True
mock_response.content = mock_content
requests.get = MagicMock(return_value=mock_response)


def test_trendingclient_get():
    client = TrendingClient("example.com", "hello.json")
    content_ids = client.get("example")
    assert len(content_ids) == 3
    for cid in (2, 0, 1):
        assert cid in content_ids
