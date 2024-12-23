import pymysql as p

try:
    # Establish a connection to the MySQL database
    con = p.connect(
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

    # Execute a SELECT query with proper multiline formatting
    query = """
        SELECT s.userid, SUM(p.price) AS total_amt_spent FROM sale s INNER JOIN product p ON s.product_id = p.product_id
        GROUP BY s.userid;
            """
    cur.execute(query)

    # Fetch and print the results
    rows = cur.fetchall()
    print("Query results:")
    for row in rows:
        print(f"User ID: {row[0]}, Total Amount Spent: {row[1]}")

except p.MySQLError as err:
    print(f"Database error: {err}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure cursor and connection are closed properly
    if 'cur' in locals() and cur:
        cur.close()
    if 'con' in locals() and con.open:
        con.close()
    print("Connection closed.")
