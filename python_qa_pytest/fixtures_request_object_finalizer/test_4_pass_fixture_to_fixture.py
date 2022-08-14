import pytest


@pytest.fixture
def fixture_one():
    print("\nHey, this is fixture one!")
    yield
    print("\nBye bye from fixture one!")


@pytest.fixture
def fixture_two(fixture_one):
    print("\nHey, this is fixture two!")
    yield
    print("\nBye bye from fixture two!")


def test_function(fixture_two):
    print("\nHey, I'm test function!")
