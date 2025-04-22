import pyodbc

server = 'localhost'
database = 'master'
username = 'SA'
password = 'YourStrong!Passw0rd'
driver = '{ODBC Driver 17 for SQL Server}'  # Change if necessary

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("""
        IF OBJECT_ID('students', 'U') IS NOT NULL DROP TABLE students;
        CREATE TABLE students (
            id INT PRIMARY KEY,
            name NVARCHAR(100),
            age INT
        );
    """)
    cursor.execute("INSERT INTO students VALUES (1, 'Alice', 22)")
    cursor.execute("INSERT INTO students VALUES (2, 'Bob', 25)")
    conn.commit()

    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(f"ID: {row.id}, Name: {row.name}, Age: {row.age}")

except Exception as e:
    print("Error:", e)
finally:
    conn.close()
