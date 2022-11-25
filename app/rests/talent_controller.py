from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException
from fastapi import Depends, FastAPI
from models.talent import Talent, Talent_Response
from fastapi_pagination import Page, Params, paginate
from typing import Union


engine = create_engine('sqlite:///planning.bd', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
tags_metadata = []
app = FastAPI(tags_metadata)


@app.get("/talents/sorted", response_model=Page[Talent_Response], tags=["sorted"])
def sorting(params: Params = Depends(), startDate: Union[str, None] = None, endDate: Union[str, None] = None):
    if (startDate and endDate) or (not startDate and not endDate):
        raise HTTPException(
            status_code=400, detail="")

    if startDate:
        if startDate == 'asc':
            results = session.query(Talent).order_by(
                Talent.start_date.asc()).all()
        elif startDate == 'desc':
            results = session.query(Talent).order_by(
                Talent.start_date.desc()).all()
    elif endDate:
        if endDate == 'asc':
            results = session.query(Talent).order_by(
                Talent.end_date.asc()).all()
        elif endDate == 'desc':
            results = session.query(Talent).order_by(
                Talent.end_date.desc()).all()

    return paginate(results, params)


tags_metadata = []
