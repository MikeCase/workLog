import tkinter as tk

class InProgressScreen(tk.Frame):
    def __init__(self, parent, controller, db) -> None:
        tk.Frame.__init__(self, parent)
        