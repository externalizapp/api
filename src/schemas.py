#!/usr/bin/env python

from pydantic import BaseModel, Json

class Award(BaseModel):
    id_supplier: int
    name: str
    value: float
    date: str

    class Config:
        orm_mode = True

class Tender(BaseModel):
    id_purchaser: int
    id_tender: int
    id_platform: int

    title: str
    purchaser: str

    file_number: str
    source: str
    platform: str
    awards: list[Award]

    class Config:
        orm_mode = True
