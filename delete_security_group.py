import boto3

ec2 = boto3.client("ec2")

response = ec2.delete_security_group(GroupId="sg-01f5599470a34aed9")