from etl.pipelines.tm_item_pipeline import ItemPipeline
from etl.pipelines.simple_item_pipeline import SimpleItemPipeline
from etl.pipelines.sticker_pipeline import StickerPipeline
from etl.pipelines.meta_item_pipeline import MetaItemPipeline

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
        'name': 'name',
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

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_meta_item_etl())
