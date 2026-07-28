from manager import Manager
from scheduler import Scheduler
from point import *
from config import COMBOS
from tkinter import *
from datetime import datetime


class App:
    def __init__(self,root,manager,scheduler):
        self.root = root
        self.manager = manager 
        self.scheduler = scheduler
        self.scheduler_running = False # bật tắt scheduler 
        self.after_id = None # dùng để bật tắt realtime schedule
        self.active_devices=list(self.manager.devices.keys())
        self.choice = IntVar(value=0) # bien choice để dùng cho radiobutton 
        #--------- AI) dung cho frame job
        self.frame_jobs = Frame(self.root, bg=PINK)
        self.frame_jobs.grid(row=5, column=0, columnspan=3, sticky="w")

        self.root.title("ToolSrom")
        self.root.geometry("400x600")

        Radiobutton(self.root, text= "`手",bg=PINK, variable=self.choice, value=0,command=self.rd_choice_event).grid(row=0,column=0)

        Button(self.root,text="DEVICES",bg=PINK,command=self.bt_get_devices).grid(row=1,column=0,padx=5)
        self.vars_login= {}

        lb_target = Label(self.root,text="TARGET",bg = PINK)
        lb_target.grid(row=2, column=0,padx=5)
        self.vars_target = {}

        self.bt_scheduler = Button(self.root,text="START",bg=PINK,command=self.bt_scheduler_event)
        self.bt_scheduler.grid(row=3, column=0,padx=5)
        self.lb_clock = Label(self.root,text=" CLOCK ",bg=PINK)
        self.lb_clock.grid(row=3, column=1,padx=5)

        self.bt_get_job = Button(root,text="GET->",bg=PINK,command=self.bt_get_job_event)
        self.bt_get_job.grid(row=3,column=2,padx=5)
        self.entry_time = Entry(self.root,width=8)
        self.entry_time.grid(row=3,column=3)
        self.combo_var = StringVar(value="boss")
        self.display_job()
        OptionMenu(self.root,self.combo_var,*COMBOS.keys()).grid(row=3,column=4)
        Button(self.root,text="DELETE",bg=PINK).grid(row=4,column=3)
        Button(self.root,text="DO",bg=PINK).grid(row=4,column=4)

    def bt_change_active_device_scheduler(self,index):
        self.scheduler.active_device_id=LIST_DEVICE[index]
    def bt_all_control(self):
        self.scheduler.active_device_id=None


    def bt_get_devices(self):
        self.manager.active_device=self.active_devices
        for i,device_id in enumerate(self.manager.devices):
            index = LIST_DEVICE.index(device_id)
            var_login = IntVar()
            self.vars_login[device_id] = var_login
            cb_login = Checkbutton(self.root,text=f"DE-{index}",bg=BLU,variable=var_login,command= lambda d=device_id: self.cb_start_login(d))
            cb_login.grid(row=1,column=index,padx=5)

            var_target = IntVar()
            self.vars_target[device_id] = var_target
            cb_target = Checkbutton(self.root,text=f"DE-{index}",bg=BLU,variable=var_target,command= lambda d=device_id: self.cb_start_target(d))
            cb_target.grid(row=2,column=index,padx=5)

            Radiobutton(self.root, text=f"ACC-{index}", variable=self.choice, value=index,command=self.rd_choice_event).grid(row=0,column=index)
            
    def rd_choice_event(self):
        if self.choice.get()==0:
            self.active_devices=list(self.manager.devices.keys())
            print(self.active_devices)
            self.display_job()
            return
        self.active_devices = LIST_DEVICE[self.choice.get()]
        print(self.active_devices)
        self.display_job()

    def cb_start_login(self,device_id):
        if self.vars_login[device_id].get()==1:
            print(f"Click RUN Checkbutton {device_id}")
            self.manager.start_thread(device_id,self.manager.worker,COMBOS["login"])
        else:
            self.manager.manager_set_event(device_id)
            print(f"Click STOP Checkbutton {device_id}")
    def cb_start_target(self,device_id):
        if self.vars_target[device_id].get()==1:
            print(f"Click RUN Checkbutton {device_id}")
            self.manager.start_thread(device_id,self.manager.worker,COMBOS["target"])
        else:
            self.manager.manager_set_event(device_id)
            print(f"Click STOP Checkbutton {device_id}")

    def update_clock(self):
        if not self.scheduler_running:
            return
        now = datetime.now().strftime("%H:%M:%S")
        self.lb_clock.config(text=now)
        self.after_id=self.root.after(1000,self.update_clock)
    def stop_clock(self):
        self.scheduler_running = False
        if self.after_id:
            self.root.after_cancel(self.after_id)

    def bt_scheduler_event(self):
        if not self.scheduler_running:
            self.scheduler_running = True
            self.bt_scheduler.config(text="S-RUN ")
            self.update_clock()
            self.scheduler.start()
            self.display_job()
        else:
            self.scheduler_running = False
            self.bt_scheduler.config(text="S-STOP")
            self.scheduler.stop()
            self.stop_clock()
    
    def bt_get_job_event(self):
        time = self.entry_time.get()
        combo_name = self.combo_var.get()

        # 👉 CASE 1: ALL DEVICES
        if isinstance(self.active_devices, list):
            self.scheduler.add_job(time, combo_name)

        # 👉 CASE 2: 1 DEVICE
        elif isinstance(self.active_devices, str):
            device_id = self.active_devices

            if device_id not in self.manager.jobs:
                self.manager.jobs[device_id] = {}

            self.manager.jobs[device_id][time] = combo_name

        # update UI
        self.display_job()
        
    def display_job(self):

        # 👉 xoá UI cũ trước
        self.clear_jobs()

        # 👉 CASE 1: ALL DEVICES
        if isinstance(self.active_devices, list):

            Label(self.frame_jobs, text="ALL-DEVICES", bg=PINK)\
                .grid(row=0, column=0, columnspan=3)

            for i, job in enumerate(self.scheduler.jobs):
                Label(self.frame_jobs, text=job["time"], bg=PINK)\
                    .grid(row=i+1, column=0)
                Label(self.frame_jobs, text=job["combo"], bg=PINK)\
                    .grid(row=i+1, column=1)

        # 👉 CASE 2: 1 DEVICE
        elif isinstance(self.active_devices, str):

            device_id = self.active_devices

            Label(self.frame_jobs, text=device_id, bg=PINK)\
                .grid(row=0, column=0, columnspan=3)

            jobs = self.manager.jobs.get(device_id, {})

            for i, (time, combo) in enumerate(jobs.items()):
                Label(self.frame_jobs, text=time, bg=PINK)\
                    .grid(row=i+1, column=1)
                Label(self.frame_jobs, text=combo, bg=PINK)\
                    .grid(row=i+1, column=2)
#-------xoa UI job 
    def clear_jobs(self):  
        for widget in self.frame_jobs.winfo_children():
            widget.destroy()
    def start_app(self):
        self.root.mainloop()


