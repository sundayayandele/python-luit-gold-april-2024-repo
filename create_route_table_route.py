import boto3

ig_id = "igw-0795a36e1ce4f944c"
route_table_id = "rtb-0a778a9783ca89391"

ec2 = boto3.client("ec2")

ec2.create_route(DestinationCidrBlock="0.0.0.0/0", GatewayId=ig_id, RouteTableId=route_table_id)


