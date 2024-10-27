from etl.pipelines.tm_item_pipeline import ItemPipeline
from etl.pipelines.simple_item_pipeline import SimpleItemPipeline
from etl.pipelines.sticker_pipeline import StickerPipeline
from etl.pipelines.meta_item_pipeline import MetaItemPipeline
from utils.misc.export_as_csv import export_as_csv
from database.get_connection import get_db
from models.db_models import SimpleItem, ItemFullExport, Sticker, MetaItem, SteamItem, SteamItem7d, SteamItem14d, SteamItem30d, SteamItem90d, SteamItem365d
from apis.clients.hexaone_api_client import hexaone_client
from etl.pipelines.steam_item_pipeline import SteamItemPipeline

async def run_etl():
    field_mappings = {
        'price': 'price',
        'id': 'id',
        'market_hash_name': 'market_hash_name',
        'classid': 'classid',
        'instanceid': 'instanceid',
        'real_instance': 'real_instance',
        'asset': 'asset',
        'old_price': 'old_price',
        'stamp': 'stamp',
        'base_id': 'base_id',
        'float': 'float',
        'phase': 'phase',
        'paintseed': 'paintseed',
        'paintindex': 'paintindex',
        'stickers': 'stickers',
        'type': 'type',
        'chance_to_transfer': 'chance_to_transfer'
    }
    pipeline = ItemPipeline(field_mappings, batch_size=1000)
    await pipeline.run()


async def run_simple_item_etl():
    field_mappings = {
        'market_hash_name': 'market_hash_name',
        'volume': 'volume',
        'price': 'price'
    }
    pipeline = SimpleItemPipeline(field_mappings)
    await pipeline.run()

async def run_sticker_etl():
    field_mappings = {
        'id': 'id',
        'name': 'market_hash_name',
    }
    pipeline = StickerPipeline(field_mappings)
    await pipeline.run()


async def run_meta_item_etl():
    field_mappings = {
        'market_hash_name': 'market_hash_name',
        'popularity_7d': 'popularity_7d',
        'avg_price': 'avg_price'
    }
    pipeline = MetaItemPipeline(field_mappings)
    await pipeline.run()

async def run_steam_item_etl():
    pipeline = SteamItemPipeline()
    await pipeline.run()

def export_tables():
    steam_models = [SteamItem, SteamItem7d, SteamItem14d, SteamItem30d, SteamItem90d, SteamItem365d]
    ctm_models = [SimpleItem, ItemFullExport, Sticker, MetaItem]
    temp_model = [Sticker]
    with get_db() as session:
        for model in temp_model:
            export_as_csv(model, session)





if __name__ == "__main__":
    export_tables()

