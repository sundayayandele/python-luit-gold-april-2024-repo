import boto3

s3 = boto3.client("s3")

response = s3.create_bucket(
    Bucket="skhan-boto3-04152024"
)

print(response)