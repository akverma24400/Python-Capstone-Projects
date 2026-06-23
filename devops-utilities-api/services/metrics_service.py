import psutil

def get_system_metrics():

    """
        this api gets the system metrics like cpu usage, memory usage and disk usage. It uses the psutil library to get the system metrics and returns them in a dictionary format. The function also checks if the cpu usage, memory usage or disk usage is above a certain threshold and returns a status message accordingly.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory().percent
    disk_info = psutil.disk_usage('/').percent

    threshold = 20  # Define a threshold for high usage
    if cpu_usage > threshold or memory_info > threshold or disk_info > threshold:
        return {
            "cpu_usage": cpu_usage,
            "memory_info": memory_info,
            "disk_info": disk_info,
            "threshold": threshold,
            "status": "High usage detected"
        }