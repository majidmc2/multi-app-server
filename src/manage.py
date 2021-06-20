import argparse
import sys
from runserver.run import runserver, migrate, make_migration, reconfigure, load_data, table_query
from setting.setting import logger


def main():
    # Define arguments
    parser = argparse.ArgumentParser(description='__Server of the messenger__')
    parser.add_argument('--reconfigure', action='store_true', default=False, dest='RECONFIGURE', help='Reconfigure settings')
    parser.add_argument('--runserver', action='store_true', default=False, dest='RUN', help='Run the server')
    parser.add_argument('--migrate', action='store_true', default=False, dest='MIGRATE', help='Migrate database')
    parser.add_argument('--makemigration', action='store', default=False, dest='MAKEMIGRATATION', help='Change header of migration')
    parser.add_argument('--loaddata', action='store', default=False, dest='LOADDATA', help='Load Json data file to Data base')
    parser.add_argument('--tquery', action='store', default=False, dest='TQUERY', help='Select every records of a table')
    arguments = vars(parser.parse_args())

    if arguments['RUN']:
        runserver()
    elif arguments['MAKEMIGRATATION']:
        make_migration(arguments['MAKEMIGRATATION'])
    elif arguments['MIGRATE']:
        migrate()
    elif arguments['RECONFIGURE']:
        reconfigure()
    elif arguments['LOADDATA']:
        load_data(arguments['LOADDATA'])
    elif arguments['TQUERY']:
        table_query(arguments['TQUERY'])
    else:
        logger.critical("Use 'manage.py -h'\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
