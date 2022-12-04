from kinguin_client.clients.balance_client import BalanceClient
from kinguin_client.clients.order_client import OrderClient
from kinguin_client.clients.products_client import ProductsClient


class Kinguin:

    BASE_URL = "https://gateway.kinguin.net/esa/"
    API_PATH = "api/v1/"

    def __init__(self, api_key: str = None):
        self.api_key = api_key

    @property
    def url(self):
        return f"{Kinguin.BASE_URL}{Kinguin.API_PATH}"

    def products(self):
        return ProductsClient(self.url, self.api_key)

    def orders(self):
        return OrderClient(self.url, self.api_key)

    def balance(self):
        return BalanceClient(self.url, self.api_key)
