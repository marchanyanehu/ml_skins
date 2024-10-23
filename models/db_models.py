from sqlalchemy import Column, Integer, Float, String, Double, ForeignKey, BigInteger
from database.base_model import BaseModel


class ItemFullExport(BaseModel):
    __tablename__ = 'item_full_export'
    price = Column(Float, nullable=True)
    id = Column(BigInteger, primary_key=True)
    market_hash_name = Column(String, nullable=True)
    classid = Column(BigInteger, nullable=True)
    instanceid = Column(BigInteger, nullable=True)
    real_instance = Column(BigInteger, nullable=True)
    asset = Column(String, nullable=True)
    old_price = Column(Float, nullable=True)
    stamp = Column(String, nullable=True)
    base_id = Column(Integer, nullable=True)
    float = Column(Double, nullable=True)
    phase = Column(String, nullable=True)
    paintseed = Column(Integer, nullable=True)
    paintindex = Column(Integer, nullable=True)
    stickers = Column(String, nullable=True)
    type = Column(String, nullable=True)
    chance_to_transfer = Column(Float, nullable=True)


class Sticker(BaseModel):
    __tablename__ = 'sticker'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)