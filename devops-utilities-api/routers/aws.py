from fastapi import APIRouter , HTTPException
from services.aws_service import get_bucket_info

router = APIRouter()
@router.get("/s3", status_code=200)
def get_buckets():
    """
        this api gets the list of buckets in the AWS account.
    """
    try:
        buckets = get_bucket_info()
    except:
        raise HTTPException(
            status_code=500,
              detail="Error retrieving bucket information"
        )
    return buckets