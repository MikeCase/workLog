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
        # self.textEntry(self, textvar=self.laborDesc, row=1, column=0, width=25)
        self.txt_desc = tk.Text(self, width=80, height=3)
        self.txt_desc.grid(row=1, column=0, columnspan=12, sticky='w')
        

        self.label(self, textvar='Booktime: ', row=2, column=0)
        self.label(self, textvar=self.laborBookTime, row=2, column=1)
        # self.lbl_booktime = tk.Label(self, textvariable=self.laborBookTime, anchor='w', justify='left')
        # self.lbl_booktime.grid(row=2, column=1, sticky='w')

        self.label(self, textvar="Start Time:", row=2, column=2)
        self.label(self, textvar=self.laborStartTime, row=2, column=3)

        self.label(self, textvar='Job Complete Time:', row=2, column=4)
        self.label(self, textvar=self.laborFin, row=2, column=5)

        self.btn_btime = tk.Button(self, text="Set Book Time", command=self.btime)
        self.btn_btime.grid(row=3, column=0)
        self.btn_start = tk.Button(self, text="Start Job", command=self.start_job)
        self.btn_start.grid(row=3, column=2)
        self.btn_complete = tk.Button(self, text="Complete Job", command=self.complete_job)
        self.btn_complete.grid(row=3, column=4)

        self.dtc_lf = ttk.LabelFrame(self, text="DTC's")
        self.dtc_lf.grid(row=4, column=0, columnspan=6, rowspan=4, pady=self.pady)

        self.dtc_treeview = ttk.Treeview(self.dtc_lf)
        self.dtc_treeview['columns'] = ('Code', 'Description')
        self.dtc_treeview.column('#0', width=0, stretch='NO')
        self.dtc_treeview.column('Code', anchor='w')
        self.dtc_treeview.column('Description', anchor='w')
        self.dtc_treeview.heading('#0', text='', anchor='center')
        self.dtc_treeview.heading('Code', text='Code', anchor='w')
        self.dtc_treeview.heading('Description', text='Description', anchor='w')
        self.dtc_treeview.grid(row=0, column=0, columnspan=2, )
        
        self.btn_dtc_add = tk.Button(self.dtc_lf, text='Add DTC')
        self.btn_dtc_add.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        self.btn_dtc_rem = tk.Button(self.dtc_lf, text='Remove DTC')
        self.btn_dtc_rem.grid(row=1, column=1, padx=self.padx, pady=self.pady)
        
        self.diag_lf = ttk.LabelFrame(self, text='Diag Notes')
        self.diag_lf.grid(row=4, column=6, columnspan=6, rowspan=4, pady=self.pady)


        self.diag_treeview = ttk.Treeview(self.diag_lf)
        self.diag_treeview['columns'] = ('Note#', 'Description')
        self.diag_treeview.column('#0', width=0, stretch='NO')
        self.diag_treeview.column('Note#', anchor='w')
        self.diag_treeview.column('Description', anchor='w')
        self.diag_treeview.heading('#0', text='', anchor='center')
        self.diag_treeview.heading('Note#', text='Note #', anchor='w')
        self.diag_treeview.heading('Description', text='Description', anchor='w')
        self.diag_treeview.grid(row=0, column=0, columnspan=2, )

        
        self.btn_diag_add = tk.Button(self.diag_lf, text='Add Diag Note')
        self.btn_diag_add.grid(row=1, column=0, padx=self.padx, pady=self.pady)
        
        self.btn_diag_rem = tk.Button(self.diag_lf, text='Remove Diag Note')
        self.btn_diag_rem.grid(row=1, column=1, padx=self.padx, pady=self.pady)




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
        label.grid(row=row, column=col, padx=self.padx, pady=self.pady, sticky='w')
        return label

    def text_entry_multi(self, *args, **kwargs):
        parent = args[0]

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

        try:
            colspan = kwargs['colspan']
        except:
            colspan = None
        
        try:
            sticky = kwargs['sticky']
        except:
            sticky = None

        textEntry = Entry(parent, textvariable=textvar, width=width)
        textEntry.grid(row=row, column=col, padx=self.padx, pady=self.pady, columnspan=colspan, sticky=sticky)
        return textEntry


    def _initScreen(self):
        laborRecord = self.db.getLabor(self.veh_vin())
        self.laborDesc.set(laborRecord.labor[0].job)
        self.laborBookTime.set(laborRecord.labor[0].booktime)
        self.laborStartTime.set(laborRecord.labor[0].start.strftime('%H:%M:%S'))
        self.laborFin.set(laborRecord.labor[0].finished)

    def _update_screen(self):
        self.txt_desc.delete('1.0', tk.END)
        laborRecord = self.db.getLabor(self.veh_vin())

        job_desc = laborRecord[0].labor[0].job
        job_booktime = laborRecord[0].labor[0].booktime
        job_start = laborRecord[0].labor[0].start.strftime('%H:%M:%S')
        job_finished = laborRecord[0].labor[0].finished

        self.laborDesc.set(job_desc)
        self.txt_desc.insert(tk.END, self.laborDesc.get())
        self.laborBookTime.set(job_booktime)
        self.laborStartTime.set(job_start)
        if job_finished: 
            self.laborFin.set(job_finished.strftime('%H:%M:%S'))
        else:
            self.laborFin.set('In Progress...')

    def veh_vin(self):
        return self.parent.children.get('!vehicleinfoscreen').get_vin().get()

    def btime(self):
        top = tk.Toplevel(self.controller)
        top.geometry('150x100')
        top.transient(self.controller)
        booktime = StringVar()

        dlg_label = tk.Label(top, text='Please enter the book time')
        dlg_label.grid(row=0, column=0, columnspan=2, padx=self.padx, pady=self.pady)
        entry = tk.Entry(top, width=8, textvariable=booktime)
        entry.grid(row=1, column=0, columnspan=2, padx=self.padx, pady=self.pady)
        button = tk.Button(top, text='Set Book Time', command=lambda: set_booktime())
        button.grid(row=2, column=0, padx=self.padx, pady=self.pady)
        btn_cancel = tk.Button(top, text="Cancel", command=lambda: top.destroy())
        btn_cancel.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        # return top
        def set_booktime():
            self.laborBookTime.set(booktime.get())
            top.destroy()

    def start_job(self):
        pass

    def complete_job(self):
        pass
