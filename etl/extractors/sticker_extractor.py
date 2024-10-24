from etl.extractors.base_extractor import BaseExtractor
from apis.clients.tm_api_client import tm_v2_client
from typing import List, Dict, Any

class StickerExtractor(BaseExtractor):
    async def extract(self) -> List[Dict[str, Any]]:
        response = await tm_v2_client.get_stickers()
        return response['data']

    async def process(self, data: Any = None) -> List[Dict[str, Any]]:
        return await self.extract()