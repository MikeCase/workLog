from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from db_conf import Base



class LaborInfo(Base):
    __tablename__ = "Labor"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    lb_job = Column('job_desc', Text)
    lb_booktime = Column('booktime', String)
    lb_start = Column('start', DateTime)
    lb_finished = Column('finished', DateTime)
    diag_id = Column(Integer, ForeignKey('diagnostics.id'))
    
    vehicle = relationship('VehInfo', uselist=False, backref='vehicle')
    
    def __init__(self, job, booktime, start,  diag=None, finish='',) -> None:
        self.job = job
        self.boottime = booktime
        self.start = start
        self.finish = finish
        self.diag = diag