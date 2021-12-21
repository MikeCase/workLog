import tkinter as tk
from tkinter import ttk

from db import DB

class CompletedScreen(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.db = DB()
        completed_list = self.db.getComplete()
        # print(completed_list)
        self.completed_list_var = tk.StringVar(value=completed_list)
        self.listbox = tk.Listbox(
            self,
            listvariable=self.completed_list_var,
            height=2,
            selectmode='extended',
            )
            
        self.listbox.pack(fill='both', expand=True)
        self.listbox.bind('<<ListboxSelect>>', lambda x: self.items_selected())

        # self.listbox

    def items_selected(self):
        # newWindow = tk.Toplevel()
        print('Clicked an item...')