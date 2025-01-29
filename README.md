MySQL Database Operations with Python
This project demonstrates how to connect Python to a MySQL database, create databases and tables, and execute CRUD operations.
Directory Structure
text
mysql-database-automation/
├── connect_mysql.py        # Connects to MySQL server
├── create_db_tables.py     # Creates databases and tables
├── execute_queries.py      # Executes queries
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
└── LICENSE                 # License information
Features
Connect to MySQL Server: Establish a connection to your MySQL database.
Create Databases and Tables: Easily set up your database structure.
Execute SQL Queries: Perform Insert, Fetch, Update, and Delete operations.
Modular and Maintainable Structure: Organized code for better maintainability.
Setup Instructions
Prerequisites
Before you begin, ensure you have the following installed:
Python 3.x
MySQL Server
MySQL Connector for Python (mysql-connector-python)
Installation
Clone the Repository
Open your terminal and run:
bash
git clone https://github.com/your-username/mysql-database-automation.git
cd mysql-database-automation
Install Dependencies
Install the required Python packages using pip:
bash
pip install -r requirements.txt
Usage Instructions
Update MySQL Credentials in connect_mysql.py
Edit the connect_mysql.py file to include your MySQL credentials:
python
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database_name"
)
Run Database and Table Creation
Execute the following command to create the necessary databases and tables:
bash
python create_db_tables.py
Execute Queries
To run predefined queries, use:
bash
python execute_queries.py
Project Dependencies
mysql-connector-python: This library allows Python to connect to MySQL databases.
