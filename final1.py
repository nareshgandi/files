import csv
import psycopg2
import psycopg2.extras
import time

start_time = time.time()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

# Open the CSV file and read its contents
with open('organizations-100000.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = list(reader)

# Define the SQL query to insert the data into the database
query = 'INSERT INTO csvdata (inx,organization_id,name,website,country,description,founded,industry,number_of_employees) VALUES %s'

# Execute the query with the data
#with conn.cursor() as cursor:
 #   psycopg2.extras.execute_values(cursor, query, data, page_size=100)
  #  conn.commit()
#print("Data insertion complete.")


# Set the page size to 1000
page_size = 1000

# Execute the query with the data
with conn.cursor() as cursor:
    for i in range(0, len(data), page_size):
        print(f"Inserting rows {i} to {i+page_size-1}")
        psycopg2.extras.execute_values(cursor, query, data[i:i+page_size])
        conn.commit()


    # Close the cursor and connection
    print("Data insertion complete.")
#    conn.close()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The script took {elapsed_time:.2f} seconds to run.")



# Close the database connection
conn.close()
