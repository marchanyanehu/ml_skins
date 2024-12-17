from sqlalchemy import Column, Integer, Float, String, Double, ForeignKey, BigInteger, Index, Boolean
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
    avg_price = Column(Float, nullable=True)


class Sticker(BaseModel):
    __tablename__ = 'sticker'
    
    id = Column(BigInteger, primary_key=True)
    market_hash_name = Column(String)
    avg_price = Column(Float)


class SimpleItem(BaseModel):
    __tablename__ = 'simple_item'

    market_hash_name = Column(String, primary_key=True)
    volume = Column(Integer, nullable=True)
    price = Column(Float, nullable=True)  


class MetaItem(BaseModel):
    __tablename__ = 'meta_item'

    market_hash_name = Column(String, primary_key=True)
    popularity_7d = Column(Integer, nullable=True)
    avg_price = Column(Float, nullable=True)

    __table_args__ = (
        Index('ix_meta_item_market_hash_name', 'market_hash_name', postgresql_using='hash'),
    )




class SteamItem(BaseModel):
    __tablename__ = 'steam_item'

    market_hash_name = Column(String, primary_key=True)
    _7d = Column(Boolean)
    _14d = Column(Boolean)
    _30d = Column(Boolean)
    _90d = Column(Boolean)
    _365d = Column(Boolean)


class SteamItem7d(BaseModel):
    __tablename__ = 'steam_item_7d'

    market_hash_name = Column(String, ForeignKey('steam_item.market_hash_name'), primary_key=True)
    avg_price = Column(Float) # avg as in api response
    max_price = Column(Float) # max 
    median_price = Column(Float) # med 
    min_price = Column(Float) # min 
    std = Column(Float) # std as in api response
    volume = Column(Integer) # sales 

    Index('ix_steam_item_7d_market_hash_name', 'market_hash_name', postgresql_using='hash')


class SteamItem14d(BaseModel):
    __tablename__ = 'steam_item_14d'

    market_hash_name = Column(String, ForeignKey('steam_item.market_hash_name'), primary_key=True)
    avg_price = Column(Float) # avg as in api response
    max_price = Column(Float) # max 
    median_price = Column(Float) # med 
    min_price = Column(Float) # min 
    std = Column(Float) # std as in api response
    volume = Column(Integer) # sales 

    Index('ix_steam_item_14d_market_hash_name', 'market_hash_name', postgresql_using='hash')


class SteamItem30d(BaseModel):
    __tablename__ = 'steam_item_30d'

    market_hash_name = Column(String, ForeignKey('steam_item.market_hash_name'), primary_key=True)
    avg_price = Column(Float) # avg as in api response
    max_price = Column(Float) # max 
    median_price = Column(Float) # med 
    min_price = Column(Float) # min 
    std = Column(Float) # std as in api response
    volume = Column(Integer) # sales 

    Index('ix_steam_item_30d_market_hash_name', 'market_hash_name', postgresql_using='hash')


class SteamItem90d(BaseModel):
    __tablename__ = 'steam_item_90d'

    market_hash_name = Column(String, ForeignKey('steam_item.market_hash_name'), primary_key=True)
    avg_price = Column(Float) # avg as in api response
    max_price = Column(Float) # max 
    median_price = Column(Float) # med 
    min_price = Column(Float) # min 
    std = Column(Float) # std as in api response
    volume = Column(Integer) # sales 

    Index('ix_steam_item_90d_market_hash_name', 'market_hash_name', postgresql_using='hash')


class SteamItem365d(BaseModel):
    __tablename__ = 'steam_item_365d'

    market_hash_name = Column(String, ForeignKey('steam_item.market_hash_name'), primary_key=True)
    avg_price = Column(Float) # avg as in api response
    max_price = Column(Float) # max 
    median_price = Column(Float) # med 
    min_price = Column(Float) # min 
    std = Column(Float) # std as in api response
    volume = Column(Integer) # sales 

    Index('ix_steam_item_365d_market_hash_name', 'market_hash_name', postgresql_using='hash')



class SteamItemRarity(BaseModel):
    __tablename__ = 'steam_item_rarity'

    market_hash_name = Column(String, primary_key=True)
    rarity = Column(String, nullable=True)

    Index('ix_steam_item_rarity_market_hash_name', 'market_hash_name', postgresql_using='hash')

