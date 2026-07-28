from device import Device,get_devices
from app import App
from manager import Manager
from point import LIST_DEVICE
from tkinter import *
from scheduler import Scheduler

if __name__ == "__main__":
    manager = Manager()
    devices = get_devices()
    for i,device_id in enumerate(devices):
        device = Device(device_id)
        manager.add_device(device)

    root = Tk()
    scheduler = Scheduler(manager)
    scheduler.add_job("21:29","changeRange200")
    scheduler.add_job("21:30","boss")
    scheduler.add_job("21:40","outBoss")
    scheduler.add_job("21:41","outGame")
    

    app = App(root,manager,scheduler)
    app.start_app()

