from .base_client import BaseClient


class OrderClient(BaseClient):
    def api_resource(self):
        return "order"
