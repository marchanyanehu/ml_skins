from sqlalchemy import Column, Integer, Float, String, Double, ForeignKey
from database.base_model import BaseModel


class ItemFullExport(BaseModel):
    __tablename__ = 'item_full_export'
    
    price = Column(Float)
    id = Column(Integer, primary_key=True)
    market_hash_name = Column(String)
    classid = Column(String)
    instanceid = Column(String)
    real_instance = Column(String)
    asset = Column(String)
    old_price = Column(Float)
    stamp = Column(String)
    base_id = Column(Integer)
    float = Column(Double)
    phase = Column(Integer)
    paintseed = Column(Integer)
    paintindex = Column(Integer)
    stickers = Column(String)
    type = Column(String)
    chance_to_transfer = Column(Float)


class Sticker(BaseModel):
    __tablename__ = 'sticker'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)