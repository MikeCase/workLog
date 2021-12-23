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

        self.laborDesc = StringVar()
        self.laborBookTime = StringVar()
        self.laborStartTime = StringVar()
        self.laborFin = StringVar()
        
        self.label(self, textvar='Job Description', row=0, column=0)
        self.textEntry(self, textvar=self.laborDesc, row=1, column=0)

        self.label(self, textvar='Book time for job', row=2, column=0)
        self.textEntry(self, textvar=self.laborBookTime, row=3, column=0)

        self.label(self, textvar="Start Time:", row=0, column=1)
        self.label(self, textvar=self.laborStartTime, row=1, column=1)

        self.label(self, textvar='Job Complete Time:', row=2, column=1)
        self.label(self, textvar=self.laborFin, row=3, column=1)

        # self._initScreen()

    def label(self, *args, **kwargs):
        parent = args[0]
        textvar = kwargs['textvar']
        row = kwargs['row']
        col = kwargs['column']

        """ Build and place a label widget """
        ## First check to see if textvar is a tk.StringVar() type
        if type(textvar) == type(tk.StringVar()):
            label = ttk.Label(parent, textvariable=textvar)
        else: ## If not, just set regular text.
            label = ttk.Label(parent, text=textvar)
        ## Set the grid
        label.grid(row=row, column=col, padx=self.padx, pady=self.pady)
        return label

    def textEntry(self, *args, **kwargs):
        parent = args[0]
        textvar = kwargs['textvar']
        row = kwargs['row']
        col = kwargs['column']

        textEntry = Entry(parent, textvariable=textvar)
        textEntry.grid(row=row, column=col, padx=self.padx, pady=self.pady)
        return textEntry


    def _initScreen(self):
        laborRecord = self.db.getLabor(self.veh_vin())
        self.laborDesc.set(laborRecord.labor[0].job)
        self.laborBookTime.set(laborRecord.labor[0].booktime)
        self.laborStartTime.set(laborRecord.labor[0].start.strftime('%H:%M:%S'))
        self.laborFin.set(laborRecord.labor[0].finished)

    def _update_screen(self):
        laborRecord = self.db.getLabor(self.veh_vin())

        job_title = laborRecord[0].labor[0].job
        job_booktime = laborRecord[0].labor[0].booktime
        job_start = laborRecord[0].labor[0].start.strftime('%H:%M:%S')
        job_finished = laborRecord[0].labor[0].finished

        self.laborDesc.set(job_title)
        self.laborBookTime.set(job_booktime)
        self.laborStartTime.set(job_start)
        if job_finished: 
            self.laborFin.set(job_finished.strftime('%H:%M:%S'))
        else:
            self.laborFin.set('')

    def veh_vin(self):
        return self.parent.children.get('!vehicleinfoscreen').get_vin().get()