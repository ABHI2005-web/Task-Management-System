Task Management System

A responsive administrative web portal built using Python, Flask, and MySQL. This system allows a preserved admin user to log in and update employee task completion states dynamically.

🛠️ Tech Stack Included


Backend: Python, Flask
Database: MySQL
Frontend: HTML5, CSS3 (Responsive UI), JavaScript


📁 Repository Structure


app.py — Core application file handling login routing, session management, and CRUD update actions via MySQL.
init_db.py — Database initialization script that configures tables using AUTO_INCREMENT and seeds initial profiles.
static/style.css — Modern, fluid CSS formatting designed around clean layout constraints.
templates/login.html — Administrative authentication interface.
templates/dashboard.html — Interactive task form built using reactive dropdown lists.


🗄️ MySQL Database Schema

The app uses a database named task_management with two tables: admins and tasks. init_db.py creates both and seeds one admin row.

sqlCREATE DATABASE IF NOT EXISTS task_management;
USE task_management;

CREATE TABLE admins (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  admin_id      VARCHAR(50)  NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
  id              INT AUTO_INCREMENT PRIMARY KEY,
  task_ref        VARCHAR(20)  NOT NULL UNIQUE,        -- e.g. TSK-0001
  employee_id     VARCHAR(50)  NOT NULL,
  employee_name   VARCHAR(100) NOT NULL,
  task_title      ENUM('task1','task2','task3') NOT NULL,
  completed       ENUM('true','false') NOT NULL,
  logged_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

init_db.py seeds the preserved admin row with a hashed password (never plaintext):

pythonfrom werkzeug.security import generate_password_hash

cursor.execute(
    "INSERT INTO admins (admin_id, password_hash) VALUES (%s, %s)",
    ("admin", generate_password_hash("admin123"))
)

app.py connects to MySQL like this:

pythonimport mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your-mysql-password",
    database="task_management"
)

Task rows are inserted with a parameterized query (never string-concatenated, to avoid SQL injection):

pythoncursor.execute(
    "INSERT INTO tasks (task_ref, employee_id, employee_name, task_title, completed) "
    "VALUES (%s, %s, %s, %s, %s)",
    (task_ref, employee_id, employee_name, task_title, completed)
)

⚙️ How to Run the Project Locally

1. Configure the MySQL Server

Make sure you have a running MySQL database instance. Open app.py and init_db.py and replace the connection parameters with your local credentials:


host — e.g. localhost
user — e.g. root
password — your MySQL password
database — task_management


2. Install Dependencies

Ensure you have Flask, the MySQL connector client library, and Werkzeug (for password hashing) installed:

bashpip install Flask mysql-connector-python Werkzeug

3. Initialize the Database

Before running the application server, execute the initialization script once to construct the data tables and populate initial records:

bashpython init_db.py

4. Launch the Server

Start the Flask local development server:

bashpython app.py

5. Access the Form

Open your web browser and navigate to: http://127.0.0.1:5000

🔐 Preserved Admin Credentials

Use these preset parameters to clear the authentication step on the login screen:


Admin ID: admin
Password: admin123



The password above is stored in MySQL as a hash (via werkzeug.security.generate_password_hash), not as plaintext — app.py checks logins with check_password_hash against the password_hash column in the admins table.
