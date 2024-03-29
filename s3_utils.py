"""
Basic S3 operations.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#s3
"""

import logging
import os
import boto3
from botocore.exceptions import ClientError

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def list_buckets(region=None):
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
    
def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(f'create_bucket(): {e}')
        return False
    return True

def delete_bucket(bucket):
    s3 = boto3.client('s3')
    response = s3.delete_bucket(Bucket=bucket)
    
def download_file(bucket, file_name, object_name):
    s3 = boto3.client('s3')
    s3.download_file(bucket, object_name, file_name)

def delete_file(bucket, file_name):
    s3 = boto3.client('s3')
    try:
        response = s3.delete_object(Bucket=bucket, Key=file_name)
    except ClientError as e:
            logging.error(f'delete_file(): {e}')
            return False
    return True
    
if __name__ == '__main__':
    bucket = 'bk-mybucket'
    file_name = 'data.txt'
    list_buckets(os.environ['AWS_REGION'])
    r_val = create_bucket(bucket, os.environ['AWS_REGION'])
    upload_file(file_name, bucket, object_name=None)
    download_file(bucket, file_name, object_name=file_name)
    # delete_file(bucket, file_name)
    # delete_bucket(bucket)
