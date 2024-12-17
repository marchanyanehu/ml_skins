from etl.pipelines.steam_item_pipeline import SteamItemPipeline
from fastapi import APIRouter
from etl.pipelines.steam_item_rarity_pipeline import SteamItemRarityPipeline

router = APIRouter(prefix="/etl/steam", tags=["ETL"])

@router.get("/run_etl_steam_item/")
async def run_steam_item_etl():
    pipeline = SteamItemPipeline()
    await pipeline.run()
    return {"message": "Steam Item ETL is running"}


@router.get("/run_etl_steam_item_rarity/")
async def run_steam_item_rarity_etl():
    field_mappings = {}  # Define any field mappings if necessary
    pipeline = SteamItemRarityPipeline(field_mappings)
    await pipeline.run()
    return {"message": "Steam Item Rarity ETL is running"}