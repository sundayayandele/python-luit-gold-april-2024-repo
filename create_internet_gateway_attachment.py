import boto3

internet_gateway_id = "igw-0795a36e1ce4f944c"
vpc_id = "vpc-03fffdff48380622a"

ec2 = boto3.client("ec2")

ec2.attach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)