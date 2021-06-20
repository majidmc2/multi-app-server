import importlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting.setting import database, db_models


engine = create_engine(database)

Session = sessionmaker(bind=engine)

Base = declarative_base()


"""
https://stackoverflow.com/a/9089671/9956693
"""
for __app, _ in db_models.items():
    importlib.import_module(f'{__app}.db_models')
