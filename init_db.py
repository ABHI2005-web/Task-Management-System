import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Admin table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            admin_id TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    # Tasks table with Auto-incrementing Primary Key to avoid duplicates
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            employee_name TEXT NOT NULL,
            task_title TEXT NOT NULL,
            completed TEXT NOT NULL DEFAULT 'false'
        )
    ''')

    # Insert default admin if not exists
    cursor.execute("INSERT OR IGNORE INTO admins (admin_id, password) VALUES (?, ?)", ('admin', 'admin123'))
    
    # Seed sample tasks matching your wireframe options
    cursor.execute("SELECT COUNT(*) FROM tasks")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO tasks (employee_id, employee_name, task_title, completed) 
            VALUES (?, ?, ?, ?)
        ''', [
            ('EMP001', 'John Doe', 'task 1', 'false'),
            ('EMP002', 'Jane Smith', 'task 2', 'true'),
            ('EMP003', 'Bob Johnson', 'task 3', 'false')
        ])

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
