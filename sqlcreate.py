import pymysql as pms

try:
    # Establish a connection to the MySQL database
    con = pms.connect(
        user='root',
        host='localhost',
        database='zomato',
        password='tiger'  # Corrected parameter name
    )

    # Check if the connection is successful
    if con.open:
        print("Connection successful.")

    # Create a cursor object
    cur = con.cursor()

    # Execute a CREATE TABLE query
    create_table_query = """
        CREATE TABLE IF NOT EXISTS product (
            product_id INT PRIMARY KEY,
            product_name VARCHAR(100),
            price INT
        );
    """
    cur.execute(create_table_query)
    print("Table created successfully.")

    # Commit the changes
    con.commit()

except pms.MySQLError as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cur' in locals() and cur:
        cur.close()
    if 'con' in locals() and con.open:
        con.close()
    print("Connection closed.")





