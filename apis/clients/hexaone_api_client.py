from config import HEXAONE_API_KEY
from apis.models.hexaone_api_model import HexaOneApiModel


hexaone_client = HexaOneApiModel(api_key=HEXAONE_API_KEY)
