from .base_client import GetClient


class ProductsClient(GetClient):
    def api_resource(self):
        return "products"
