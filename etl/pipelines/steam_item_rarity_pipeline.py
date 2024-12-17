from etl.base import ETLPipeline
from etl.extractors.steam_item_rarity_extractor import SteamItemRarityExtractor
from etl.transformers.steam_item_rarity_transformer import SteamItemRarityTransformer
from etl.loaders.steam_item_rarity_loader import SteamItemRarityLoader
from services.base_service import BaseService
from models.db_models import SteamItemRarity
from typing import Dict

class SteamItemRarityPipeline(ETLPipeline):
    def __init__(self, field_mappings: Dict[str, str]):
        self.extractor = SteamItemRarityExtractor()
        self.transformer = SteamItemRarityTransformer(field_mappings)
        self.loader = SteamItemRarityLoader(BaseService(SteamItemRarity))

    async def run(self):
        data = await self.extractor.process()
        transformed_data = await self.transformer.process(data)
        await self.loader.process(transformed_data)