from sqlalchemy import create_engine
from models.talent import Base, Talent
from sqlalchemy.orm import sessionmaker
import os
import ijson

DATA_FILE_PATH = os.path.join(os.getcwd(), '', 'app\data\planning.json')


def createEngine():
    engine = create_engine("sqlite:///planning.db", echo=True)
    return engine


def importTalent():
    engine = createEngine()
    Talent.__table__.drop(engine, checkfirst=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    with open(DATA_FILE_PATH, 'r') as f:
        for talent in ijson.items(f, 'item'):
            currentTalent = Talent(talent)
            session.add(currentTalent)

    session.commit()
    session.close()
