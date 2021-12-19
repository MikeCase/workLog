from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from models.vehinfo import VehInfo

from db_conf import Base



class LaborInfo(Base):
    __tablename__ = "Labor"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    job = Column('job_desc', Text)
    booktime = Column('booktime', String)
    start = Column('start', DateTime)
    finished = Column('finished', DateTime)
    # diag_id = Column(Integer, ForeignKey('Diagnostics.id'))
    vehicle_id = Column(Integer, ForeignKey('Vehicle.id'))
    # vehicle = relationship('VehInfo', uselist=False, back_populates="Labor")
    
    def __init__(self, job, booktime, start,  diag=None, finish='',) -> None:
        self.job = job
        self.boottime = booktime
        self.start = start
        self.finish = finish
        self.diag = diag