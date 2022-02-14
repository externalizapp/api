#!/usr/bin/env python

from sqlalchemy.orm import Session
from sqlalchemy import func, Column
from sqlalchemy.dialects import postgresql

from . import models, schemas

def get_tender(db: Session, id: int):
    return db.query(models.Tender).filter(models.Tender.id_tender == id).first()

def get_tenders(db: Session, q: str | None = None):
    if q:
        '''
        SELECT *
        FROM tenders c, json_array_elements(c.awards) aws
        WHERE c.title ILIKE '%q%'
        OR aws->>'name' ILIKE '%q%';
        '''
        award = Column('award', type_=postgresql.JSON)
        q = db.query(models.Tender).\
            select_from(
                models.Tender,
                func.json_array_elements(models.Tender.awards).alias('award')).\
            filter(
                award['name'].astext.ilike(f'%{q}%') |
                models.Tender.title.ilike(f'%{q}%'))

        # DEBUG
        # print(str(q.statement.compile(dialect=postgresql.dialect())))
        return q.all()

    return db.query(models.Tender).all()
