from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import psutil
from datetime import datetime
from plyer import notification

alert_triggered = False
modification_times = []


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        global modification_times
        global alert_triggered

        if event.is_directory:
            return

        current_time = time.time()

        modification_times.append(current_time)

        modification_times = [
            t for t in modification_times
            if current_time - t <= 10
        ]

        print(f"[INFO] File Modified : {event.src_path}")
        print(f"[INFO] Modifications in last 10 seconds : {len(modification_times)}")

        if len(modification_times) >= 10 and not alert_triggered:

            alert_triggered = True

            print("\n====================================")
            print("WARNING!")
            print("Possible ransomware activity detected!")
            print("====================================")

            notification.notify(
                title="RansomShield Alert",
                message="Possible ransomware activity detected!",
                timeout=10
            )

            with open("response_log.txt", "a", encoding="utf-8") as log:
                log.write("\n=====================================\n")
                log.write(f"Time : {datetime.now()}\n")
                log.write("ALERT : Possible ransomware detected\n")
                log.write("[OK] Suspicious process terminated (SIMULATED)\n")
                log.write("[OK] Device isolated from network (SIMULATED)\n")
                log.write("[OK] Forensic evidence collected\n")
                log.write("[OK] Administrator notified\n")
                log.write("=====================================\n")

            with open("evidence.txt", "a", encoding="utf-8") as f:
                f.write("\n=====================================\n")
                f.write("RANSOMWARE ALERT\n")
                f.write(f"Time : {datetime.now()}\n")
                f.write(f"Target File : {event.src_path}\n")
                f.write(f"Rapid Modifications : {len(modification_times)}\n")

                f.write("\nRunning Processes\n")
                f.write("-------------------------------------\n")

                for process in psutil.process_iter(['pid', 'name']):
                    try:
                        f.write(
                            f"{process.info['name']} - PID : {process.info['pid']}\n"
                        )
                    except:
                        pass

                f.write("=====================================\n")

    def on_deleted(self, event):

        if event.is_directory:
            return

        print(f"[INFO] File Deleted : {event.src_path}")

        with open("response_log.txt", "a", encoding="utf-8") as log:
            log.write("\n=====================================\n")
            log.write("FILE DELETED\n")
            log.write(f"File : {event.src_path}\n")
            log.write(f"Time : {datetime.now()}\n")
            log.write("=====================================\n")

    def on_moved(self, event):

        if event.is_directory:
            return

        print(f"[INFO] File Renamed")
        print(f"Old : {event.src_path}")
        print(f"New : {event.dest_path}")

        with open("change_log.txt", "a", encoding="utf-8") as log:
            log.write("\n=====================================\n")
            log.write(f"Time : {datetime.now()}\n")
            log.write("FILE RENAMED\n")
            log.write(f"Old Name : {event.src_path}\n")
            log.write(f"New Name : {event.dest_path}\n")
            log.write("=====================================\n")


path = r"D:\RansomShield\test_folder"

event_handler = MyHandler()

observer = Observer()

observer.schedule(event_handler, path, recursive=False)

observer.start()

print("====================================")
print("      RansomShield Started")
print("====================================")
print(f"Monitoring Folder : {path}")
print("Waiting for file activity...")
print("====================================")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()