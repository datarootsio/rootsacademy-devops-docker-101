import json
import os

import boto3


def handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "world") if event.get("queryStringParameters") else "world"

    bucket_name = os.environ["BUCKET_NAME"]
    s3 = boto3.client("s3")

    file_count = 0
    continuation_token = None
    while True:
        kwargs = {"Bucket": bucket_name}
        if continuation_token:
            kwargs["ContinuationToken"] = continuation_token

        response = s3.list_objects_v2(**kwargs)
        file_count += len(response.get("Contents", []))

        if response.get("IsTruncated"):
            continuation_token = response["NextContinuationToken"]
        else:
            break

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"hello, {name}", "file_count": file_count}),
    }