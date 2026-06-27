from fastapi import APIRouter, HTTPException
from services.aws_service import get_cost_info

router = APIRouter()

@router.get("/cost",status_code=200)
def get_instances():

    try:
        return get_cost_info()
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error..."
        )