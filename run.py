import ingestion
from helpers import database as db_helper

db_helper.create_db_schema()

# while True:
#     ingestion.populate_incremental_data(offset=10000)

ingestion.parse_json_files()
