import psycopg2
import csv
import psycopg2.extras
import time

start_time = time.time()

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

 #   start_time = time.time()

# Open the CSV file
with open('organizations-100000.csv', 'r') as file:
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()
    # Create a CSV reader object to read the file
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Iterate over the rows in the CSV file
    for row in reader:
        # Insert the row into the database
        cur.execute(
            "INSERT INTO csvdata (inx,organization_id,name,website,country,description,founded,industry,number_of_employees) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            row
        )
    # Commit the changes to the database
    conn.commit()
    # Close the cursor and connection
    print("Data insertion complete.")    
    cur.close()
    conn.close()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The script took {elapsed_time:.2f} seconds to run.")



