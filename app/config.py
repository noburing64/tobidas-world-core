import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path=join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY=os.environ.get("SECRET_KEY", "secret")
API_DOMAIN=os.environ.get("API_BASE_URL", "api:8080")