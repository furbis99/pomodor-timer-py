# Setting class

# Imports
import tkinter as tk
from tkinter import ttk
class Settings(ttk.Frame):
    def __init__(self,parent,controller,show_frames):
        super().__init__(parent)
        # Column and row config
        self.columnconfigure(0,weight=1)
        self.rowconfigure(2,weight=1)

        # Container
        setting_container = ttk.Frame(self,padding="30 15 30 51 ")
        setting_container.grid(row=0,column=0,sticky="EW")

        #* POMODORO WIDGETS SETTINGS
        #? Label
        pomodoro_label = ttk.Label(setting_container,text="Pomodoro:")
        pomodoro_label.grid(column=0,row=0,sticky="W")
        #? SpinBox Input
        pomodoro_input = ttk.Spinbox(
            setting_container,
            from_= 0,
            to = 120,
            increment=1,
            textvariable=controller.pomodoro, # get the value of the pomodoro variable from the app file
            justify="center",
            width=10)
        pomodoro_input.grid(column=1,row=0,sticky="EW")
        pomodoro_input.focus()

        #* LONG BREAK WIDGETS SETTINGS
         #? Label
        long_break_label = ttk.Label(setting_container,text="Long break:")
        long_break_label.grid(column=0,row=1,sticky="W")
        #? SpinBox Input
        long_break_input = ttk.Spinbox(
            setting_container,
            from_= 0,
            to = 60,
            increment=1,
            textvariable=controller.long_break, # get the value of the long_break variable from the app file
            justify="center",
            width=10)
        long_break_input.grid(column=1,row=1,sticky="EW")

        #* SHORT BREAK WIDGETS SETTINGS
         #? Label
        short_break_label = ttk.Label(setting_container,text="Short break:")
        short_break_label.grid(column=0,row=2,sticky="W")
        #? SpinBox Input
        short_break_input = ttk.Spinbox(
            setting_container,
            from_= 0,
            to = 30,
            increment=1,
            textvariable=controller.short_break, # get the value of the short_break variable from the app file
            justify="center",
            width=10)
        short_break_input.grid(column=1,row=2,sticky="EW")

        for child in setting_container.winfo_children():
            child.grid_configure(padx=5,pady=5) #add a padding to all elements inside the container

        # Button Container
        button_container = ttk.Frame(self)
        button_container.grid(sticky="EW",padx=10)
        button_container.columnconfigure(0,weight=1)

        timer_button = ttk.Button(
            button_container,
            text="Back",
            command=show_frames,
            cursor="hand2"
        )
        timer_button.grid(column=0,row=0,sticky="EW",padx=2)