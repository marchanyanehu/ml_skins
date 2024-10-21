from os import getenv


DB_HOST = getenv('DB_HOST', 'localhost')
DB_PORT = getenv('DB_PORT', '5432')
DB_USER = getenv("DB_USER", "postgres")
DB_NAME = getenv("DB_NAME", "ml_skins")
DB_PASSWORD = getenv("DB_PASSWORD", "postgres")

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

API_KEY = getenv("API_KEY", "your_api_key_here")


