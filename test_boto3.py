import boto3 # imports the boto3 library into the Python file

#s3 = boto3.client("s3", aws_access_key_id="", aws_secret_access_key="", aws_session_token="") #This is a way to hard-code into your code. Not recommended

session = boto3.Session()

s3 = boto3.client("s3")
s3 = session.client("s3")

