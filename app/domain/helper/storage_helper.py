import boto3

# TODO: 削除予定
def save(image, file_path: str, type="storage"):
    def save_to_storage(image, file_path):
        with open(file_path, "wb") as fp:
            fp.write(image)
            
    def save_to_cloud(image, file_path):
        # TODO: resourceを使う
        # s3 = boto3.client('s3',
        #     aws_access_key_id='',
        #     aws_secret_access_key='',
        #     region_name='ap-northeast-1'
        # )
        # waiter = s3.get_waiter('object_exists')
        # waiter.wait(Bucket='test_bucket', Key='NewObject.txt')
        pass
    
    if type == "s3":
        return save_to_cloud(image, file_path)
    else:
        return save_to_storage(image, file_path)
    
def store(local_file_path: str, file_path: str, type="s3"):
    pass