import tkinter as tk
from tkinter import Entry, StringVar, ttk
import requests
# from Screens.screen_helpers import ScreenHelpers
# from pprint import pprint

from db import DB

class VehicleInfoScreen(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.db = DB()
        padx = 3
        pady = 5
        self.vehYear = StringVar()
        self.vehMake = StringVar()
        self.vehModel = StringVar()
        self.vehEngine = StringVar()
        self.vehVin = StringVar()
        self.vehMileage = StringVar()
        self.vehPlate = StringVar()
        self.vehDatecode = StringVar()


        ## Labels
        lblVehYear = ttk.Label(self, text="Vehicle Year").grid(
            column=0, row=0, padx=padx, pady=pady)
        lblVehMake = ttk.Label(self, text="Vehicle Make").grid(
            column=0, row=1, padx=padx, pady=pady)
        lblVehModel = ttk.Label(self, text="Vehicle Model").grid(
            column=0, row=2, padx=padx, pady=pady)
        lblVehEngine = ttk.Label(self, text="Vehicle Engine").grid(
            column=0, row=3, padx=padx, pady=pady)
        lblVehVin = ttk.Label(self, text="Vehicle Vin").grid(
            column=3, row=0, padx=padx, pady=pady)
        lblVehMileage = ttk.Label(self, text="Vehicle Mileage").grid(
            column=3, row=1, padx=padx, pady=pady)
        lblVehPlate = ttk.Label(self, text="Vehicle Plate").grid(
            column=3, row=2, padx=padx, pady=pady)
        lblVehDateCode = ttk.Label(self, text="Vehicle Date Code").grid(
            column=5, row=0, padx=padx, pady=pady)

        ## Entry boxes
        txtVehYear = Entry(self, textvariable=self.vehYear).grid(
            column=1, row=0, padx=padx, pady=pady)
        txtVehMake = Entry(self, textvariable=self.vehMake).grid(
            column=1, row=1, padx=padx, pady=pady)
        txtVehModel = Entry(self, textvariable=self.vehModel).grid(
            column=1, row=2, padx=padx, pady=pady)
        txtVehEngine = Entry(self, textvariable=self.vehEngine).grid(
            column=1, row=3, padx=padx, pady=pady)
        txtVehVin = Entry(self, textvariable=self.vehVin)
        txtVehVin.bind('<KeyRelease>', lambda x: self._to_upper(vehVin))
        txtVehVin.grid(column=4, row=0, padx=padx, pady=pady)
        txtVehMileage = Entry(self, textvariable=self.vehMileage).grid(
            column=4, row=1, padx=padx, pady=pady)
        txtVehPlate = Entry(self, textvariable=self.vehPlate)
        txtVehPlate.bind('<KeyRelease>', lambda x: self._to_upper(vehPlate))
        txtVehPlate.grid(
            column=4, row=2, padx=padx, pady=pady)
        txtVehDateCode = Entry(self, textvariable=self.vehDatecode).grid(
            column=6, row=0, padx=padx, pady=pady)

        ## Buttons
        btnSaveVehicle = ttk.Button(self, text='Save', command=lambda: self.saveVehicle(
        )).grid(column=3, row=3, padx=padx, pady=pady)
        btnClearVehicle = ttk.Button(self, text='Clear', command=lambda: self.clearVehicle(
        )).grid(column=4, row=3, padx=padx, pady=pady)
        btnDecodeVin = ttk.Button(self, text='Decode', command=lambda: self.decodeVin(
        )).grid(column=5, row=3, padx=padx, pady=pady)
        btnDeleteRecord = ttk.Button(self, text='Remove', command=lambda: self._removeVehicle(self.vehVin.get())).grid(column=6, row=3, padx=padx, pady=pady)

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
        self.tv.grid(column=0, row=4, columnspan=9, sticky='we')
        self.tv.bind('<Double-1>', self.onDoubleClick)

        self.listVehicle()


    # Methods

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
        self.getLabor(self.tv.item(item)['values'][0])

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