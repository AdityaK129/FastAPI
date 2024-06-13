from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class CountryConfiguration(Base):
    __tablename__ = "country_configurations"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True, nullable=False)
    configuration = Column(JSON, nullable=False)
