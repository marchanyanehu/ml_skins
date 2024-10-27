from database.get_connection import get_db
from models.db_models import SteamItem, SteamItem7d, SteamItem14d, SteamItem30d, SteamItem90d, SteamItem365d
from apis.clients.hexaone_api_client import hexaone_client
from sqlalchemy.exc import IntegrityError

class SteamItemPipeline:
    def __init__(self):
        self.client = hexaone_client

    async def run(self):
        response = await self.client.get_market_prices()
        prices = response['result']['prices']
        
        with get_db() as db:
            for item_name, periods in prices.items():
                steam_item = db.query(SteamItem).filter(SteamItem.market_hash_name == item_name).first()
                if not steam_item:
                    steam_item = SteamItem(market_hash_name=item_name)
                    db.add(steam_item)
                    db.commit()

                for period, data in periods.items():
                    model_class = self.get_model_class(period)
                    if model_class:
                        self.upsert_item(db, model_class, item_name, data)

    def get_model_class(self, period):
        model_classes = {
            '7': SteamItem7d,
            '14': SteamItem14d,
            '30': SteamItem30d,
            '90': SteamItem90d,
            '365': SteamItem365d
        }
        return model_classes.get(period)

    def upsert_item(self, db, model_class, item_name, data):
        item = db.query(model_class).filter(model_class.market_hash_name == item_name).first()
        if item:
            item.avg_price = data['avg']
            item.max_price = data['max']
            item.median_price = data['med']
            item.min_price = data['min']
            item.std = data['std']
            item.volume = data['sales']
        else:
            item = model_class(
                market_hash_name=item_name,
                avg_price=data['avg'],
                max_price=data['max'],
                median_price=data['med'],
                min_price=data['min'],
                std=data['std'],
                volume=data['sales']
            )
            db.add(item)
        db.commit()