import json
import boto3

def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, "terminated.")
    
def terminate_instances(client):
    response = client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Environment: Dev" and instance["State"]["Name"] != "terminated":
                        terminate_instance(client, instance["InstanceId"])

def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    terminate_instances(ec2)