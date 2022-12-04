from kinguin_client.clients.balance_client import BalanceClient
from kinguin_client.clients.order_client import OrderClient
from kinguin_client.clients.products_client import ProductsClient


class Kinguin:

    BASE_URL = "https://gateway.kinguin.net/esa/"
    SANDBOX_URL = "https://gateway.sandbox.kinguin.net/esa/"
    API_PATH = "api/v1/"

    def __init__(self, api_key: str = None, sandbox: bool = False):
        self.api_key = api_key
        self.sandbox = sandbox

    @property
    def url(self):
        if self.sandbox:
            return f"{Kinguin.SANDBOX_URL}{Kinguin.API_PATH}"
        return f"{Kinguin.BASE_URL}{Kinguin.API_PATH}"

    def products(self):
        return ProductsClient(self.url, self.api_key)

    def orders(self):
        return OrderClient(self.url, self.api_key)

    def balance(self):
        return BalanceClient(self.url, self.api_key)
