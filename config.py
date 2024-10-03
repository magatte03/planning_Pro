import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL n'est pas définie dans le fichier .env")