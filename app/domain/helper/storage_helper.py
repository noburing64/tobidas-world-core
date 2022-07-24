import boto3
import config

# TODO: 削除予定
def save(image, file_path: str, type="storage"):
    def save_to_storage(image, file_path):
        with open(file_path, "wb") as fp:
            fp.write(image)
            
    def save_to_cloud(image, file_path):
        s3 = boto3.resource(
            service_name='s3',
            endpoint_url=config.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
            region_name=config.AWS_S3_REGION_NAME
        )
        bucket = s3.Bucket("develop")
        #bucket.Object(file_path).put(Body=image)
        bucket.upload_file(image, file_path)
    
    if type == "s3":
        return save_to_cloud(image, file_path)
    else:
        return save_to_storage(image, file_path)
    
def store(local_file_path: str, file_path: str, type="s3"):
    s3 = boto3.resource(
        service_name='s3',
        endpoint_url=config.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        region_name=config.AWS_S3_REGION_NAME
    )
    
    bucket = s3.Bucket("develop")
    bucket.upload_file(local_file_path, file_path)