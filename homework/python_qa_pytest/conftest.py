import pytest


@pytest.fixture()
def fixture_list_compare(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)
    return [x for x in range(1, 9)]


@pytest.fixture(params=[x for x in range(0, 10)])
def fixture_with_params(request):
    return request.param
