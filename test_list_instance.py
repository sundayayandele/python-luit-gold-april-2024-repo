import boto3



def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, "terminated.")
    

ec2 = boto3.client("ec2")
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        #if instance["State"]["Name"] != "terminated":# and instance["InstanceId"] != "i-09422a8475098c699":
            #print(instance["InstanceId"], instance["State"]["Name"])
            #terminate_instance(ec2, instance["InstanceId"])
            #if "Tags" in instance:
                #if instance["Tags"]["Key"] == "Dev":
            if "Tags" in instance:
                #tags = instance["Tags"]
                for tag in instance["Tags"]:
                    if tag["Key"] == "Environment: Dev" and instance["State"]["Name"] != "terminated":
                        #print(instance["InstanceId"], tag["Value"])#, #instance["Tags"]["Value"])
                        terminate_instance(ec2, instance["InstanceId"])