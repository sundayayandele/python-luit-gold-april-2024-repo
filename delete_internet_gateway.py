import boto3

internet_gateway_id = "igw-0795a36e1ce4f944c"

ec2 = boto3.client("ec2")

ec2.delete_internet_gateway(InternetGatewayId=internet_gateway_id)