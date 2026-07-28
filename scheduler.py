
import threading
import time
from datetime import datetime
from config import COMBOS


class Scheduler:
    def __init__(self,manager):
        self.manager = manager
        self.jobs = []
        self.running = False
    
    def add_job(self,time_str,combo_name):
        self.jobs.append({
            "time":time_str,
            "combo":combo_name,
            "done_today":False
        })
    def start(self):
        print("Scheduler Start")
        self.running=True
        threading.Thread(target=self.run,daemon=True).start()
    def stop(self):
        self.running=False

    def run(self):
        print("Scheduler Run")
        while self.running:
            now = datetime.now().strftime("%H:%M")
            # 1. Job global (chạy job cua scheduler)
            for job in self.jobs:
                if job["time"] == now and not job["done_today"]:
                    combo = COMBOS[job["combo"]]
                    for device_id in self.manager.devices:
                        self.manager.start_thread(device_id,self.manager.worker,combo)
                    job["done_today"] = True
                # 👉 CASE 2: là chạy job cua moi device
            for device_id in self.manager.devices:
                if device_id in self.manager.jobs:
                    if now in self.manager.jobs[device_id]:
                        job = self.manager.jobs[device_id][now]
                        combo = COMBOS[job] #day moi la combo, combo la 1 list cac dict
                        self.manager.start_thread(device_id,self.manager.worker,combo)
                        self.manager.pop_job(device_id, now)
            time.sleep(1)

        print("Scheduler OFF")


