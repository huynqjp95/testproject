from device import Device
import threading

class Manager:
    def __init__(self):
        self.devices = {}
        self.threads = {}
        self.events  = {}
        self.jobs    = {}

    # -------------------------
    # 📱 ADD DEVICE
    # -------------------------
    def add_device(self,device):
        self.devices[device.device_id] = device
        self.events[device.device_id]  = threading.Event()
    
    def add_job(self,device_id,time,combo):
        if device_id not in self.jobs:
            self.jobs[device_id] = {}
        self.jobs[device_id][time]=combo
    def pop_job(self,device_id,time):
        if device_id not in self.jobs:
            print(f"{device_id} NOT TON TAI")
            return
        self.jobs[device_id].pop(time,None)

    

    # -------------------------
    # 🛑 Stop thread cũ nếu đang chạy
    # -------------------------
    def start_thread(self, device_id,worker,*args,**kwargs):
        if device_id in self.threads:
            old_thread = self.threads[device_id]
            if old_thread.is_alive():
                print(f"Thread {device_id} đang chạy , chương trình sẽ tắt thread này")
                self.events[device_id].set()
                old_thread.join()

        # -------------------------
        # 🔄 Reset event
        # -------------------------
        stop_event=self.events[device_id]
        stop_event.clear()

        # -------------------------
        # 🧠 Wrapper để bắt lỗi + logging
        # -------------------------
        def thread_wrapper():
            try:
                print(f"{device_id} RUN - {worker.__name__}")
                worker(device_id,stop_event,*args,**kwargs)
            except Exception as e :
                print(f"{device_id} ERROR : ",e)
            finally:
                print(f"{device_id} STOP - {worker.__name__}")
                
        # -------------------------
        # 🚀 Tạo thread
        # -------------------------
        t = threading.Thread(target=thread_wrapper,daemon=True)
        self.threads[device_id]=t
        t.start()


#--- WORKER các hàm logic điều khiển device
    def manager_start_device(self,device_id,stop_event):
        if not stop_event.is_set():
            self.devices[device_id].start_device()
#--- ACTION WORKER
    def worker(self,device_id,stop_event,combo):
        if stop_event.is_set():
            return
        device = self.devices[device_id]
        for step in combo:
            if step["action"] == "tap":
                device.tap(step["x"],step["y"])
            elif step["action"] == "swipe":
                device.swipe(step["x"],step["y"])
            elif step["action"] == "target":    #_------ vong loop cho target tap lien tuc
                while not stop_event.is_set():
                    device.tap(step["x"],step["y"])
                    stop_event.wait(step["delay"])
                return
            stop_event.wait(step["delay"])
    
#--- Stop thread
    def manager_set_event(self,device_id):
        self.events[device_id].set()
    def manager_clear_event(self,device_id):
        self.events[device_id].clear()



    


