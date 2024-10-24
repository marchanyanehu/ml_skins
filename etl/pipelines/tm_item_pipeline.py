from etl.base import ETLPipeline
from etl.extractors.tm_item_extractor import TMItemExtractor
from etl.transformers.tm_item_transformer import ItemTransformer
from etl.loaders.db_loader import DBLoader
from services.base_service import BaseService
from models.db_models import ItemFullExport
from typing import Dict

class ItemPipeline(ETLPipeline):
    def __init__(self, field_mappings: Dict[str, str], batch_size: int = 100):
        self.extractor = TMItemExtractor(batch_size)
        self.transformer = ItemTransformer(field_mappings)
        self.loader = DBLoader(BaseService(ItemFullExport))

    async def run(self):
        async for batch in self.extractor.process():
            transformed_batch = await self.transformer.process(batch, self.extractor.format)
            await self.loader.process(transformed_batch)