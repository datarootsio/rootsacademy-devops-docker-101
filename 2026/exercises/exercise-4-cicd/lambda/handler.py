import json
import os

import boto3


def handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "world") if event.get("queryStringParameters") else "world"

    # TODO: count the objects in the S3 bucket named by the BUCKET_NAME
    # environment variable, and put the count in the response as
    # "file_count". Hint: boto3.client("s3").list_objects_v2(Bucket=...) —
    # an empty bucket's response has no "Contents" key at all.
    bucket_name = os.environ.get("BUCKET_NAME")
    response = boto3.client("s3").list_objects_v2(Bucket=bucket_name)
    if "Contents" in response:
        file_count = len(response["Contents"])
    else:
        file_count = 0
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"hello, {name}",
        "file_count": file_count}),
    }
