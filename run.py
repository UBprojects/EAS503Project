from helpers import database as db_helper
from ingestion import populate_data

db_helper.create_db_schema()

populate_data()
