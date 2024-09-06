# OMOP-on-FHIR v2 Python

## Overview

This repository provides a Python-based solution for interacting with a PostgreSQL database for the OMOP-on-FHIR v2 framework, focusing on automated handling of healthcare data such as patient records. Using SQLAlchemy as the ORM (Object Relational Mapper) and environment configurations with `dotenv`, this project supports database operations like inserting, updating, and deleting patient records seamlessly.

## Table of Contents
- [Project Description](#project-description)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Operations](#database-operations)
  - [Insert Operation](#insert-operation)
  - [Update Operation](#update-operation)
  - [Delete Operation](#delete-operation)
- [Usage Example](#usage-example)
- [Acknowledgments](#acknowledgments)

## Project Description

The **OMOP-on-FHIR v2 Python** project automates various database operations related to healthcare data management, specifically under the OMOP-on-FHIR standard. The project focuses on managing patient records within a PostgreSQL database using SQLAlchemy for ORM. Key functionalities include:

- Automated environment handling using `.env` files.
- Automated operations for adding, updating, and deleting records in a structured, clean, and reusable way.
- A sample implementation with Python classes that maps to the OMOP standard schema.

## Key Features

- **Environment Variable Management**: Environment variables are loaded from a `.env` file for secure handling of database credentials and other sensitive information.
  
- **ORM with SQLAlchemy**: SQLAlchemy's ORM capabilities are used for mapping Python classes to database tables, enabling easy interaction with the PostgreSQL database.

- **CRUD Operations**: Provides functionality to perform Create, Read, Update, and Delete operations using clean, reusable handler functions for common database actions.

- **Error Handling**: Includes basic error handling to manage database transaction failures.

## Requirements

The project requires the following:

- **Python 3.x**
- **PostgreSQL** database
- Python libraries:
  - `sqlalchemy`
  - `psycopg2`
  - `python-dotenv`
  - `pandas`
  - `numpy`

You can install these dependencies via `pip`:

```bash
pip install sqlalchemy psycopg2 python-dotenv pandas numpy
```

## Installation

1. **Clone the Repository**:

   Clone the repository to your local machine:

   ```bash
   git clone https://gitlab.gtri.gatech.edu/icl-heatd/omoponfhir/omop-on-fhir-v2/omop-on-fhir-v2-python.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd omop-on-fhir-v2-python
   ```

3. **Install the Required Libraries**:

   Use `pip` to install all dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Environment**:

   Create a `.env` file in the root directory of the project. You can use the `dev.env` file provided as an example and configure it to your environment.

## Environment Variables

The project loads environment variables using the `dotenv` library. Create a `.env` file at the root of your project and add your PostgreSQL database credentials like this:

```
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_NAME=your_database_name
DB_PORT=5432
DB_SCHEMA=your_schema
```

These variables are accessed in the script to connect to your PostgreSQL database securely.

## Database Operations

### Insert Operation

The `insert_object` function allows you to insert data into the database for any specified table class.

```python
def insert_object(session, table_class, data):
    new_object = table_class(**data)
    session.add(new_object)
    session.commit()
```

### Update Operation

The `update_object` function updates existing rows in the database based on a specified row ID.

```python
def update_object(session, table_class, row_id, update_data):
    object_to_update = session.query(table_class).get(row_id)
    if object_to_update:
        for key, value in update_data.items():
            setattr(object_to_update, key, value)
        session.commit()
```

### Delete Operation

The `delete_object` function deletes a row from the specified table class using a row ID.

```python
def delete_object(session, table_class, row_id):
    object_to_delete = session.query(table_class).get(row_id)
    if object_to_delete:
        session.delete(object_to_delete)
        session.commit()
```

## Usage Example

Here’s an example workflow for inserting, updating, and deleting a `Person` record in the OMOP schema:

1. **Insert a New Record**:

   ```python
   data = {
       "person_id": 1000000000,
       "gender_concept_id": 8507,
       "year_of_birth": 1990,
       "month_of_birth": 5,
       "day_of_birth": 15,
       "birth_datetime": datetime(1990, 5, 15, 12, 30, 0),
       "race_concept_id": 8515,
       "ethnicity_concept_id": 38003563
   }

   insert_object(session, Person, data)
   ```

2. **Update an Existing Record**:

   ```python
   update_data = {
       "gender_source_value": "F"
   }

   update_object(session, Person, row_id=1000000000, update_data=update_data)
   ```

3. **Delete a Record**:

   ```python
   delete_object(session, Person, row_id=1000000000)
   ```

## Acknowledgments

This project is part of the **OMOP-on-FHIR** initiative and is a collaborative effort to standardize healthcare data operations using Python. Special thanks to the contributors and project maintainers for their guidance and support.
