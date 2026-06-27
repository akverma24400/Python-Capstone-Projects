import boto3
from datetime import datetime, timezone, timedelta

def get_bucket_info():
    s3_client = boto3.client("s3")

    buckets = s3_client.list_buckets()["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()
    new_buckets = []
    old_buckets = []
    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_date - timedelta(days=90)
        if creation_date < days_ago_90:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return {
        "total_buckets":len(buckets),
        "new_buckets":len(new_buckets),
        "old_buckets":len(old_buckets),
        "new_buckets_names":new_buckets,
        "old_buckets_names":old_buckets
    }

def get_ec2_info():
    ec2 = boto3.client("ec2")

    # Get all available regions
    regions = [region["RegionName"] for region in ec2.describe_regions()["Regions"]]

    instances_info = []

    for region in regions:
        ec2_resource = boto3.resource("ec2", region_name=region)

        for instance in ec2_resource.instances.all():

            # Get Name tag
            instance_name = "No Name"
            if instance.tags:
                for tag in instance.tags:
                    if tag["Key"] == "Name":
                        instance_name = tag["Value"]
                        break

            instances_info.append({
                "name": instance_name,
                "instance_id": instance.id,
                "region": region,
                "status": instance.state["Name"]
            })

    return {
        "total_instances": len(instances_info),
        "instances": instances_info
    }
