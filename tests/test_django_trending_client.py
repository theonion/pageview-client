import json

from mock import MagicMock
import pytest
import requests

from pageview_client.clients import DjangoTrendingClient

from example.app.models import Article


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

article0 = Article(title="article 0", pk=0)
article1 = Article(title="article 1", pk=1)
article2 = Article(title="article 2", pk=2)
Article.objects.all = MagicMock(return_value=[article0, article1, article2])
Article.objects.in_bulk = MagicMock(return_value={0: article0, 1: article1, 2: article2})


@pytest.mark.django_db
def test_djangotrendingclient_get():
    client = DjangoTrendingClient(
        Article.objects.in_bulk, Article.objects.all, hostname="example.com", endpoint="hello.json")
    articles = client.get("example")
    expected = [article2, article0, article1]
    assert articles == expected
