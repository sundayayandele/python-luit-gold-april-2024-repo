import boto3

vpc_id = "vpc-03fffdff48380622a"
internet_gateway_id = "igw-0795a36e1ce4f944c"

ec2 = boto3.client("ec2")

ec2.detach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId = vpc_id)