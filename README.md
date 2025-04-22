# SQL Server Connection App using Python

This application demonstrates how to connect to a SQL Server database using a Python script within GitHub Codespaces.

## Prerequisites

Before running the app, ensure that the following requirements are met:

- **Python 3.x** is installed.
- The required Python libraries are installed:
  - `pyodbc` (for connecting to SQL Server)
  
## Setting Up the Environment

1. **Clone the repository to GitHub Codespaces**:
   - Open GitHub Codespaces and create a new Codespace from this repository.

2. **Install required Python packages**:
   - After opening the Codespace, open the terminal and install the necessary dependencies using `pip`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set up SQL Server connection details**:
   - Open the `db_config.py` file and update the connection parameters such as the server, database, username, and password.
   - Example configuration:
     ```python
     server = 'your_sql_server_address'
     database = 'your_database_name'
     username = 'your_username'
     password = 'your_password'
     ```

## Running the Script

1. **Start the script**:
   - In GitHub Codespaces terminal, run the script using:
     ```bash
     python connect_sql.py
     ```

2. The Python script will establish a connection to the SQL Server database and you will see any relevant output or error messages based on the connection attempt.

## Script Overview

- **connect_sql.py**: This script connects to the SQL Server using the details provided in `db_config.py`. It queries a test database and prints the results.
  
  Example of the script:
  ```python
  import pyodbc
  
  # Import connection settings
  from db_config import server, database, username, password

  # Set up the connection
  conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
  
  # Create a cursor and execute a query
  cursor = conn.cursor()
  cursor.execute('SELECT TOP 5 * FROM your_table')
  
  # Fetch and print the results
  rows = cursor.fetchall()
  for row in rows:
      print(row)

  # Close the connection
  conn.close()
