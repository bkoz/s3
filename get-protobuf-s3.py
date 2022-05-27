"""
File: get-protobuf-s3.py

Download a protobuf model from S3 storage.

Required environment variables that need to be set:
    S3_REGION,
    S3_ACCESS_KEY_ID, 
    S3_SECRET_ACCESS_KEY
    S3_BUCKET

Date: May 27, 2022
"""
import tensorflow as tf
import boto3
import logging
import os

logging.basicConfig(level=logging.INFO)

def downloadDirectoryFromS3(bucketName: str, remoteDirectoryName: str) -> None:
    """
    Download a directory from S3 storage by iterating through
    the bucket objects associated with a remote folder. The
    remote directory structure is preserved.

    Required environment variables that need to be set:
    S3_REGION,
    S3_ACCESS_KEY_ID, 
    S3_SECRET_ACCESS_KEY

    Args:
    bucketName: str - The name of the S3 bucket.
    remoteDirectoryName: str - The name of the remote directory (folder) to download.
    """
    s3_resource = boto3.resource(
        's3', 
        region_name=os.environ['S3_REGION'], 
        aws_access_key_id=os.environ['S3_ACCESS_KEY_ID'], 
        aws_secret_access_key=os.environ['S3_SECRET_ACCESS_KEY']
        )
    bucket = s3_resource.Bucket(bucketName) 
    for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key) # save to same path

if __name__ == "__main__":

    logging.info(f'Tensorflow version: {tf.__version__}')
    logging.info(f"S3_REGION: {os.environ['S3_REGION']}")
    logging.info(f"S3_ACCESS_KEY_ID: {os.environ['S3_ACCESS_KEY_ID']}")
    logging.info(f"S3_BUCKET: {os.environ['S3_BUCKET']}")
    remote_folder = "models/vitals_simple/1651022813/"
    logging.info(f"Downloading s3://{os.environ['S3_BUCKET']}/{remote_folder}")
    downloadDirectoryFromS3(os.environ['S3_BUCKET'], remote_folder)

    # Load, print and make a prediction.
    loaded_model = tf.keras.models.load_model(remote_folder)
    loaded_model.summary()
    logging.info(f'Prediction: {loaded_model((tf.constant([60]), tf.constant([18]), tf.constant([98.6])))}')