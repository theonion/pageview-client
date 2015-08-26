import pytest

from pageview_client.clients import BasePageviewClient


def test_basepageviewclient_clean_scheme():
    scheme0 = BasePageviewClient._clean_scheme("http://")
    assert scheme0 == "http://"
    scheme1 = BasePageviewClient._clean_scheme("https")
    assert scheme1 == "https://"


def test_basepageviewclient_clean_hostname():
    hostname0 = BasePageviewClient._clean_hostname("example.com/")
    assert hostname0 == "example.com/"
    hostname1 = BasePageviewClient._clean_hostname("example2.org")
    assert hostname1 == "example2.org/"


def test_basepageviewclient_build_url():
    scheme = "http"
    hostname = "example.com"
    endpoint = "hello.json"
    url = BasePageviewClient._build_url(scheme, hostname, endpoint)
    assert url == "http://example.com/hello.json"


def test_basepageviewclient_get():
    client = BasePageviewClient("example.com", "hello.json")
    with pytest.raises(NotImplementedError):
        client.get()
