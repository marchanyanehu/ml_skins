from apis.models.api_base_model import APIClient
from typing import Literal, Optional

class MCTMApiClient(APIClient):
    def __init__(self, base_url, api_key=None):
        super().__init__("https://market.csgo.com/api", api_key)

    async def get_all_items(self, lang: str = 'en'):
        return await self.async_get(f"items?lang={lang}")


    def get_stickers(self, lang: str = 'en'):
        return self.get(f"v2/stickers?lang={lang}")