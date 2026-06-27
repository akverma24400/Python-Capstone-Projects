import psutil

def sys_health():
    """
        This API gets the System Metrics(CPU, Memory, Disk, System Health)
        Based on a CPU Threshold i.e 10 (Configurable)
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    cpu_threshold = 20

    status = "HIGH CPU" if cpu_percent > cpu_threshold else "Healthy..."

    return{
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent" : disk_percent,
        "System_Status": status
    }