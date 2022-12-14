import pytest
import requests


@pytest.mark.parametrize("Id", [1, 2, 3])
def test_get_requst(Id):
    r = requests.get(
        url='https://reqres.in/api/users/2',
        data={"id": Id}
    ).json()

    assert r['data']['id'] == Id
