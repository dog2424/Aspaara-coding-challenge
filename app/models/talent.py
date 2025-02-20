from sqlalchemy import Column, String, Integer, Boolean, DateTime, Float, JSON
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import mapper
from pydantic import BaseModel

Base = declarative_base()


class Talent(Base):
    __tablename__ = "talents"

    id = Column(Integer(), primary_key=True)
    original_id = Column(String(255), unique=True, nullable=False)
    talent_id = Column(String(255))
    talent_name = Column(String(255))
    talent_grade = Column(String(255))
    booking_grade = Column(String(255))
    operating_unit = Column(String(255), nullable=False)
    office_city = Column(String(255))
    office_postal_code = Column(String(255), nullable=False)
    job_manager_name = Column(String(255))
    job_manager_id = Column(String(255))
    total_hours = Column(Float(), nullable=False)
    start_date = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    end_date = Column(DateTime(timezone=True),
                      server_default=func.now(), nullable=False)
    client_name = Column(String(255))
    client_id = Column(String(255), nullable=False)
    industry = Column(String(255))
    required_skills = Column(JSON)
    optional_skills = Column(JSON)
    is_unassigned = Column(Boolean())

    def __init__(self, talent):
        self.id = talent['id']
        self.original_id = talent['originalId']
        self.talent_id = talent['talentId']
        self.talent_name = talent['talentName']
        self.talent_grade = talent['talentGrade']
        self.booking_grade = talent['bookingGrade']
        self.operating_unit = talent['operatingUnit']
        self.office_city = talent['officeCity']
        self.office_postal_code = talent['officePostalCode']
        self.job_manager_name = talent['jobManagerName']
        self.job_manager_id = talent['jobManagerId']
        self.total_hours = talent['totalHours']
        self.start_date = datetime.strptime(
            talent['startDate'], '%m/%d/%Y %I:%M %p')
        self.end_date = datetime.strptime(
            talent['endDate'], '%m/%d/%Y %I:%M %p')
        self.client_name = talent['clientName']
        self.client_id = talent['clientId']
        self.industry = talent['industry']
        self.required_skills = talent['requiredSkills']
        self.optional_skills = talent['optionalSkills']
        self.is_unassigned = talent['isUnassigned']


class Talent_Response(BaseModel):
    id: int
    original_id: str
    talent_id: str
    talent_name: str
    talent_grade: str
    booking_grade: str
    operating_unit: str
    office_city: str
    office_postal_code: str
    job_manager_name: str
    job_manager_id: str
    total_hours: float
    start_date: datetime
    end_date: datetime
    client_name: str
    client_id: str
    industry: str
    required_skills: object
    optional_skills: object
    is_unassigned: bool

    class Config:
        orm_mode = True
