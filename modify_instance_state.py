import boto3

instance_id = "i-0f984011e1d74a485"

def stop_instance(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, "stopped.")
    
def start_instance(client, instance_id):
    response = client.start_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, "started.")

def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, "terminated.")

if __name__ == "__main__":
    instance_id = "i-003d9ce404ee877e3"

    ec2 = boto3.client("ec2")
    terminate_instance(ec2, instance_id)