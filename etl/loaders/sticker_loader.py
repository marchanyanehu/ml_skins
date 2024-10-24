from etl.loaders.base_loader import BaseLoader
from typing import List, Dict, Any
from services.base_service import BaseService
from sqlalchemy.exc import IntegrityError

class StickerLoader(BaseLoader):
    def __init__(self, service: BaseService):
        self.service = service

    def load(self, data: List[Dict[str, Any]]) -> None:
        try:
            self.service.bulk_add_items(data)
        except IntegrityError:
            # Handle duplicate entries if necessary
            for item in data:
                try:
                    self.service.add_item(item)
                except IntegrityError:
                    # Log or handle individual duplicate entries
                    pass

    async def process(self, data: List[Dict[str, Any]]) -> None:
        self.load(data)