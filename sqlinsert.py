import mysql.connector

# Establish a connection to the MySQL database
con = mysql.connector.connect(
    user='root',
    host='localhost',
    database='zomato',
    password='tiger'  # Corrected parameter name
)

# Check if the connection is successful
print("Connection successful:", con.is_connected())

# Create a cursor object
cur = con.cursor()

# Insert multiple rows into the `product` table
insert_query = '''
    INSERT INTO product(product_id, product_name, price) 
    VALUES (%s, %s, %s)
'''
values = [
    (1, 'p1', 980),
    (2, 'p2', 870),
    (3, 'p3', 330)
]

try:
    # Execute the insert query
    cur.executemany(insert_query, values)

    # Commit the transaction
    con.commit()
    print("Data inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    con.rollback()  # Rollback in case of an error

finally:
    # Close the cursor and connection
    cur.close()
    con.close()
    print("Connection closed.")
