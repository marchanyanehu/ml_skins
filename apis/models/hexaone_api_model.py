from models.api_base_model import APIClient
from urllib.parse import urlencode
import httpx



class HexaOneApiModel(APIClient):
    def __init__(self, base_url="https://hexa.one/api/v1", api_key=None):
        super().__init__(base_url=base_url, api_key=api_key)

    def _build_url(self, endpoint, params=None):
        if params is None:
            params = {}
        query_string = urlencode(params)
        return f"{self.base_url}/{endpoint}?{query_string}"
    
    def _build_auth_header(self, key):
        if key is None:
            return {}
        return {
            "X-API-Key": key
        }

    def get(self, endpoint, params=None, headers=None):
        url = self._build_url(endpoint, params)
        response = httpx.get(url, headers=headers)
        return self._handle_response(response)
    

    def get_account_info(self):
        return self.get("api/account", headers=self._build_auth_header(self.api_key))

    def get_market_prices(self, game_id: str = '730'):
        return self.get(f"market/prices/{game_id}", headers=self._build_auth_header(self.api_key))
