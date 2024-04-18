import boto3

cidrblock = "12.0.1.0/24"
vpc_id = "vpc-03fffdff48380622a"

ec2 = boto3.client("ec2")

subnet = ec2.create_subnet(CidrBlock=cidrblock, VpcId=vpc_id)

print(subnet["Subnet"]["SubnetId"])