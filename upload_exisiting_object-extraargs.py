import boto3

s3 = boto3.client("s3")

s3.upload_file("/home/ec2-user/environment/luit-gold-april-2024-repo/test_text.txt", "skhan-boto3-04152024", "test_text_upload.txt", ExtraArgs={"ContentType":"text/plain"})