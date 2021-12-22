import tkinter as tk
from tkinter import Entry, StringVar, ttk

# from db import DB
# from models.laborinfo import LaborInfo

# from Screens.Content.veh_info_screen import VehicleInfoScreen

class LaborInfoScreen(tk.Frame):
    def __init__(self, parent, controller, db) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.db = db
        self.padx = 3
        self.pady = 5

        # print(self.parent.children.get('!vehicleinfoscreen').get_vin().get())
        self.laborDesc = StringVar()
        self.laborBookTime = StringVar()
        self.laborStartTime = StringVar()
        self.laborFin = StringVar()
        
        self.label(self, textvar='Job Description', row=0, column=0)
        self.textEntry(self, textvar=self.laborDesc, row=1, column=0)

        self.label(self, textvar='Book time for job', row=2, column=0)
        self.textEntry(self, textvar=self.laborBookTime, row=3, column=0)

        self.label(self, textvar="Start Time:", row=0, column=1)
        self.label(self, textvar=self.laborStartTime, row=0, column=2)

        self.label(self, textvar='Job Complete Time:', row=2, column=1)
        self.label(self, textvar=self.laborFin, row=2, column=2)

        # self._initScreen()

    def label(self, parent, textvar, row, column):
        if type(textvar) == type(tk.StringVar()):
            label = ttk.Label(parent, textvariable=textvar)
        else:
            label = ttk.Label(parent, text=textvar)

        label.grid(row=row, column=column, padx=self.padx, pady=self.pady)
        return label

    def textEntry(self, parent, textvar, row, column):
        textEntry = Entry(parent, textvariable=textvar)
        textEntry.grid(row=row, column=column, padx=self.padx, pady=self.pady)
        return textEntry


    def _initScreen(self):
        laborRecord = self.db.getLabor(self.veh_vin())
        self.laborDesc.set(laborRecord.labor[0].job)
        self.laborBookTime.set(laborRecord.labor[0].booktime)
        self.laborStartTime.set(laborRecord.labor[0].start.strftime('%H:%M:%S'))
        self.laborFin.set(laborRecord.labor[0].finished)

    def _update_screen(self):
        # print(self.veh_vin())
        laborRecord = self.db.getLabor(self.veh_vin())

        # print(laborRecord[0].labor[0].start.strftime('%H:%M:%S'))
        self.laborDesc.set(laborRecord[0].labor[0].job)
        self.laborBookTime.set(laborRecord[0].labor[0].booktime)
        self.laborStartTime.set(laborRecord[0].labor[0].start.strftime('%H:%M:%S'))
        self.laborFin.set(laborRecord[0].labor[0].finished)
        print(self.laborStartTime.get())

    def veh_vin(self):
        return self.parent.children.get('!vehicleinfoscreen').get_vin().get()