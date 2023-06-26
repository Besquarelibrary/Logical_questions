# Import the mysql.connector module for MySQL database connection
import mysql.connector
from SMTP import email_service  # Importing email_service from SMTP module

# Establishing a connection to the MySQL database (host, user, password, database)
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uday@402403",
    database="udaydb"
)

# Create a cursor object to execute SQL queries
cursor = con.cursor()

# Execute the SQL query to create database
#cursor.execute("CREATE Database udaydb")

# Execute the SQL query to create table
# cursor.execute("CREATE TABLE Employee_details(Name varchar(30), ID int(10), Email varchar(20))")

# Execute the SQL query to update column data type & size
# cursor.execute("ALTER TABLE Employee_details MODIFY Email VARCHAR(40) ;")

# Execute the SQL query to show tables in the database
cursor.execute("SHOW TABLES")

# Print a separator line
print("-------------------------------------------------------------------------------------------")

# Iterate through the result set and print each table name
for db in cursor:
    print(db)

# Print another separator line
print("-------------------------------------------------------------------------------------------")

# Function to check if an employee with the given ID already exists
def check_employee(employee_id):
    c = con.cursor()
    sql = "SELECT * FROM employee_details WHERE id = %s"
    c.execute(sql, (employee_id,))
    result = c.fetchone()
    return result is not None


# Function to add an employee
def add_employee():
    employee_id = input("Enter Employee Id: ")

    # Checking if Employee with given ID already exists
    if check_employee(employee_id):
        print("Employee already exists. Please try again.")
        menu()
    else:
        name = input("Enter Employee Name: ")
        email = input("Enter Employee Email: ")
        data = (employee_id, name, email)

        # Inserting Employee details into the Employee Table
        sql = 'INSERT INTO employee_details (id, name, email) VALUES (%s, %s, %s)'
        c = con.cursor()

        try:
            # Executing the SQL Query
            c.execute(sql, data)
            # Committing the changes in the table
            con.commit()
            print("Employee Added Successfully")
            menu()
        except mysql.connector.Error as e:
            print(f"An error occurred: {str(e)}")
            menu()


def display_table():
    # Executing the SQL query to fetch data from the table
    sql = "SELECT * FROM employee_details order by ID"
    cursor.execute(sql)

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Printing the table data
    for row in rows:
        print("Employee name:", row[0])
        print("Employee ID:", row[1])
        print("Email ID:", row[2])
        print("----------------------------------------------------------------------")

    menu()


def remove_employee(employee_id):
    # Checking if the employee exists
    if not check_employee(employee_id):
        print("Employee does not exist. Please try again.")
        menu()

    try:
        # Deleting the employee from the table
        sql = "DELETE FROM employee_details WHERE ID = %s"
        cursor.execute(sql, (employee_id,))

        # Committing the changes in the database
        con.commit()

        print("Employee removed successfully")
    except mysql.connector.Error as e:
        print(f"An error occurred while removing the employee: {str(e)}")

    # Return to the menu
    menu()


def menu():
    print("---------------------------------------------------------------------------")
    # Display the menu options
    print("1.Add Employee")
    print("2.Display data table")
    print("3.Remove employee")
    print("4.Check employee")
    print("5.Email service")
    print("6.Exit")
    print("---------------------------------------------------------------------------")

    # Prompt for user's choice
    choice = input("Enter your choice: ")

    # Perform actions based on the user's choice
    if choice == "1":
        add_employee()

    elif choice == "2":
        display_table()

    elif choice == "3":
        employee_id = int(input("Enter ID number to remove: "))
        remove_employee(employee_id)

    elif choice == "4":
        employee_id = int(input("Enter the employee ID: "))
        if check_employee(employee_id):
            sql = "SELECT * FROM employee_details WHERE id = %s"
            cursor.execute(sql, (employee_id,))
            employee_data = cursor.fetchone()
            print("Employee name:", employee_data[0])
            print("Employee ID:", employee_data[1])
            print("Email ID:", employee_data[2])
            print("-------------------------------------------------------------------------------------------")
        else:
            print("ID does not exist")
            print("-------------------------------------------------------------------------------------------")
        menu()

    elif choice == "5":
        # Executing the SQL query to fetch data from the table
        sql = "SELECT * FROM employee_details order by ID"
        cursor.execute(sql)

        # Fetching all rows from the result set
        rows = cursor.fetchall()

        # Printing the table data
        for table_data in rows:
            email_service(table_data[2], table_data[0])
            print("Email Successfully sent to:", table_data[0])
        exit()

    elif choice == "6":
        # Close the database connection and exit the program
        con.close()
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice. Please try again.")
        menu()


# Starting point of the program
menu()

