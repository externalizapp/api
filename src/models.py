#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSON

from .database import Base

class Tender(Base):
    __tablename__ = 'tenders'

    id_purchaser = Column(Integer, primary_key=True)
    id_tender = Column(Integer, primary_key=True)
    id_platform = Column(Integer, primary_key=True)

    title = Column(String)
    purchaser = Column(String)

    file_number = Column(String)
    source = Column(String)
    platform = Column(String)
    awards = Column(JSON)
