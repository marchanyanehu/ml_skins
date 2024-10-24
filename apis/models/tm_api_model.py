from apis.models.api_base_model import APIClient
from typing import Literal, Optional

class TmApiV1Client(APIClient):
    def __init__(self, api_key=None):
        super().__init__(base_url="https://market.csgo.com/api", api_key=api_key)

    def get_full_export_preview(self, currency: Literal['USD', 'EUR'] = 'USD'):
        return self.get(f"full-export/{currency}.json") 

    async def get_full_export_by_json(self, json_id: str):
        return await self.async_get(f"full-export/{json_id}")


class TmApiV2Client(APIClient):
    def __init__(self, api_key=None):
        super().__init__(base_url="https://market.csgo.com/api/v2", api_key=api_key)
    
    async def get_stickers(self, lang: Literal['en', 'ru'] = 'en'):
        return await self.async_get("stickers" , params={'lang': lang})
    
    async def get_simple_items(self, currency: Literal['USD', 'EUR'] = 'USD'):
        return await self.async_get(f"prices/{currency}.json")
    
    async def get_meta_data_of_items(self, currency: Literal['USD', 'EUR'] = 'USD'):
        return await self.async_get(f"prices/class_instance/{currency}.json")