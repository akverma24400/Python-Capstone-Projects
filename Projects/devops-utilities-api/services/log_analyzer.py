from collections import Counter

def analyze_logs(file_path=r"C:\Users\akver\OneDrive\Desktop\Capstone-Projects\Python-Capstone-Projects\Projects\devops-utilities-api\app.log"):
    counts = Counter()
    try:
        with open(file_path, "r") as file:
            for line in file:
                if "INFO" in line:
                    counts["INFO"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "ERROR" in line:
                    counts["ERROR"] += 1

        return{
            "Status":"success",
            "Summery": dict(counts)
        }
    except FileNotFoundError:
        return{
            "Status":"Failed",
            "message": "log file not found"
        }