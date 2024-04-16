import boto3

s3 = boto3.client("s3")

with open("/home/ec2-user/environment/luit-gold-april-2024-repo/test_text.txt", "rb") as f:
    s3.put_object(Bucket="skhan-boto3-04152024", Key="test_text.txt", Body=f, ContentType="text/plain")