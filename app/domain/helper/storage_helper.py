import boto3
import config
from google.cloud import storage as gcs
from google.oauth2 import service_account

# TODO: 削除予定
def save(image, file_path: str, type="storage"):
    def save_to_storage(image, file_path):
        with open(file_path, "wb") as fp:
            fp.write(image)
    return save_to_storage(image, file_path)
    
def store(local_file_path: str, file_path: str, type="s3"):
    if config.GCP_CREDENTIAL_KEY_PATH != '':
        credential = service_account.Credentials.from_service_account_file(config.GCP_CREDENTIAL_KEY_PATH)
        client = gcs.Client(config.GCP_PROJECT_NAME, credentials=credential)
        bucket = client.get_bucket(config.GCP_STORAGE_BUCKET_NAME)
        blob_gcs = bucket.blob(file_path)
        blob_gcs.upload_from_filename(local_file_path)
    else:
        if config.GCP_STORAGE_HOST_NAME != '':
            client = gcs.Client()
            bucket = client.get_bucket(config.GCP_STORAGE_BUCKET_NAME)
            blob_gcs = bucket.blob(file_path)
            blob_gcs.upload_from_filename(local_file_path)
        else:
            s3 = boto3.resource(
                service_name='s3',
                endpoint_url=config.AWS_S3_ENDPOINT_URL,
                aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
                region_name=config.AWS_S3_REGION_NAME
            )
            
            bucket = s3.Bucket("develop")
            bucket.upload_file(local_file_path, file_path)