from point import *
import time
import subprocess
class Device:
    def __init__(self,device_id):
        self.adb_path = r"C:\LDPlayer\LDPlayer9\dnconsole.exe"
        self.device_id = device_id
    
    def tap(self,x,y):
        subprocess.run(["adb","-s",self.device_id,"shell","input","tap",str(x),str(y)])
    
    # hàm get này dùng toàn hệ thống để có thể xác nhận device hoạt động
def get_devices():
    result = subprocess.run(["adb", "devices"],capture_output=True,text=True)
    lines = result.stdout.strip().split("\n")
    devices = []
    for line in lines[1:]:
        if line.strip():
            parts = line.split("\t")
            if len(parts) == 2 and parts[1] == "device":
                devices.append(parts[0])
    return devices
    