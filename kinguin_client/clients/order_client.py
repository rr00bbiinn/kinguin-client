from .base_client import GetClient, PostClient


class OrderClient(GetClient, PostClient):
    def api_resource(self):
        return "order"
