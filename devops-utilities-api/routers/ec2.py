from fastapi import APIRouter , HTTPException
from services.aws_service import get_ec2_info

router = APIRouter()
@router.get("/ec2", status_code=200)
def get_ec2_instances():
    """
        this api gets the list of EC2 instances in the AWS account.
    """
    try:
        ec2_instances = get_ec2_info()
    except:
        raise HTTPException(
            status_code=500,
              detail="Error retrieving EC2 information"
        )
    return ec2_instances