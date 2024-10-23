from etl.extractors.base_extractor import BaseExtractor
from apis.clients.tm_api_client import tm_v1_client
from typing import List, Dict, Any, AsyncGenerator

class TMItemExtractor(BaseExtractor):
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size
        self.format = None

    async def extract(self) -> AsyncGenerator[List[Dict[str, Any]], None]:
        preview = tm_v1_client.get_full_export_preview()
        self.format = preview['format']
        json_files = preview['items']
        
        batch = []
        for json_file in json_files:
            items = await tm_v1_client.get_full_export_by_json(json_file)
            batch.extend(items)
            
            while len(batch) >= self.batch_size:
                yield batch[:self.batch_size]
                batch = batch[self.batch_size:]
        
        if batch:
            yield batch

    async def process(self, data: Any = None) -> AsyncGenerator[List[Dict[str, Any]], None]:
        async for batch in self.extract():
            yield batch