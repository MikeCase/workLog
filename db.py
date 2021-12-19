from db_conf import *
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
        new_labor = LaborInfo('First job', 'First job', datetime.now())
        new_record = VehInfo([new_labor], record["vin"], year=record["year"], make=record["make"], model=record["model"],
                             engine=record["engine"], mileage=record["mileage"], plate=record["plate"], datecode=record["datecode"])
        # print(new_record.vin)
        # session.add(new_labor)
        session.add(new_record)
        session.commit()
        print(f'Added {record}')

    def getVehicle(self):
        vehicles = session.query(VehInfo).all()
        return vehicles
        