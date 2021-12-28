from db_conf import *
from sqlalchemy import desc
from pprint import pprint
from datetime import datetime
from models.vehinfo import VehInfo
from models.diaginfo import DiagInfo
from models.dtcinfo import DTCInfo
from models.laborinfo import LaborInfo


class DB:
    def __init__(self) -> None:
        Base.metadata.create_all(bind=engine)
        self.session = db_session

    def getComplete(self):
        # print(session.query(VehInfo).all())
        pass

    def addVehicle(self, record):
        '''Add or update a vehicle record. 
           First check to see if a record with the corresponding vin exists, if so 
           update the record, otherwise create a new record.
        '''

        existing_record = session.query(VehInfo).filter_by(vin=record['vin']).first()
        if existing_record:
            existing_record.vin = record['vin']
            existing_record.year = record['year']
            existing_record.make = record['make']
            existing_record.model = record['model']
            existing_record.engine = record['engine']
            existing_record.mileage = record['mileage']
            existing_record.plate = record['plate']
            existing_record.datecode = record['datecode']
            session.commit()
            print('Updated Record')
        else:
            new_labor = LaborInfo('First job', 'First job', datetime.now())
            new_record = VehInfo([new_labor], record["vin"], year=record["year"], make=record["make"], model=record["model"],
                                engine=record["engine"], mileage=record["mileage"], plate=record["plate"], datecode=record["datecode"])
            
            session.add(new_record)
            session.commit()
            print(f'Added {record}')

    def getVehicle(self):
        vehicle = session.query(VehInfo).all()
        return vehicle
        
    def getNewVehicles(self):
        vehicle = session.query(VehInfo).order_by(desc(VehInfo.id)).first()
        if vehicle != None:
            return vehicle

    def removeVehicle(self, VehicleVin):
        vehicle = session.query(VehInfo).filter_by(vin = VehicleVin).first()
        session.delete(vehicle)
        session.commit()

    def getLabor(self, id):
        # print(f'{self.vin_to_id(id)} - getlabor method')
        record = session.query(VehInfo).filter(VehInfo.labor.any(vehicle_id = self.vin_to_id(id))).all()
        # print(record)
        if record != None:
            print(record[0].labor[0].vehicle_id)
            print(record[0].labor[0].job)
            print(record[0].id)
            return record

    def vin_to_id(self, current_vin):
        # print(f'{current_vin} - vin_to_id method')
        id = session.query(VehInfo).filter(VehInfo.vin.__eq__(current_vin)).first()
        return id.id