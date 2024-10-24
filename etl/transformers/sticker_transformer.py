from etl.transformers.base_transformer import BaseTransformer
from typing import List, Dict, Any

class StickerTransformer(BaseTransformer):
    def __init__(self, field_mappings: Dict[str, str]):
        self.field_mappings = field_mappings

    def transform(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        transformed_batch = []
        for item in batch:
            transformed_item = {}
            for field, mapped_field in self.field_mappings.items():
                value = item.get(field, None)
                if value == '':
                    value = None
                transformed_item[mapped_field] = value
            transformed_batch.append(transformed_item)
        return transformed_batch

    async def process(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return self.transform(batch)