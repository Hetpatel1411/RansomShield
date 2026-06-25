import psutil

print("=" * 70)
print("        RansomShield - Process Information")
print("=" * 70)

for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    try:
        print(f"Process Name : {process.info['name']}")
        print(f"PID          : {process.info['pid']}")
        print(f"CPU Usage    : {process.info['cpu_percent']} %")
        print(f"Memory Usage : {process.info['memory_percent']:.2f} %")
        print("-" * 70)

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass