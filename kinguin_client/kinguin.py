class Kinguin:

    BASE_URL = "https://gateway.kinguin.net/esa/"
    API_PATH = "api/v1/"

    def __init__(self, api_key: str = None):
        self.api_key = api_key

    @property
    def url(self):
        return f"{Kinguin.BASE_URL}{Kinguin.API_PATH}"
