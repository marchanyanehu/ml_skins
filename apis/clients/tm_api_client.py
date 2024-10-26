from apis.models.tm_api_model import TmApiV1Model, TmApiV2Model
from config import CTM_API_KEY



tm_v1_client = TmApiV1Model(api_key=CTM_API_KEY)
tm_v2_client = TmApiV2Model(api_key=CTM_API_KEY)

