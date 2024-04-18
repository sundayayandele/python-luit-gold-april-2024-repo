import boto3

vpc_id="vpc-03fffdff48380622a"

ec2 = boto3.client("ec2")

ec2.delete_vpc(VpcId=vpc_id)