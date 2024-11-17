from etl.base import ETLPipeline
from etl.extractors.simple_item_extractor import SimpleItemExtractor
from etl.transformers.simple_item_transformer import SimpleItemTransformer
from etl.loaders.simple_item_loader import SimpleItemLoader
from services.base_service import BaseService
from models.db_models import SimpleItem
from typing import Dict
from services.base_service import BaseService

steam_service = BaseService(model=SimpleItem)

class SimpleItemPipeline(ETLPipeline):
    def __init__(self, field_mappings: Dict[str, str]):
        steam_service.truncate_table()
        self.extractor = SimpleItemExtractor()
        self.transformer = SimpleItemTransformer(field_mappings)
        self.loader = SimpleItemLoader(BaseService(SimpleItem))

    async def run(self):
        data = await self.extractor.process()
        transformed_data = await self.transformer.process(data)
        await self.loader.process(transformed_data)