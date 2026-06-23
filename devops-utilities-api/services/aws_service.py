import boto3
from datetime import datetime, timezone

def get_bucket_info():
    """
        this api gets the list of buckets in the AWS account. 
        It uses the boto3 library to get the list of buckets and returns them in a dictionary format.
    """
    s3_client = boto3.client('s3')
    buckets = s3_client.list_buckets()['Buckets']
    old_buckets = []
    new_buckets = []
    current_date = datetime.now(timezone.utc)  # Get the current date and time in UTC
    print(f"Current time: {current_date}")  # Debugging line to check current time
    for bucket in buckets:
        bucket_name = bucket['Name']
        creation_date = bucket['CreationDate']
        # Check if the bucket is older than 30 days
        if (current_date - creation_date).days > 2:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return{
        "total_buckets": len(buckets),
        "new_buckets": len(new_buckets),
        "new_buckets_names": new_buckets,
        "old_buckets": len(old_buckets),
        "old_buckets_names": old_buckets
    }

def get_ec2_info():
    """"
        This Api gets the list of EC2 instances in the AWS account along with their region and status.
        It uses the boto3 library to get the list of EC2 instances and returns them in a dictionary format.
    """
    ec2_client = boto3.client('ec2')
    regions = ec2_client.describe_regions()['Regions']
    instances_info = []
    for region in regions:
        region_name = region['RegionName']
        ec2_client_region = boto3.client('ec2', region_name=region_name)
        instances = ec2_client_region.describe_instances()['Reservations']
        for reservation in instances:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']

                instance_name = "N/A"
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']
                        break
                    
                instances_info.append({
                    "instance_id": instance_id,
                    "region": region_name,
                    "status": instance_state,
                    "name": instance_name
                })
    return {
        "total_instances": len(instances_info),
        "instances_info": instances_info
    }
