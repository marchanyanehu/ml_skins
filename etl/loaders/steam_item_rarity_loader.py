from etl.loaders.base_loader import BaseLoader
from typing import List, Dict, Any
from services.base_service import BaseService
from sqlalchemy.exc import IntegrityError

class SteamItemRarityLoader(BaseLoader):
    def __init__(self, service: BaseService):
        self.service = service

    def load(self, data: List[Dict[str, Any]]) -> None:
        try:
            self.service.bulk_add_items(data)
        except IntegrityError:
            for item in data:
                try:
                    self.service.add_item(item)
                except IntegrityError:
                    pass  # Handle duplicates if necessary

    async def process(self, data: List[Dict[str, Any]]) -> None:
        self.load(data)