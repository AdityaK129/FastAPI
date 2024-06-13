from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
import uvicorn
from .utils import logging  # Importing the logging setup

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/create_configuration/", response_model=schemas.Configuration)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(database.get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db, config=config)

@app.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(database.get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@app.post("/update_configuration/", response_model=schemas.Configuration)
def update_configuration(config: schemas.ConfigurationUpdate, db: Session = Depends(database.get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.update_configuration(db, config=config)

@app.delete("/delete_configuration/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(database.get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.delete_configuration(db, country_code=country_code)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
