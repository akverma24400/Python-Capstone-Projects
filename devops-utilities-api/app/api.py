from fastapi import FastAPI
from routers import metrics,aws,ec2

app = FastAPI(
    title="DevOps Utilities API",
    description="A collection of DevOps utilities for automation and management.",
    version="1.1.0",
    doc_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def hello():
    """
    this is a simple endpoint that returns a greeting message. It serves as a health check for the API and confirms that the service is running correctly.
    """
    return {"message": "Hello, DevOps Utilities API!"}


app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")
app.include_router(ec2.router, prefix="/aws")





