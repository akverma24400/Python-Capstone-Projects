from fastapi import APIRouter , HTTPException
from services.metrics_service import get_system_metrics

router = APIRouter()
@router.get("/metrics", status_code=200)
def get_metrics():
    """
        this api gets the system metrics like cpu usage, memory usage and disk usage.
        It uses the psutil library to get the system metrics and returns them in a dictionary format. 
        The function also checks if the cpu usage, AWS usage, memory usage or disk usage is above a certain threshold and returns
        a status message accordingly.
    """
    try:
        return get_system_metrics()
    except:
        raise HTTPException(
            status_code=500,
              detail="Error retrieving system metrics"
        )       