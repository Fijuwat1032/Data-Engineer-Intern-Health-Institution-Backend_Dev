# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# # from your_models_module import Base, YourTableClass  # Import your models

# # Create an SQLite in-memory database engine
# engine = create_engine("sqlite+pysqlite:///:memory:")

# # Create a session factory
# Session = sessionmaker(bind=engine)
# session = Session()

# def insert_object(table_class, data):
#     """Insert a new row into the specified table."""
#     new_object = table_class(**data)  # Create a new instance of the table class
#     session.add(new_object)           # Add the object to the session
#     session.commit()                  # Commit the transaction

# def update_object(table_class, row_id, update_data):
#     """Update an existing row in the specified table."""
#     object_to_update = session.query(table_class).get(row_id)
#     if object_to_update:
#         for key, value in update_data.items():
#             setattr(object_to_update, key, value)
#         session.commit()

# def delete_object(table_class, row_id):
#     """Delete a row from the specified table."""
#     object_to_delete = session.query(table_class).get(row_id)
#     if object_to_delete:
#         session.delete(object_to_delete)
#         session.commit()

def insert_object(session, table_class, data):
    """Insert a new row into the specified table."""
    new_object = table_class(**data)
    session.add(new_object)
    session.commit()

def update_object(session, table_class, row_id, update_data):
    """Update an existing row in the specified table."""
    object_to_update = session.query(table_class).get(row_id)
    if object_to_update:
        for key, value in update_data.items():
            setattr(object_to_update, key, value)
        session.commit()

def delete_object(session, table_class, row_id):
    """Delete a row from the specified table."""
    object_to_delete = session.query(table_class).get(row_id)
    if object_to_delete:
        session.delete(object_to_delete)
        session.commit()

