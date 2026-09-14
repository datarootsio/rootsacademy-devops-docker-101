import json
import os

import boto3


def handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "world") if event.get("queryStringParameters") else "world"

    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=os.environ["BUCKET_NAME"])
    file_count = len(response.get("Contents", []))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"hello, {name}", "file_count": file_count}),
    }
