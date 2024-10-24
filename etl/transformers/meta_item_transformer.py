from etl.transformers.base_transformer import BaseTransformer
from typing import List, Dict, Any

class MetaItemTransformer(BaseTransformer):
    def __init__(self, field_mappings: Dict[str, str]):
        self.field_mappings = field_mappings

    def transform(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        transformed_data = []
        for item in data:
            transformed_item = {
                'market_hash_name': item['market_hash_name'],
                'popularity_7d': int(item['popularity_7d']) if item['popularity_7d'] is not None else 0,
                'avg_price': float(item['avg_price']) if item['avg_price'] is not None else 0.0,
            }
            transformed_data.append(transformed_item)
        return transformed_data

    async def process(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return self.transform(batch)
