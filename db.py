from db_conf import session
from models.vehinfo import VehInfo
from models.diaginfo import DiagInfo
from models.dtcinfo import DTCInfo
from models.laborinfo import LaborInfo

class DB:
    def __init__(self) -> None:
        pass

    def getComplete(self):
        # print(session.query(VehInfo).all())
        pass

    def addVehicle(self, record):
        record = VehInfo(
            f'{record["vin"]}',
            f'{record["year"]}',
            f'{record["make"]}',
            f'{record["model"]}',
            f'{record["engine"]}',
            f'{record["mileage"]}',
            f'{record["plate"]}',
            f'{record["datecode"]}', 
            )
        session.add(record)
        
        print(f'Added {record}')