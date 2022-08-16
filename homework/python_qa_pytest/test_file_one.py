import pytest


def test_one(fixture_list_compare):
    assert len(fixture_list_compare) == 8


@pytest.mark.parametrize("keyword, string", [("app", "apple"), ("win", "winter"), ("guse", "use")])
def test_keyword_in_string(keyword, string):
    assert keyword in string


def test_parametrize_list(fixture_with_params):
    assert fixture_with_params > 1
