from tkinter import ttk

from Screens.Content.completed_screen import CompletedScreen
from Screens.Content.in_progress_screen import InProgressScreen
from Screens.Content.labor_info_screen import LaborInfoScreen
from Screens.Content.veh_info_screen import VehicleInfoScreen



class ScreenManager:

    def __init__(self, root, tabs) -> None:

        self.root = root
        self.tabs = tabs

        self.screen = self.tabs[0]
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.frame = ttk.Labelframe(self.notebook, self.screen)

        def makeNotebook(self):
            self.notebook.add()    
            
        def addFrame(self):
            pass

        def loadScreen(self):
            pass