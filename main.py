from datetime import datetime
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from person import Person  # Import the Person class from your person module
import src.handlers.databaseHandler as dh

# Load environment variables from dev.env file
load_dotenv("/Users/twu433/omop-on-fhir-v2-python/dev.env")

# Access environment variables
db_username = os.environ.get("DB_USERNAME")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_port = os.environ.get("DB_PORT")
db_schema = os.environ.get("DB_SCHEMA")  # Get the schema from environment

# Construct the database URL with the schema
database_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the SQLAlchemy engine with the schema in connect_args
engine = create_engine(database_url, connect_args={'options': f'-csearch_path={db_schema}'})

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Check if the row with person_id 1000000000 exists before attempting to delete it
row_to_delete = session.query(Person).filter_by(person_id=1000000000).first()
if row_to_delete:
    dh.delete_object(session, table_class=Person, row_id=1000000000)
    print("Delete successful: True")
else:
    print("Row does not exist, no deletion performed")

# List of dictionaries containing data for the first 5 rows
data_to_insert = [
    {
        "person_id": 1000000000,
        "gender_concept_id": 8507,
        "year_of_birth": 1990,
        "month_of_birth": 5,
        "day_of_birth": 15,
        "birth_datetime": datetime(1990, 5, 15, 12, 30, 0),
        "race_concept_id": 8515,
        "ethnicity_concept_id": 38003563,
        "location_id": None,
        "provider_id": 456,
        "care_site_id": 789,
        "person_source_value": "12345",
        "gender_source_value": "M",
        "gender_source_concept_id": 8507,
        "race_source_value": "White",
        "race_source_concept_id": 8515,
        "ethnicity_source_value": "Non-Hispanic",
        "ethnicity_source_concept_id": 38003563,
    },
    # Add data for the other rows
]

# Test your handler functions on the retrieved data
try:
    # Test insert_object
    for data in data_to_insert:
        dh.insert_object(session, table_class=Person, data=data)  # Pass the session here
    print("Insert successful: True")

    # Test update_object
    update_data = {
        "gender_source_value": "F"
    }
    dh.update_object(session, table_class=Person, row_id=1000000000, update_data=update_data)  # Pass the session here
    print("Update deleted:", row_to_delete is not None)
    print("Update present:", session.query(Person).filter_by(person_id=1000000000).first() is not None)

    # Check again if the row with person_id 1000000000 exists before attempting to delete it
    row_to_delete = session.query(Person).filter_by(person_id=1000000000).first()
    if row_to_delete:
        dh.delete_object(session, table_class=Person, row_id=1000000000)
        print("Delete successful: True")
    else:
        print("Row does not exist, no deletion performed")

except Exception as e:
    # Print an error message if the test fails
    print("Error during testing:", e)
