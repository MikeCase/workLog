import tkinter as tk
from tkinter import Entry, StringVar, ttk
import requests
from sqlalchemy.sql.expression import column
# from Screens.screen_helpers import ScreenHelpers
from pprint import pprint

from db import DB

class VehicleInfoScreen(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        pprint(dir(parent))
        self.parent = parent
        self.db = DB()
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
        self.button(self, text='Clear', command=lambda: self.clearVehicle(), gridcol=4, gridrow=3)
        self.button(self, text='Decode', command=lambda: self.decodeVin(), gridcol=5, gridrow=3)
        self.button(self, text='Remove', command=lambda: self._removeVehicle(self.vehVin.get()), gridcol=6, gridrow=3)

        ## Treeview
        self.tv = ttk.Treeview(self)

        self.tv['columns'] = ('VIN', 'Year', 'Make', 'Model',
                      'Engine', 'Mileage', 'Plate', 'Datecode')
        self.tv.column('#0', width=0, stretch='NO')
        self.tv.column('VIN', anchor='w', width=80)
        self.tv.column('Year', anchor='center', width=10)
        self.tv.column('Make', anchor='center', width=60)
        self.tv.column('Model', anchor='center', width=60)
        self.tv.column('Engine', anchor='center', width=20)
        self.tv.column('Mileage', anchor='center', width=40)
        self.tv.column('Plate', anchor='center', width=20)
        self.tv.column('Datecode', anchor='w', width=15)

        ## Heading rows
        self.tv.heading('#0', text='', anchor='center')
        self.tv.heading('VIN', text='VIN', anchor='center')
        self.tv.heading('Year', text="Year", anchor='center')
        self.tv.heading('Make', text="Make", anchor='center')
        self.tv.heading('Model', text="Model", anchor='center')
        self.tv.heading('Engine', text="Engine", anchor='center')
        self.tv.heading('Mileage', text="Mileage", anchor='center')
        self.tv.heading('Plate', text="Plate", anchor='center')
        self.tv.heading('Datecode', text="Datecode", anchor='center')
        self.tv.bind('<Double-1>', self.onDoubleClick)
        self.tv.grid(column=0, row=4, columnspan=9, sticky='we')

        self.listVehicle()


    # Methods

    def button(self, parent, text, command, gridrow, gridcol):
        button = ttk.Button(parent, text=text, command=command)
        button.grid(column=gridcol, row=gridrow, padx=self.padx, pady=self.pady)

    def label(self, parent, text, row, column, binder=None):
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
        args[0].set(args[0].get().upper())

    def onDoubleClick(self, event):
        item = self.tv.selection()[0]
        self.vehVin.set(value=self.tv.item(item)['values'][0])
        self.vehYear.set(value=self.tv.item(item)['values'][1])
        self.vehMake.set(value=self.tv.item(item)['values'][2])
        self.vehModel.set(value=self.tv.item(item)['values'][3])
        self.vehEngine.set(value=self.tv.item(item)['values'][4])
        self.vehMileage.set(value=self.tv.item(item)['values'][5])
        self.vehPlate.set(value=self.tv.item(item)['values'][6])
        self.vehDatecode.set(value=self.tv.item(item)['values'][7])
        # self.getLabor(self.tv.item(item)['values'][0])

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

    def clearVehicle(self):
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