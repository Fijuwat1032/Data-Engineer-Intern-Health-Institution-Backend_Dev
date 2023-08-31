from sqlalchemy import create_engine, text

# Create an SQLite in-memory database engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Start a transaction and insert data into the database
with engine.begin() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    
    # Query the data within the same context
    result = conn.execute(text("SELECT x, y FROM some_table"))
    
    # Iterate through the query results and print them
    for row in result:
        y = row.y
        # illustrate use with Python f-strings
        print(f"Row: {row.x} {y}")

# The transaction is automatically committed when the context exits successfully
