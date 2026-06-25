import psutil

print("=" * 50)
print("Running Python Processes")
print("=" * 50)

for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    try:
        if "python" in process.info['name'].lower():
            print(f"PID         : {process.info['pid']}")
            print(f"Process     : {process.info['name']}")
            print(f"CPU Usage   : {process.info['cpu_percent']}%")
            print(f"Memory Usage: {process.info['memory_percent']:.2f}%")
            print("-" * 50)

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass