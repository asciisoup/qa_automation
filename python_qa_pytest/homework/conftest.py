import pytest


@pytest.fixture()
def fixture_list_compare(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)
    return [x for x in range(1, 9)]
