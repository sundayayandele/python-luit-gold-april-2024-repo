import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_security_groups()

for sg in response["SecurityGroups"]:
    print(sg["GroupId"], sg["VpcId"], sg["GroupName"], sg["Description"])
    
    if "IpPermissions" in sg:
        for permission in sg["IpPermissions"]:
            if "FromPort" in permission:
                print(permission["FromPort"])
            
            if "IpProtocol" in permission:
                print(permission["IpProtocol"])
                
            if "ToPort" in permission:
                print(permmission["ToPort"])
            
            if "IpRange" in permission:
                for iprange in permission["IpRange"]:
                    print(iprange["CidrIp"])
    
