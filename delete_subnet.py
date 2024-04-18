import boto3

subnet_id = "subnet-043d702d40e897e0e"

ec2 = boto3.client("ec2")

ec2.delete_subnet(SubnetId=subnet_id)