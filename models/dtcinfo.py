from sqlalchemy import Column, Integer, String, Text
from db_conf import Base



class DTCInfo(Base):
    __tablename__ = "DTCs"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    dtc_code = Column('dtc_code', String)
    dtc_info = Column('dtc_desc', Text)

    def __init__(self, dtc_code, dtc_info) -> None:
        self.dtc_code = dtc_code
        self.dtc_info = dtc_info