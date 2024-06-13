from sqlalchemy.orm import Session
from . import models, schemas

def create_configuration(db: Session, config: schemas.ConfigurationCreate):
    db_config = models.CountryConfiguration(country_code=config.country_code, configuration=config.configuration)
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_configuration(db: Session, country_code: str):
    return db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()

def update_configuration(db: Session, config: schemas.ConfigurationUpdate):
    db_config = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == config.country_code).first()
    if db_config:
        db_config.configuration = config.configuration
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_configuration(db: Session, country_code: str):
    db_config = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()
    if db_config:
        db.delete(db_config)
        db.commit()
    return db_config
