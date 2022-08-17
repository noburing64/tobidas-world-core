import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path=join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY=os.environ.get("SECRET_KEY", "secret")
API_DOMAIN=os.environ.get("API_BASE_URL", "api:8080")
AWS_S3_ENDPOINT_URL=os.environ.get("AWS_S3_ENDPOINT_URL", "localhost")
AWS_S3_REGION_NAME=os.environ.get("S3_REGION_NAME", "")
AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY", "")
GCP_CREDENTIAL_KEY_PATH=os.environ.get("GCP_CREDENTIAL_KEY_PATH", "")
GCP_PROJECT_NAME=os.environ.get("GCP_PROJECT_NAME", "")
GCP_STORAGE_BUCKET_NAME=os.environ.get("GCP_STORAGE_BUCKET_NAME", "")