from fastapi import FastAPI
from routers import matrics, logs, aws, ec2
app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utitlities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version="1.1.0",
    doc_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def hello():
    """
    This is a Hello API , just for testing
    """
    return {"message":"Hello Dosto, This is DevOps Utilites API"}

app.include_router(matrics.router)
app.include_router(logs.router)
app.include_router(aws.router, prefix="/aws")
app.include_router(ec2.router, prefix="/aws")