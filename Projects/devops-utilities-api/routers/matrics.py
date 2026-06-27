from fastapi import APIRouter, HTTPException
from services.metrics_service import sys_health

router = APIRouter()

@router.get("/health",status_code=200)
def get_metrics():

    try:
        metrics = sys_health()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )