import mysql.connector
from mysql.connector import Error

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = "employee_management_system"

def init_db():
    try:
        # First connect without specifying the database to create it if it doesn't exist
        print("Connecting to MySQL server...")
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Database '{DB_NAME}' created or already exists.")
            
            # Use the newly created/existing database
            cursor.execute(f"USE {DB_NAME}")
            
            # 1. Departments Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS departments (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    department_name VARCHAR(255) NOT NULL
                )
            ''')
            
            # 2. Employees Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    department_id INT,
                    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL
                )
            ''')
            
            # 3. Salaries Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS salaries (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    employee_id INT NOT NULL,
                    salary_amount DECIMAL(10, 2) NOT NULL,
                    effective_date DATE,
                    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
                )
            ''')
            
            # 4. Attendance Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS attendance (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    employee_id INT NOT NULL,
                    date DATE NOT NULL,
                    status ENUM('Present', 'Absent', 'Leave') NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
                )
            ''')
            
            conn.commit()
            print("Tables (departments, employees, salaries, attendance) successfully created in MySQL.")
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    init_db()
