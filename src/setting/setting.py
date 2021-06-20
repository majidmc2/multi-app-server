"""
This file is all settings for run server
"""
import logging


DEBUG = True


applications = {
    "example_UDP_app": {
        "class": "UDPProtocol",
        "configurations": {
            "local_address": "192.168.1.60",
            "port": 9999,
            "text": "Hello, World!"
        }
    },
}


database = "postgresql://USER:PASS@localhost:5432/TABLE"


db_models = {
	"example_UDP_app": ["UDP"]
    "example_messages_app": ["Message"],
    "example_users_app": ["User"]
}


if DEBUG:
    logging.basicConfig(
        datefmt='%Y/%m/%d %I:%M:%S %p',
        format='[%(levelname)s] [%(asctime)s] [%(message)s]',
        level=logging.DEBUG
    )
else:
    logging.basicConfig(
        filename='server.log',
        datefmt='%Y/%m/%d %I:%M:%S %p',
        format='[%(levelname)s] [%(asctime)s] [%(message)s]',
        level=logging.DEBUG
    )
logger = logging.getLogger()
