from etl.pipelines.steam_item_pipeline import SteamItemPipeline
from fastapi import APIRouter

router = APIRouter(prefix="/etl/steam", tags=["ETL"])

@router.get("/run_etl_steam_item/")
async def run_steam_item_etl():
    pipeline = SteamItemPipeline()
    await pipeline.run()
    return {"message": "Steam Item ETL is running"}