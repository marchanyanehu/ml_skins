import httpx
from urllib.parse import urlencode

# TODO ADD INHERITANCE FROM BaseModel OF WEB ENGINE
class APIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key

    def _build_url(self, endpoint, params=None):
        if params is None:
            params = {}
        if self.api_key:
            params['key'] = self.api_key
        query_string = urlencode(params)
        return f"{self.base_url}/{endpoint}?{query_string}"
    
    def get(self, endpoint, params=None):
        url = self._build_url(endpoint, params)
        response = httpx.get(url)
        return self._handle_response(response)
    
    def post(self, endpoint, data, params=None):
        url = self._build_url(endpoint, params)
        response = httpx.post(url, data=data)
        return self._handle_response(response)
    
    def _handle_response(self, response):
        response.raise_for_status()
        return response.json()
    
    async def async_get(self, endpoint, params=None):
        url = self._build_url(endpoint, params)
        async with httpx.AsyncClient() as client:
            print(f"Requesting {url}")
            response = await client.get(url, timeout=10)
        return self._handle_response(response)
    
    async def async_post(self, endpoint, data, params=None):
        url = self._build_url(endpoint, params)
        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=data)
        return self._handle_response(response)
    
