import sys
import tkinter as tk
from tkinter import ttk
from Screens.Content.veh_info_screen import VehicleInfoScreen
from Screens.Content.labor_info_screen import LaborInfoScreen
from Screens.Content.in_progress_screen import InProgressScreen
from Screens.Content.completed_screen import CompletedScreen
from db import DB


### Maybe this works? I dont know, I'm to lazy to look it up atm. 
### VVVVVVVV
try:
    import obd
except ImportError: 
    print('OBD Module not installed, OBD connections won\'t work')
### End maybe.. research this shit. 

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "Mechanics Work Log")
        # tk.Tk.iconphoto()
        self.db = DB()
        if "obd" in sys.modules:
            self.con = obd.OBD()
        else:
            self.con = None
        
        container = ttk.Notebook(self)
        container.pack(fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (VehicleInfoScreen, LaborInfoScreen, InProgressScreen, CompletedScreen):
            if self.con is not None and self.con.is_connected():
                frame = F(container, self, self.db, self.con)
            else:
                frame = F(container, self, self.db)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            if F == VehicleInfoScreen:
                container.add(self.frames[F], text='Vehicle Info')
            if F == LaborInfoScreen:
                container.add(self.frames[F], text='Labor Info')
            if F == InProgressScreen:
                container.add(self.frames[F], text='Current Jobs')
            if F == CompletedScreen:
                container.add(self.frames[F], text='Completed Jobs')
        # self.show_frames(container, self.frames)
        
    # def show_frames(self, cont, frames):
    #     for frame in frames:
    #         cont.add(frame)


if __name__ == "__main__":
    app = Main()
    app.mainloop()
