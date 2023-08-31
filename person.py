from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    person_id = Column(Integer, primary_key=True)
    gender_concept_id = Column(Integer)
    year_of_birth = Column(Integer)
    month_of_birth = Column(Integer)
    day_of_birth = Column(Integer)
    birth_datetime = Column(DateTime)
    race_concept_id = Column(Integer)
    ethnicity_concept_id = Column(Integer)
    location_id = Column(Integer)
    provider_id = Column(Integer)
    care_site_id = Column(Integer)
    person_source_value = Column(String)
    gender_source_value = Column(String)
    gender_source_concept_id = Column(Integer)
    race_source_value = Column(String)
    race_source_concept_id = Column(Integer)
    ethnicity_source_value = Column(String)
    ethnicity_source_concept_id = Column(Integer)
    time_of_birth = Column(DateTime)  # Add the time_of_birth attribute
