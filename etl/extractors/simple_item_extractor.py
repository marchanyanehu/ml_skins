from etl.extractors.base_extractor import BaseExtractor
from apis.clients.tm_api_client import tm_v2_client
from typing import List, Dict, Any, AsyncGenerator

class SimpleItemExtractor(BaseExtractor):
    async def extract(self) -> List[Dict[str, Any]]:
        response = await tm_v2_client.get_simple_items()
        return response['items']

    async def process(self, data: Any = None) -> List[Dict[str, Any]]:
        return await self.extract()