from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.sql.sqltypes import Date
from db_conf import Base


class VehInfo(Base):
    
    __tablename__ = "Vehicle"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    year = Column('veh_year', String)
    make = Column('veh_make', String)
    model = Column('veh_model', String)
    engine = Column('veh_engine', String)
    vin = Column('veh_vin', String, unique=True)
    mileage = Column('veh_mileage', String)
    plate = Column('veh_plate', String)
    datecode = Column('veh_datecode', String)
    # labor_id = Column(Integer, ForeignKey('Labor.id'))
    labor = relationship('LaborInfo', order_by='LaborInfo.id')
    # labor = Column(Integer)

    def __init__(self, labor, vin, year='', make='', model='', engine='', mileage='', plate='', datecode=''):
        self.year = year
        self.vin = vin
        self.make = make
        self.model = model
        self.engine = engine
        self.mileage = mileage
        self.plate = plate
        self.datecode = datecode
        self.labor = labor

        def __repr__(self):
            return f'<Vin: {self.vin}, Year: {self.year}, Make: {self.make}, Model: {self.model}, Engine: {self.engine}, Mileage: {self.mileage}, Plate: {self.plate}, Datecode: {self.datecode}>'
        
        def __str__(self):
            return f'<Vin: {self.vin}, Year: {self.year}, Make: {self.make}, Model: {self.model}, Engine: {self.engine}, Mileage: {self.mileage}, Plate: {self.plate}, Datecode: {self.datecode}>'