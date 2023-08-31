# Timer

import tkinter as tk
from tkinter import ttk
#Module to be able to manipulate the timer breaks
from collections import deque

from frames import Timer 
from frames.setting import Settings

# Class Pomodoro Timer 
class PomodoroTimer(tk.Tk):
    def __init__(self,*args,**Kwargs):
        super().__init__(*args,**Kwargs)
        #Config
        self.title("Pomodoro Timer")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.short_break = tk.StringVar(value = 5)
        self.long_break = tk.StringVar(value = 15)
        self.time_order = ["Pomodoro","Short Break","Pomodoro","Short Break","Pomodoro","Long Break"] # Time Breakers
        self.timer_schedule = deque(self.time_order) # deque provides an O(1) time complexity for append and pop operations as compared to a list 

        
        #Container
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0,weight=1)

        #Timer Frame
        timer_frame = Timer(container,self)
        timer_frame.grid(row=0,column=0,sticky="NESW")

app = PomodoroTimer()
app.mainloop()