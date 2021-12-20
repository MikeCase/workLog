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
        
        self.lblJobDesc = ttk.Label(frame, text='Job Description').grid(row=0, column=0)
        self.txtJobDesc = Entry(frame, textvariable=self.laborDesc).grid(row=1, column=0)

        self.lblBookTime = ttk.Label(frame, text='Book time for job').grid(row=2, column=0)
        self.txtBookTime = Entry(frame, textvariable=self.laborBookTime).grid(row=3, column=0)

        self.lblJobStart = ttk.Label(frame, text="Start Time").grid(row=0, column=1)
        self.txtJobStart = ttk.Label(frame, textvariable=self.laborStartTime).grid(row=0, column=2)

        self.lblFin = ttk.Label(frame, text='Job Complete Time:').grid(row=1, column=1)
        self.lblDataFin = ttk.Label(frame, textvariable=self.laborFin).grid(row=1, column=2)

        self._initScreen()

        
    def _initScreen(self):
        self.db.getLabor()