# Import create_engine
from sqlalchemy import create_engine, Table, MetaData

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///./data/census.sqlite')

# Print table names
print(engine.table_names())

metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

# Reflect the census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables['census']))

# Build select statement for census table: stmt
stmt = 'SELECT * FROM census'

# Execute the statement and fetch the results: results
results = engine.execute(stmt).fetchall()

# Print Results
print(results)

# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

results = engine.execute(stmt).fetchall()
# Execute the statement and print the results
print(results)

# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by using an index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])