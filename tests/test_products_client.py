import pytest

from kinguin_client import Kinguin


@pytest.fixture
def url():
    return "https://gateway.kinguin.net/esa/api/v1/products"


def test_products_client(requests_mock, url):
    client = Kinguin()
    requests_mock.get(url, json={"test": "test"}, status_code=200)
    response = client.products().get()

    assert response.get("test") == "test"
