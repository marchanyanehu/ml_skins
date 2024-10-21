from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL

class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_engine(DB_URL)
            cls._instance.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._instance.engine)
        return cls._instance

    def get_session(self):
        return self.SessionLocal()

db = DatabaseSingleton()