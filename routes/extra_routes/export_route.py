from models.db_models import SimpleItem, ItemFullExport, Sticker, MetaItem, SteamItem, SteamItem7d, SteamItem14d, SteamItem30d, SteamItem90d, SteamItem365d, SteamItemRarity
from database.get_connection import get_db
from utils.misc.export_as_csv import export_as_csv
from fastapi import APIRouter
from typing import Literal

STEAM_MODELS = [SteamItem, SteamItem7d, SteamItem14d, SteamItem30d, SteamItem90d, SteamItem365d]
CTM_MODELS = [SimpleItem, ItemFullExport, Sticker, MetaItem]
TEMP_MODELS = [SteamItemRarity]

router = APIRouter(prefix="/export", tags=["Export"])

@router.get("/export_steam/")
def export_tables(models_to_export: Literal['steam', 'cstm', 'temp']):
    if models_to_export == 'steam':
        model_list = STEAM_MODELS
    elif models_to_export == 'cstm':
        model_list = CTM_MODELS
    else:
        model_list = TEMP_MODELS
    with get_db() as session:
        for model in model_list:
            export_as_csv(model, session)

