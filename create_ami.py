import boto3

ec2 = boto3.client("ec2")

response = ec2.create_image(InstanceId="i-003d9ce404ee877e3", Name="Test Ami")

print(response["ImageId"])