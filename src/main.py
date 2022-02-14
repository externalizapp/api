#!/usr/bin/env python

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/api/tenders/{id}', response_model=schemas.Tender)
async def read_tender(id: int, db: Session = Depends(get_db)):
    tender = crud.get_tender(db, id=id)
    if tender is None:
        raise HTTPException(status_code=404, detail="Tender not found")
    return tender

@app.get('/api/tenders/', response_model=list[schemas.Tender])
async def read_tenders(db: Session = Depends(get_db), q: str | None = None):
    tenders = crud.get_tenders(db, q)
    if tenders is None:
        raise HTTPException(status_code=404, detail="Tender not found")
    return tenders
