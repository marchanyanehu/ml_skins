from etl.pipelines.item_pipeline import ItemPipeline

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

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_etl())