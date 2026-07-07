# Task Management System

A responsive administrative web portal built using Python, Flask, and MySQL. This system allows a preserved admin user to log in and update employee task completion states dynamically.

## 🛠️ Tech Stack Included
- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML5, CSS3 (Responsive UI), JavaScript

## 📁 Repository Structure
- `app.py` — Core application file handling login routing, session management, and CRUD update actions via MySQL.
- `init_db.py` — Database initialization script that configures tables using `AUTO_INCREMENT` and seeds initial profiles.
- `static/style.css` — Modern, fluid CSS formatting designed around clean layout constraints.
- `templates/login.html` — Administrative authentication interface.
- `templates/dashboard.html` — Interactive task form built using reactive dropdown lists.

## ⚙️ How to Run the Project Locally

### 1. Configure the MySQL Server
Make sure you have a running MySQL database instance. Open `app.py` and `init_db.py` to replace the connection parameters with your local credentials:
- `host`
- `user`
- `password`
- `database`

### 2. Install Dependencies
Ensure you have Flask and the MySQL connector client library installed:
```bash
pip install Flask mysql-connector-python

### 3. Initialize the Database
Before running the application server, execute the initialization script once to construct the data tables and populate initial records:

Bash
python init_db.py
### 4.Launch the Server
Start the Flask local development container:

Bash
python app.py

### 5. Access the Form
Open your web browser and navigate to: http://127.0.0.1:5000

🔐 Preserved Admin Credentials
Use these preset parameters to clear the authentication step on the login screen:

Admin ID: admin

Password: admin123
