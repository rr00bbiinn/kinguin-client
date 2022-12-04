from kinguin_client import Kinguin, __version__


def test_version():
    assert __version__ == "0.1.0"


def test_kinguin_client():
    client = Kinguin(api_key="api_key")

    assert client.api_key == "api_key"
    assert client.url == "https://gateway.kinguin.net/esa/api/v1/"


def test_kinguin_sandbox_client():
    client = Kinguin(api_key="api_key", sandbox=True)

    assert client.url == "https://gateway.sandbox.kinguin.net/esa/api/v1/"
