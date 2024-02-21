# Timer

import tkinter as tk
from tkinter import ttk
# Module to be able to manipulate the timer breaks
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

        self.frames = {}

        #Timer Frame
        timer_frame = Timer(container,self,lambda: self.show_frame(Settings))
        timer_frame.grid(row=0,column=0,sticky="NESW")
    
        #Setting Frame
        setting_frame = Settings(container,self,lambda: self.show_frame(Timer))
        setting_frame.grid(row=0,column=0,sticky="NESW")

        
        self.frames[Timer] = timer_frame
        self.frames[Settings] = setting_frame
        
        self.show_frame(Timer)
    
    def show_frame(self,container):
        frame = self.frames[container]
        frame.tkraise()


if __name__ == '__main__':
    app = PomodoroTimer()
    app.mainloop()