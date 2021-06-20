"""
This file is runner each application that was existed
"""

import os
import importlib
import json
import sys

from configparser import ConfigParser

from setting.setting import database, applications, db_models, logger
from utils.command_runner import popen
from runserver.db_base import Session


def runserver():

    '''Check That script run with root user'''
    if os.getuid() != 0:
        logger.critical("Run the server with superuser")
        sys.exit(2)

    for app, value in applications.items():
        if os.path.exists(os.path.join(os.getcwd(), app)):
            try:
                module = importlib.import_module(f'{app}.main')
                _class = getattr(module, f'{value["class"]}')
                _class()
                # logger.info(f"Run {app}")
            except Exception as e:
                logger.warning(f"{str(e)}")
        else:
            logger.critical(f"The {app} directory not found\n")


def reconfigure():
    parser = ConfigParser()
    parser.read('alembic.ini')
    parser.set('alembic', 'sqlalchemy.url', database)
    with open('alembic.ini', 'w') as configfile:
        parser.write(configfile)
    print("[INFO] [Settings has reconfigured successfully\n]")


def make_migration(message):
    cmd = f'alembic revision --autogenerate -m "{message}"'
    popen(cmd)


def migrate():
    cmd = 'alembic upgrade head'
    popen(cmd)


def load_data(file):
    file_path = os.getcwd() + "/fixtures/" + file
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            for item in data:
                try:
                    module = importlib.import_module(f'{item["application"]}.db_models')
                    _class = getattr(module, f'{item["db_model"]}')

                    if "foreign_key" in item["load"]:
                        session = Session()

                        for _fk in item["load"]["foreign_key"]:
                            module = importlib.import_module(f'{_fk["application"]}.db_models')
                            _fk_class = getattr(module, f'{_fk["db_model"]}')
                            _fk_data = session.query(_fk_class).get(_fk["id"])
                            item["load"][_fk["field"]] = _fk_data

                        del item["load"]["foreign_key"]
                        session.add(_class(**item["load"]))
                        session.commit()
                        session.close()

                    else:
                        session = Session()
                        session.add(_class(**item["load"]))
                        session.commit()
                        session.close()

                    print(f"[INFO] [Done!]")

                except Exception as e:
                    print(f"[CRITICAL] [{str(e)}]")
    else:
        print(f"[CRITICAL] [The {file} file not found\n]")


def table_query(path):
    app = path.split(".")[0]
    table = path.split(".")[1]
    try:
        session = Session()
        if app in db_models:
            module = importlib.import_module(f'{app}.db_models')
            _class = getattr(module, table)
            data = session.query(_class).all()
            for d in data:
                print(f'[INFO] [{d.__dict__}]')
            session.close()
        else:
            print(f"[CRITICAL] [Application '{app}' not found]")
    except Exception as e:
        print(f"[CRITICAL] [{str(e)}]")
