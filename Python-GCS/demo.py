import os
from google.cloud import storage
from google.cloud.storage import bucket

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

# dir(storage_client)
# Create new bucket
bucket_name = 'asapcapstoneapi'
bucket = storage_client.bucket(bucket_name)
bucket.location = 'us-central1'
storage_client.create_bucket(bucket)
# print bucket details
vars(bucket)

# get bucket instance accesing a specific bucket
my_bucket = storage_client.get_bucket('asapcapstoneapi')

# upload files
def upload_file_to_bucket(blob_name,file_path, bucket_name):
    try:
        bucket= storage_client.get_bucket(bucket_name)
        blob= bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

file_path = r'C:\Users\ASUS\Desktop\upload_bucket'
upload_file_to_bucket('input_list_1', os.path.join(file_path, '1.jpg'), 'asapcapstoneapi')
upload_file_to_bucket('document/input_list_2', os.path.join(file_path, '2.jpg'), 'asapcapstoneapi')

# download files
def download_file_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False

bucket_name ='asapcapstoneapi'
download_file_from_bucket('input_list_1',os.path.join(os.getcwd(),'file1.jpg'), bucket_name)
download_file_from_bucket('document/input_list_2', os.path.join(file_path, '2.jpg'), 'asapcapstoneapi')


# Download File By Passing URI Path

def download_file_uri(uri, file_path):
    with open(file_path, 'wb') as f:
        storage_client.download_blob_to_file(uri, f)
    print('Saved')

uri = 'gs://<uri>'

# List Buckets
# list_buckets(max_results=None, page_token=None, prefix=None, projection='noAcl', fields=None, project=None, timeout=60, retry=<google.api_core.retry.Retry object>)

for bucket in storage_client.list_buckets(max_results=100):
    print(bucket)