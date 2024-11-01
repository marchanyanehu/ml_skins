from etl.pipelines import ItemPipeline, SimpleItemPipeline, StickerPipeline, MetaItemPipeline
from fastapi import APIRouter

router = APIRouter(prefix="/etl/cstm", tags=["ETL"])


@router.get("/run_etl_full_item/")
async def run_etl_full_item():
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
    return {"message": "Full Item ETL is running"}

@router.get("/run_etl_simple_item/")
async def run_simple_item_etl():
    field_mappings = {
        'market_hash_name': 'market_hash_name',
        'volume': 'volume',
        'price': 'price'
    }
    pipeline = SimpleItemPipeline(field_mappings)
    await pipeline.run()
    return {"message": "Simple Item ETL is running"}

@router.get("/run_etl_sticker/")
async def run_sticker_etl():
    field_mappings = {
        'id': 'id',
        'name': 'market_hash_name',
    }
    pipeline = StickerPipeline(field_mappings)
    await pipeline.run()
    return {"message": "Sticker ETL is running"}

@router.get("/run_etl_meta_item/")
async def run_meta_item_etl():
    field_mappings = {
        'market_hash_name': 'market_hash_name',
        'popularity_7d': 'popularity_7d',
        'avg_price': 'avg_price'
    }
    pipeline = MetaItemPipeline(field_mappings)
    await pipeline.run()
    return {"message": "Meta Item ETL is running"}