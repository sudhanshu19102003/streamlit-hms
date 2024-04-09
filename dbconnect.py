import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    port="3306",
    user="debdut",
    password="GUDDUdebdut007",
    database="hmsystem"
)

mycursor = mydb.cursor()

# Check if the table exists
mycursor.execute("SHOW TABLES LIKE 'bookings'")
table_exists = mycursor.fetchone()

# If the table does not exist, create it
if not table_exists:
    # Define the SQL command to create the table
    create_table_query = """
    CREATE TABLE bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        guest_name VARCHAR(255) NOT NULL,
        hotel_name VARCHAR(255) NOT NULL,
        room_number INT NOT NULL,
        check_in_date DATE NOT NULL,
        check_out_date DATE NOT NULL
    )
    """

    # Execute the SQL command
    mycursor.execute(create_table_query)

    # Commit the transaction
    mydb.commit()