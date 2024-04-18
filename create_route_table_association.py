import boto3

route_table_id = "rtb-0a778a9783ca89391"
subnet_id = "subnet-043d702d40e897e0e"

ec2 = boto3.client("ec2")

association = ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)

print(association["AssociationId"])