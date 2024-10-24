from etl.base import ETLPipeline
from etl.extractors.sticker_extractor import StickerExtractor
from etl.transformers.sticker_transformer import StickerTransformer
from etl.loaders.sticker_loader import StickerLoader
from services.base_service import BaseService
from models.db_models import Sticker
from typing import Dict

class StickerPipeline(ETLPipeline):
    def __init__(self, field_mappings: Dict[str, str]):
        self.extractor = StickerExtractor()
        self.transformer = StickerTransformer(field_mappings)
        self.loader = StickerLoader(BaseService(Sticker))

    async def run(self):
        data = await self.extractor.process()
        transformed_data = await self.transformer.process(data)
        await self.loader.process(transformed_data)