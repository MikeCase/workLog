from tkinter import StringVar, ttk
from typing import Text

from db import DB

class VehicleInfoScreen:
    def __init__(self, frame) -> None:
        self.db = DB()
        self.padx = 3
        self.pady = 5
        self.vehYear = StringVar(value="2010")
        self.vehMake = StringVar(value="Toyota")
        self.vehModel = StringVar(value="Tacoma")
        self.vehEngine = StringVar(value="2.7l")
        self.vehVin = StringVar(value="12345678901234567")
        self.vehMileage = StringVar(value="192089")
        self.vehPlate = StringVar(value="l33t1")
        self.veh_date_code = StringVar(value="04/10")


        self.lblVehYear = ttk.Label(frame, text="Vehicle Year").grid(column=0, row=0, padx=self.padx, pady=self.pady)
        self.lblVehMake = ttk.Label(frame, text="Vehicle Make").grid(column=0, row=1, padx=self.padx, pady=self.pady)
        self.lblVehModel = ttk.Label(frame, text="Vehicle Model").grid(column=0, row=2, padx=self.padx, pady=self.pady)
        self.lblVehEngine = ttk.Label(frame, text="Vehicle Engine").grid(column=0, row=3, padx=self.padx, pady=self.pady)
        self.lblVehVin = ttk.Label(frame, text="Vehicle Vin").grid(column=3, row=0, padx=self.padx, pady=self.pady)
        self.lblVehMileage = ttk.Label(frame, text="Vehicle Mileage").grid(column=3, row=1, padx=self.padx, pady=self.pady)
        self.lblVehPlate = ttk.Label(frame, text="Vehicle Plate").grid(column=3, row=2, padx=self.padx, pady=self.pady)
        self.lblVehDateCode = ttk.Label(frame, text="Vehicle Date Code").grid(column=6, row=2, padx=self.padx, pady=self.pady)

        self.txtVehYear = ttk.Entry(frame, textvariable=self.vehYear).grid(column=1, row=0, padx=self.padx, pady=self.pady)
        self.txtVehMake = ttk.Entry(frame, textvariable=self.vehMake).grid(column=1, row=1, padx=self.padx, pady=self.pady)
        self.txtVehModel = ttk.Entry(frame, textvariable=self.vehModel).grid(column=1, row=2, padx=self.padx, pady=self.pady)
        self.txtVehEngine = ttk.Entry(frame, textvariable=self.vehEngine).grid(column=1, row=3, padx=self.padx, pady=self.pady)
        self.txtVehVin = ttk.Entry(frame, textvariable=self.vehVin).grid(column=4, row=0, padx=self.padx, pady=self.pady)
        self.txtVehMileage = ttk.Entry(frame, textvariable=self.vehMileage).grid(column=4, row=1, padx=self.padx, pady=self.pady)
        self.txtVehPlate = ttk.Entry(frame, textvariable=self.vehPlate).grid(column=4, row=2, padx=self.padx, pady=self.pady)
        self.txtVehDateCode = ttk.Entry(frame, textvariable=self.veh_date_code).grid(column=7, row=2, padx=self.padx, pady=self.pady)

        self.btnSaveVehicle = ttk.Button(frame, text='Save', command=lambda: self.saveVehicle()).grid(column=3, row=3, padx=self.padx, pady=self.pady)
        self.btnClearVehicle = ttk.Button(frame, text='Clear', command=lambda: self.clearVehicle()).grid(column=4, row=3, padx=self.padx, pady=self.pady)

        self.tv = ttk.Treeview(frame)
        self.tv['columns'] = ('VIN', 'Year', 'Make', 'Model', 'Engine', 'Mileage', 'Plate', 'Datecode')
        self.tv.column('#0', width=0, stretch='NO')
        self.tv.column('VIN', anchor='w', width=80)
        self.tv.column('Year', anchor='center', width=10)
        self.tv.column('Make', anchor='center', width=60)
        self.tv.column('Model', anchor='center', width=60)
        self.tv.column('Engine', anchor='center', width=20)
        self.tv.column('Mileage', anchor='center', width=40)
        self.tv.column('Plate', anchor='center', width=20)
        self.tv.column('Datecode', anchor='w', width=15)
        
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
        
        self.listVehicle()

    def saveVehicle(self):
        data = {
            'year': str(self.vehYear.get()),
            'make': str(self.vehMake.get()),
            'model': str(self.vehModel.get()),
            'engine': str(self.vehEngine.get()),
            'vin': str(self.vehVin.get()),
            'mileage': str(self.vehMileage.get()),
            'plate': str(self.vehPlate.get()),
            'datecode': str(self.veh_date_code.get()),
        }
        print(type(data))
        self.db.addVehicle(data)
        print('Saving...')

    def clearVehicle(self):
        str(self.vehYear.set(''))
        str(self.vehMake.set(''))
        str(self.vehModel.set(''))
        str(self.vehEngine.set(''))
        str(self.vehVin.set(''))
        str(self.vehMileage.set(''))
        str(self.vehPlate.set(''))

    def listVehicle(self):
        vehicles = self.db.getVehicle()
        for row in vehicles:
            self.tv.insert('', 'end', values=(row.vin, row.year, row.make, row.model, row.engine, row.mileage, row.plate, row.datecode))