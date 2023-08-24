# Timer

import tkinter as tk
from tkinter import ttk
#Module to be able to manipulate the timer breaks
from collections import deque


# Class Pomodoro Timer 
class PomodoroTimer(tk.Tk):
    def __init__(self,*args,**Kwargs):
        super().__init__(*args,**Kwargs)
        #Config
        self.title("Pomodoro Timer")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)

        #Container
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0,weight=1)

        #Timer Frame
        timer_frame = Timer(container)
        timer_frame.grid(row=0,column=0,sticky="NESW")

# Class Timer 
class Timer(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.current_time = tk.StringVar(value="00:10")
        self.time_running = True
        self.time_order = ["Pomodoro","Short Break","Pomodoro","Short Break","Pomodoro","Long Break"] # Time Breakers
        self.timer_schedule = deque(self.time_order) # deque provides an O(1) time complexity for append and pop operations as compared to a list 
        self._timer_decrement_job = None # (-) private It will help us to be able to manipulate the load of the frame
        
        # Timer Description Label
        self.current_timer_description = tk.StringVar(value=self.timer_schedule[0]) # current timer desc string var
        timer_descriptin = ttk.Label(self,textvariable=self.current_timer_description) # Description Label
        timer_descriptin.grid(row=0,column=0,sticky="w",padx=(10,0),pady=(10,0))
        
        # Timer Container Frame
        timer_frame = ttk.Frame(self,height="100")
        timer_frame.grid(pady=(10,0),sticky="NSEW")

        # Timer Counter
        timer_counter = ttk.Label(timer_frame,textvariable=self.current_time)
        timer_counter.place(relx=0.5,rely=0.5,anchor="center")

        # Buttons Container Frame
        buttons_container = ttk.Frame(self,padding=10)
        buttons_container.grid(row=2,column= 0,sticky="EW")
        buttons_container.columnconfigure((0,1),weight=1)

        # Start Button
        self.start_button = ttk.Button(
            buttons_container,
            text= "Start",
            command = self.start_timer,
            cursor="hand2"
        )
        self.start_button.grid(row=0,column=0,sticky="Ew")
        
        # Stop Button
        self.stop_button = ttk.Button(
            buttons_container,
            text="Stop",
            command=self.stop_timer,
            cursor="hand2"
        )
        self.stop_button.grid(row=0,column=1,sticky="EW")

        self.decrement_time()
    
    
    def start_timer(self):
        # Initializes the variables needed to start the timer (enable/disable buttons)
        self.time_running = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "enabled"
        self.decrement_time()

    def stop_timer(self):
        # Initializes the variables needed to stop the timer (enable/disable buttons)
        self.time_running = False
        self.start_button["state"] = "enabled"
        self.stop_button["state"] = "disabled"

        # Stops the update of the timer in the frame
        if self._timer_decrement_job:
            self.after_cancel(self._timer_decrement_job)
            self._timer_decrement_job = None 

    def decrement_time(self):
        current_time = self.current_time.get()

        if self.time_running and current_time!= "00:00":
            minutes,seconds = current_time.split(":")

            if int(seconds) >0:
                seconds= int(seconds)-1
                minutes= int(minutes)
            
            else:
                seconds= 59
                minutes = int(minutes)-1
            
            self.current_time.set(f"{minutes:02d}:{seconds:02d}")
            self._timer_decrement_job= self.after(1000,self.decrement_time)
        
        elif self.time_running and current_time == "00:00":
            self.timer_schedule.rotate(-1) # Rotate the deque (n) steps.If (-n) is negative, rotate to the left.
            next_up = self.timer_schedule[0] # => First element after rotate.
            self.current_timer_description.set(next_up) # Change to current description

            # Timers Options
            if next_up == "Pomodoro":
                self.current_time.set("25:00")
            elif next_up == "Short Break":
                self.current_time.set("05:00")
            elif next_up == "Long Break":
                self.current_time.set("15:00")

            self._timer_decrement_job= self.after(1000,self.decrement_time)


app = PomodoroTimer()
app.mainloop()