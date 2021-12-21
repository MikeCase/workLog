import tkinter as tk
from tkinter import ttk
# from Screens.screen_manager import ScreenManager
from Screens.Content.veh_info_screen import VehicleInfoScreen
from Screens.Content.labor_info_screen import LaborInfoScreen
from Screens.Content.in_progress_screen import InProgressScreen
from Screens.Content.completed_screen import CompletedScreen


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = ttk.Notebook(self)
        container.pack(fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (VehicleInfoScreen, LaborInfoScreen, InProgressScreen, CompletedScreen):
            frame = F(container, self)
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

    def show_frames(self, cont, frames):
        for frame in frames:
            cont.add(frame)
        # frame = self.frames[cont]
        # self.container.add(frame)
        # frame.tkraise()


if __name__ == "__main__":
    app = Main()
    app.mainloop()
