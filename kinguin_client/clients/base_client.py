import requests
from requests import Response


class BaseClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    @property
    def headers(self):
        return {
            "X-Api-Key": self.api_key,
            "Content-Type": "application/json",
        }

    def api_resource(self):
        return ""

    def handle_response(self, response: Response):
        if response.status_code in [200, 201, 202, 204]:
            return response.json()
        else:
            if "application/json" not in response.headers.get("Content-Type", ""):  # noqa: E501
                status_code, reason = response.status_code, response.reason
                raise KinguinError(
                    f"Unknown error (status code: {status_code}, reason: {reason})"  # noqa: E501
                )

            data = response.json()
            error_msg, status_code, kind = (
                data.get("detail") or "Unknown error",
                data.get("status"),
                data.get("kind"),
            )

            raise KinguinError(
                f"{error_msg} (status code: {status_code}, kind: {kind})"
            )  # noqa: E501


class GetClient(BaseClient):
    def get(self, resource_id: str = None, params: dict = None):

        if resource_id:
            query_url = f"{self.base_url}{self.api_resource()}/{resource_id}"
        else:
            query_url = f"{self.base_url}{self.api_resource()}"

        response = requests.get(query_url, params=params, headers=self.headers)

        return self.handle_response(response=response)


class PostClient(BaseClient):

    def post(self):
        raise NotImplementedError()


class KinguinError(Exception):
    """Kinguin Error"""

    ...
