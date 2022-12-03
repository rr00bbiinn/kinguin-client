from .base_client import BaseClient


class ProductsClient(BaseClient):
    def api_resource(self):
        return "products"
