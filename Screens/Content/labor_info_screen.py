from tkinter import Entry, StringVar, ttk

from db import DB
from models.laborinfo import LaborInfo

class LaborInfoScreen:
    def __init__(self, frame) -> None:
        self.db = DB()
        self.padx = 3
        self.pady = 5

        self.laborDesc = StringVar()
        self.laborBookTime = StringVar()
        self.laborStartTime = StringVar()
        self.laborFin = StringVar()
        
        self.lblJobDesc = ttk.Label(frame, text='Job Description').grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.txtJobDesc = Entry(frame, textvariable=self.laborDesc).grid(row=1, column=0, padx=self.padx, pady=self.pady)

        self.lblBookTime = ttk.Label(frame, text='Book time for job').grid(row=2, column=0, padx=self.padx, pady=self.pady)
        self.txtBookTime = Entry(frame, textvariable=self.laborBookTime).grid(row=3, column=0, padx=self.padx, pady=self.pady)

        self.lblJobStart = ttk.Label(frame, text="Start Time:").grid(row=0, column=1, padx=self.padx, pady=self.pady)
        self.txtJobStart = ttk.Label(frame, text=self.laborStartTime).grid(row=0, column=2, padx=self.padx, pady=self.pady)

        self.lblFin = ttk.Label(frame, text='Job Complete Time:').grid(row=2, column=1, padx=self.padx, pady=self.pady)
        self.lblDataFin = ttk.Label(frame, text=self.laborFin).grid(row=2, column=2, padx=self.padx, pady=self.pady)

        self._initScreen()

        
    def _initScreen(self):
        laborRecord = self.db.getLabor()
        self.laborDesc.set(laborRecord.labor[0].job)
        self.laborBookTime.set(laborRecord.labor[0].booktime)
        self.laborStartTime.set(laborRecord.labor[0].start)
        self.laborFin.set(laborRecord.labor[0].finished)