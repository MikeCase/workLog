import tkinter as tk
from tkinter import Entry, StringVar, ttk
import requests
from sqlalchemy.sql.expression import column
from pprint import pprint
# import obd

class VehicleInfoScreen(tk.Frame):
    
    def __init__(self, parent, controller, db, obd_connection=None) -> None:
        """Vehicle Info Screen

        Args:
            parent (tk.Widget): Parent Widget
            controller ([type]): [description]
            db ([type]): [description]
        """
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.db = db
        self.con = obd_connection
        self.padx = 3
        self.pady = 5

        self.vehYear = StringVar()
        self.vehMake = StringVar()
        self.vehModel = StringVar()
        self.vehEngine = StringVar()
        self.vehVin = StringVar()
        self.vehMileage = StringVar()
        self.vehPlate = StringVar()
        self.vehDatecode = StringVar()
        
        tv_cols = (
            'VIN',
            'Year',
            'Make',
            'Model',
            'Engine',
            'Mileage',
            'Plate',
            'Datecode'
            )

        tv_anchors = (
            'w',
            'center',
            'center',
            'center',
            'center',
            'center',
            'center',
            'w'
        )

        tv_widths = (
            80, 
            10,
            60,
            60,
            20,
            40,
            20,
            15,
        )

        ## Labels
        self.label(self, text="Vehicle Year",column=0, row=0)
        self.label(self, text="Vehicle Make", column=0, row=1)
        self.label(self, text="Vehicle Model", column=0, row=2)
        self.label(self, text="Vehicle Engine", column=0, row=3)
        self.label(self, text="Vehicle Vin", column=3, row=0)
        self.label(self, text="Vehicle Mileage", column=3, row=1)
        self.label(self, text="Vehicle Plate", column=3, row=2)
        self.label(self, text="Vehicle Date Code", column=5, row=0)

        ## Entry boxes
        self.textEntry(self, textvar=self.vehYear, column=1, row=0)
        self.textEntry(self, textvar=self.vehMake, column=1, row=1)
        self.textEntry(self, textvar=self.vehModel, column=1, row=2)
        self.textEntry(self, textvar=self.vehEngine, column=1, row=3)
        self.textEntry(self, textvar=self.vehVin, column=4, row=0, binder='toUpper')
        self.textEntry(self, textvar=self.vehMileage, column=4, row=1)
        self.textEntry(self, textvar=self.vehPlate, column=4, row=2, binder='toUpper')
        self.textEntry(self, textvar=self.vehDatecode, column=6, row=0)

        ## Buttons
        self.button(self, text='Save', command=lambda: self.saveVehicle(), gridcol=3, gridrow=3)
        self.button(self, text='Clear', command=lambda: self._clearVehicle(), gridcol=4, gridrow=3)
        self.button(self, text='Decode', command=lambda: self.decodeVin(), gridcol=5, gridrow=3)
        self.button(self, text='Remove', command=lambda: self._removeVehicle(self.vehVin.get()), gridcol=6, gridrow=3)

        ## Treeview

        self.tv = self.makeTreeView(self, tv_cols, anchor=tv_anchors, width=tv_widths, binder=['<Double-1>', self.onDoubleClick])
        

        self.listVehicle()
        self.obd_get_vin()

    # Methods

    def makeTreeView(self, *args, **kwargs):
        """Create TreeView Widget to be displayed in frame

        Returns:
            ttk.TreeView: TreeView Widget
        """

        parent = args[0]
        cols=args[1]

        try:
            a = kwargs['anchor']
        except KeyError:
            a = []
            for _, i in enumerate(cols):
                a.append('center')

        try:
            w = kwargs['width']
        except KeyError:
            w = []
            for _, i in enumerate(cols):
                w.append('40')

        ## Build TreeView widget            
        tv = ttk.Treeview(parent)

        ## TreeView Columns
        tv['columns'] = cols
        tv.column('#0', width=0, stretch='NO')
        for idx, col in enumerate(cols):
            tv.column(col, anchor=a[idx], width=w[idx])

        ## Heading rows
        tv.heading('#0', text='', anchor='center')
        for idx, col in enumerate(cols):
            tv.heading(col, text=col, anchor=a[idx])

        try:
            tv.bind(kwargs['binder'][0], kwargs['binder'][1])
        except:
            pass
        
        ## Apply grid positioning
        tv.grid(column=0, row=4, columnspan=9, sticky='we')

        return tv

    def button(self, parent, text, command, gridrow, gridcol):
        """Creates a button Widget to be displayed in frame.

        Args:
            parent ([tk.Frame]): tk.Frame element
            text ([str]): String to be displayed
            command ([callback]): command to call
            gridrow ([int]): row number
            gridcol ([int]): column number
        """
        button = ttk.Button(parent, text=text, command=command)
        button.grid(column=gridcol, row=gridrow, padx=self.padx, pady=self.pady)

    def label(self, parent, text, row, column):
        label = ttk.Label(parent, text=text)

        label.grid(row=row, column=column, padx=self.padx, pady=self.pady)
        return label

    def textEntry(self, parent, textvar, row, column, binder=None):
        textEntry = Entry(parent, textvariable=textvar)
        if binder and binder == "toUpper":
            textEntry.bind('<KeyRelease>', lambda x: self._to_upper(textvar))
        textEntry.grid(row=row, column=column, padx=self.padx, pady=self.pady)
        return textEntry

    def _to_upper(self, *args):
        """Helper method to capitalize text entered into Entry Widget

        """
        args[0].set(args[0].get().upper())

    def onDoubleClick(self, event):
        """Helper method for double clicking on a treeview row.

        Args:
            event (tk.event): Not used
        """
        item = self.tv.selection()[0]
        self.vehVin.set(value=self.tv.item(item)['values'][0])
        self.vehYear.set(value=self.tv.item(item)['values'][1])
        self.vehMake.set(value=self.tv.item(item)['values'][2])
        self.vehModel.set(value=self.tv.item(item)['values'][3])
        self.vehEngine.set(value=self.tv.item(item)['values'][4])
        self.vehMileage.set(value=self.tv.item(item)['values'][5])
        self.vehPlate.set(value=self.tv.item(item)['values'][6])
        self.vehDatecode.set(value=self.tv.item(item)['values'][7])
        self.parent.children.get('!laborinfoscreen')._update_screen()

    def saveVehicle(self):
        # vin = .capitalize()
        data = {
            'year': str(self.vehYear.get()),
            'make': str(self.vehMake.get()),
            'model': str(self.vehModel.get()),
            'engine': str(self.vehEngine.get()),
            'vin': str(self.vehVin.get()),
            'mileage': str(self.vehMileage.get()),
            'plate': str(self.vehPlate.get()),
            'datecode': str(self.vehDatecode.get()),
        }

        # print(type(data))
        self.db.addVehicle(data)
        # print('Saving...')
        self._updateVehicleList()

    def _clearVehicle(self):
        str(self.vehYear.set(''))
        str(self.vehMake.set(''))
        str(self.vehModel.set(''))
        str(self.vehEngine.set(''))
        str(self.vehVin.set(''))
        str(self.vehMileage.set(''))
        str(self.vehPlate.set(''))
        str(self.vehDatecode.set(''))

    def _updateVehicleList(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        vehicle = self.listVehicle()
        self.parent.children.get('!laborinfoscreen')._update_screen()



    def listVehicle(self):
        vehicles = self.db.getVehicle()
        for row in vehicles:
            self.tv.insert('', 'end', values=(row.vin, row.year, row.make,
                           row.model, row.engine, row.mileage, row.plate, row.datecode))
        # self.listVehicle()

    def decodeVin(self):

        vin = str(self.vehVin.get())
        r = requests.get(
            f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvaluesextended/{vin}?format=json')
        result = r.json()['Results'][0]

        # print(result['DisplacementL'])
        self.vehVin.set(value=result['VIN'])
        self.vehYear.set(value=result['ModelYear'])
        self.vehMake.set(value=result['NCSAMake'])
        self.vehModel.set(value=result['Model'])
        self.vehEngine.set(value=f'{result["DisplacementL"]}L')

    def _removeVehicle(self, vin):
        record = self.tv.selection()[0]
        vin = self.tv.item(record)['values'][0]
        self.db.removeVehicle(vin)
        self._updateVehicleList()

    def get_vin(self):
        return self.vehVin

    def set_vin(self, newVin):
        self.vehVin = newVin

    def obd_get_vin(self):
        if self.con != None:
            resp = self.con.query(obd.commands.VIN)
            print(resp.value.decode())
            self.vehVin.set(resp.value.decode())