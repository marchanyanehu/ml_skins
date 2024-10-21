from apis.models.tm_api_model import TmApiV1Client, TmApiV2Client
from config import API_KEY


tm_v1_client = TmApiV1Client(api_key=API_KEY)
tm_v2_client = TmApiV2Client(api_key=API_KEY)

