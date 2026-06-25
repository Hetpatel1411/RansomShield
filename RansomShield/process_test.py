import psutil

print("=" * 90)
print("               RansomShield - Running Process Monitor")
print("=" * 90)

for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    try:
        print(
            f"Process : {process.info['name']:<30}"
            f"PID : {process.info['pid']:<8}"
            f"CPU : {process.info['cpu_percent']:>5}%   "
            f"RAM : {process.info['memory_percent']:.2f}%"
        )

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass

print("=" * 90)