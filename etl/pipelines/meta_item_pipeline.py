from etl.base import ETLPipeline
from etl.extractors.meta_item_extractor import MetaItemExtractor
from etl.transformers.meta_item_transformer import MetaItemTransformer
from etl.loaders.meta_item_loader import MetaItemLoader
from services.base_service import BaseService
from models.db_models import MetaItem
from typing import Dict

class MetaItemPipeline(ETLPipeline):
    def __init__(self, field_mappings: Dict[str, str]):
        self.extractor = MetaItemExtractor()
        self.transformer = MetaItemTransformer(field_mappings)
        self.loader = MetaItemLoader(BaseService(MetaItem))

    async def run(self):
        async for batch in self.extractor.process():
            transformed_batch = await self.transformer.process(batch)
            await self.loader.process(transformed_batch)
