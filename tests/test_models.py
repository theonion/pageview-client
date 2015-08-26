from pageview_client.models import Trend


def test_trend_str():
    trend = Trend(123, 321)
    assert str(trend) == "<Trend: content_id=123 score=321>"


def test_trend_repr():
    trend = Trend(123, 321)
    assert str(trend) == "<Trend: content_id=123 score=321>"


def test_trends_are_orderable():
    trend0 = Trend(123, 100)
    trend1 = Trend(234, 99)
    trend2 = Trend(345, 101)
    trend3 = Trend(456, 98)
    trend4 = Trend(567, 100)
    trends = [trend0, trend1, trend2, trend3, trend4]
    sorted_trends = sorted(trends, reverse=True)
    expected_sort = [trend2, trend0, trend4, trend1, trend3]
    assert sorted_trends == expected_sort
