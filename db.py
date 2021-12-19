from db_conf import *
from sqlalchemy import desc
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
        # print(record['year'])
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
            # print(new_record.vin)
            # session.add(new_labor)
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