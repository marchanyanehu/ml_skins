from etl.transformers.base_transformer import BaseTransformer
from typing import List, Dict, Any

class ItemTransformer(BaseTransformer):
    def __init__(self, field_mappings: Dict[str, str]):
        self.field_mappings = field_mappings

    def transform(self, batch: List[List[Any]], format: List[str]) -> List[Dict[str, Any]]:
        transformed_batch = []
        for item in batch:
            transformed_item = {}
            for i, field in enumerate(format):
                if field in self.field_mappings:
                    value = item[i]
                    if value == '':
                        value = None
                    transformed_item[self.field_mappings[field]] = value
            transformed_batch.append(transformed_item)
        return transformed_batch

    async def process(self, batch: List[List[Any]], format: List[str]) -> List[Dict[str, Any]]:
        return self.transform(batch, format)
