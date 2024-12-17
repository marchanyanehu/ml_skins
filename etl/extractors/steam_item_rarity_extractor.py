from etl.extractors.base_extractor import BaseExtractor
from apis.clients.hexaone_api_client import hexaone_client
from typing import Dict, Any

class SteamItemRarityExtractor(BaseExtractor):
    async def extract(self) -> Dict[str, Any]:
        response = await hexaone_client.get_market_items()
        return response['result']['items']

    async def process(self, data: Any = None) -> Dict[str, Any]:
        return await self.extract()