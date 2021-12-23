import tkinter as tk
from tkinter import Entry, StringVar, ttk


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
        
        ## Frame Layout
        self.label(self, textvar='Job Description', row=0, column=0)
        self.textEntry(self, textvar=self.laborDesc, row=1, column=0, width=25)

        self.label(self, textvar='Book time for job', row=2, column=0)
        self.textEntry(self, textvar=self.laborBookTime, row=3, column=0)

        self.label(self, textvar="Start Time:", row=0, column=1)
        self.label(self, textvar=self.laborStartTime, row=1, column=1)

        self.label(self, textvar='Job Complete Time:', row=2, column=1)
        self.label(self, textvar=self.laborFin, row=3, column=1)

        # self._initScreen()

    def label(self, *args, **kwargs):
        """ Build and place a label widget """

        parent = args[0]
        textvar = kwargs['textvar']
        row = kwargs['row']
        col = kwargs['column']

        ## Choose between text and textvariable options
        if type(textvar) == type(tk.StringVar()):
            label = ttk.Label(parent, textvariable=textvar)
        else:
            label = ttk.Label(parent, text=textvar)
        ## Set the widget in its grid position
        label.grid(row=row, column=col, padx=self.padx, pady=self.pady)
        return label

    def textEntry(self, *args, **kwargs):
        parent = args[0]
        textvar = kwargs['textvar']
        row = kwargs['row']
        col = kwargs['column']

        try:
            width = kwargs['width']
            print(f'Width set to {kwargs["width"]}')
        except KeyError:
            print("Width not set, setting a default value")
            width = 20

        textEntry = Entry(parent, textvariable=textvar, width=width)
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

        job_desc = laborRecord[0].labor[0].job
        job_booktime = laborRecord[0].labor[0].booktime
        job_start = laborRecord[0].labor[0].start.strftime('%H:%M:%S')
        job_finished = laborRecord[0].labor[0].finished

        self.laborDesc.set(job_desc)
        self.laborBookTime.set(job_booktime)
        self.laborStartTime.set(job_start)
        if job_finished: 
            self.laborFin.set(job_finished.strftime('%H:%M:%S'))
        else:
            self.laborFin.set('In Progress...')

    def veh_vin(self):
        return self.parent.children.get('!vehicleinfoscreen').get_vin().get()