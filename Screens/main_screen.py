from tkinter import ttk

from Screens.Content.completed_screen import CompletedScreen
from Screens.Content.in_progress_screen import InProgressScreen
from Screens.Content.labor_info_screen import LaborInfoScreen
from Screens.Content.veh_info_screen import VehicleInfoScreen
test_list = [
    'start - finish - car - job',
    'start - finish - car - job',
    'start - finish - car - job',
    'start - finish - car - job',
    'start - finish - car - job',
    'start - finish - car - job',
    'start - finish - car - job',
    'start - finish - car - job',

]
class MainNoteBook:

    def __init__(self, root, tabs) -> None:
        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, expand=True, fill='both')

        for tab in tabs:
            frame = ttk.Frame(notebook)
            frame.pack(fill='both', expand=True)
            if tab == "Vehicle Info":
                VehicleInfoScreen(frame)
            if tab == "Labor Info":
                LaborInfoScreen(frame)
            if tab == "In Progress":
                InProgressScreen(frame)
            if tab == "Completed":
                CompletedScreen(frame, test_list)

            notebook.add(frame, text=tab)



        