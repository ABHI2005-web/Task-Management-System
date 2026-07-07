import mysql.connector

def init_db():
    # Replace with your actual MySQL databas credentials
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database_name"
    )
    cursor = conn.cursor()

    # Admin tabl
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            admin_id VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL
        )
    ''')

    # Tasks table (Note: MySQL uses AUTO-INCREMENT)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INT AUTO_INCREMENT PRIMARY KEY,
            employee_id VARCHAR(255) NOT NULL,
            employee_name VARCHAR(255) NOT NULL,
            task_title VARCHAR(255) NOT NULL,
            completed VARCHAR(50) NOT NULL DEFAULT 'false'
        )
    ''')

    # Insert default admin if not exists
    cursor.execute("SELECT * FROM admins WHERE admin_id = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO admins (admin_id, password) VALUES (%s, %s)", ('admin', 'admin123'))
    
    # Seed sample tasks if table is empty
    cursor.execute("SELECT COUNT(*) FROM tasks")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO tasks (employee_id, employee_name, task_title, completed) 
            VALUES (%s, %s, %s, %s)
        ''', [
            ('EMP001', 'John Doe', 'task 1', 'false'),
            ('EMP002', 'Jane Smith', 'task 2', 'true'),
            ('EMP003', 'Bob Johnson', 'task 3', 'false')
        ])

    conn.commit()
    conn.close()
    print("MySQL Database initialized successfully.")

if __name__ == '__main__':
    init_db()
