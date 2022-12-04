from .base_client import GetClient


class BalanceClient(GetClient):
    def api_resource(self):
        return "balance"
