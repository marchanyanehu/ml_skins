from etl.extractors.base_extractor import BaseExtractor
from apis.clients.tm_api_client import tm_v2_client
from typing import List, Dict, Any, AsyncGenerator

class MetaItemExtractor(BaseExtractor):
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size

    async def extract(self) -> AsyncGenerator[List[Dict[str, Any]], None]:
        response = await tm_v2_client.get_meta_data_of_items()
        items = list(response['items'].values())
        
        for i in range(0, len(items), self.batch_size):
            yield items[i:i+self.batch_size]

    async def process(self, data: Any = None) -> AsyncGenerator[List[Dict[str, Any]], None]:
        async for batch in self.extract():
            yield batch
