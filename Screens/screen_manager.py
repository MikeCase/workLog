import tkinter as tk

from Screens.Content.completed_screen import CompletedScreen
from Screens.Content.in_progress_screen import InProgressScreen
from Screens.Content.labor_info_screen import LaborInfoScreen
from Screens.Content.veh_info_screen import VehicleInfoScreen



class ScreenManager:
    pass
    # def __init__(self, *args, **kwargs) -> None:
    #     tk.Tk.__init__(self, *args, **kwargs)
    #     container = tk.Frame(self)
    #     container.pack(fill='both', expand=True)
    #     container.grid_rowconfigure(0, weight=1)
    #     container.grid_columnconfigure(0, weight=1)

    #     self.frames = {}
    #     frame = VehicleInfoScreen(container, self)
    #     self.frames[VehicleInfoScreen] = frame
    #     frame.grid(row=0, column=0, sticky='nsew')
    #     self.show_frame(VehicleInfoScreen)

    #     def show_frame(self, cont):
    #         frame = self.frames[cont]
    #         frame.tkraise()

        # self.root = root
        # self.tabs = tabs

        # self.screen = self.tabs[0]
        # self.notebook = ttk.Notebook(self.root)
        # self.notebook.pack()

        # self.frame = ttk.Labelframe(self.notebook, self.screen)

        # def makeNotebook(self):
        #     self.notebook.add()    
            
        # def addFrame(self):
        #     pass

        # def loadScreen(self):
        #     pass