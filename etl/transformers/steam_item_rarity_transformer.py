from etl.transformers.base_transformer import BaseTransformer
from typing import List, Dict, Any

class SteamItemRarityTransformer(BaseTransformer):
    def __init__(self, field_mappings: Dict[str, str]):
        self.field_mappings = field_mappings

    def transform(self, items: Dict[str, Any]) -> List[Dict[str, Any]]:
        transformed_data = []
        for market_hash_name, item in items.items():
            transformed_item = {}
            transformed_item['market_hash_name'] = market_hash_name
            # Extract rarity from tags
            rarity = None
            for tag in item.get('tags', []):
                if tag.get('category') == 'Rarity':
                    rarity = tag.get('name')
                    break
            transformed_item['rarity'] = rarity
            transformed_data.append(transformed_item)
        return transformed_data

    async def process(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        return self.transform(data)