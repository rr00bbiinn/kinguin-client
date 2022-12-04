from .base_client import BaseClient


class BalanceClient(BaseClient):
    def api_resource(self):
        return "balance"
