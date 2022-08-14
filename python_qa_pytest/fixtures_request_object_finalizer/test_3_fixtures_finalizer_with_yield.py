import pytest


@pytest.fixture(score="function")
def setup_function_fixture():
    print("\nHello from setup function fixture!\n")
    yield
    print("\nBye bye from setup function fixture!\n")


@pytest.fixture(score="module")
def setup_function_fixture():
    print("\nHello from setup module fixture!\n")
    yield
    print("\nBye bye from setup module fixture!\n")


def test_one(setup_function_fixture):
    pass


def test_two(setup_function_fixture):
    pass
