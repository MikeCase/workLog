from sqlalchemy import Column, Boolean, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db_conf import Base



class DiagInfo(Base):
    __tablename__ = "Diagnostics"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    dg_findings = Column('findings', Text)
    dg_custcomp = Column('complaint', Text)
    dg_mil = Column('mil', Boolean)
    dtc_id = Column(Integer, ForeignKey('DTCs.id'))
    dtc = relationship('DTCInfo', backref="Diagnostics")

    def __init__(self, findings='', custcomp='', mil=False, dtc=None) -> None:
        self.findings = findings
        self.custcomp = custcomp
        self.mil = mil
        self.dtc = dtc
