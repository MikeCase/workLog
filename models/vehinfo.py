from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from db_conf import Base


class VehInfo(Base):
    __tablename__ = "Vehicle"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    veh_year = Column('veh_year', Date)
    veh_make = Column('veh_make', String)
    veh_model = Column('veh_model', String)
    veh_engine = Column('veh_engine', String)
    veh_vin = Column('veh_vin', String)
    veh_mileage = Column('veh_mileage', String)
    veh_plate = Column('veh_plate', String)
    veh_datecode = Column('veh_datecode', String)
    labor_id = Column(Integer, ForeignKey('Labor.id'))
    labor = relationship('LaborInfo')

    def __init__(self, vin, year='', make='', model='', engine='', mileage='', plate='', datecode='', labor=None ):
        self.year = year
        self.vin = vin
        self.make = make
        self.model = model
        self.engine = engine
        self.mileage = mileage
        self.plate = plate
        self.date_code = datecode
        self.labor = labor

    def addRecord(self):
        pass