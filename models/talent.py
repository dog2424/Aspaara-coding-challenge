from sqlalchemy import Column, String, Integer, Boolean, DateTime, Float, JSON


class Talent():

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
                        server_default=DateTime.now(), nullable=False)
    end_date = Column(DateTime(timezone=True),
                      server_default=DateTime.now(), nullable=False)
    client_name = Column(String(255))
    client_id = Column(String(255), nullable=False)
    industry = Column(String(255))
    required_skills = Column(JSON)
    optional_skills = Column(JSON)
    is_unassigned = Column(Boolean())
