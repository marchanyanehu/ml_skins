from etl.loaders.base_loader import BaseLoader
from services.base_service import BaseService
from models.db_models import MetaItem, SimpleItem
from sqlalchemy.exc import IntegrityError
from typing import List, Dict, Any
from database.get_connection import get_db

class MetaItemLoader(BaseLoader):
    def __init__(self, service: BaseService):
        self.service = service
        self.simple_item_service = BaseService(SimpleItem)

    def load(self, data: List[Dict[str, Any]]) -> None:
        for item in data:
            try:
                # Use a session context to ensure the item is loaded and updated within the same session
                with get_db() as db:
                    existing_item = db.query(MetaItem).filter(MetaItem.market_hash_name == item['market_hash_name']).first()
                    if existing_item:
                        total_popularity = existing_item.popularity_7d + item['popularity_7d']
                        if total_popularity > 0:
                            weighted_avg_price = (
                                (existing_item.avg_price * existing_item.popularity_7d) + 
                                (item['avg_price'] * item['popularity_7d'])
                            ) / total_popularity
                            existing_item.popularity_7d = total_popularity
                            existing_item.avg_price = weighted_avg_price
                            db.commit()
                    else:
                        # Check if the item exists in the SimpleItem table
                        simple_item = db.query(SimpleItem).filter(SimpleItem.market_hash_name == item['market_hash_name']).first()
                        if simple_item:
                            new_item = MetaItem(**item)
                            db.add(new_item)
                            db.commit()
            except IntegrityError:
                # Log or handle individual duplicate entries
                pass

    async def process(self, data: List[Dict[str, Any]]) -> None:
        self.load(data)
