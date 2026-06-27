from fastapi import APIRouter, HTTPException
from services.log_analyzer import analyze_logs

router = APIRouter()

@router.get("/logs",status_code=200)
def get_metrics():

    try:
        logs = analyze_logs()
        return logs
    except:
        raise HTTPException(
            status_code=500,
            detail="Logs Not Found..."
        )