# Task Management System

A responsive administrative web portal built using Python, Flask, and SQLite. This system allows a preserved admin user to log in and update employee task completion states dynamically.

## 🛠️ Tech Stack Included
- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML5, CSS3 (Responsive UI), JavaScript

## 📁 Repository Structure
- `app.py` — Core application file handling login routing, session management, and CRUD update actions.
- `init_db.py` — Database initialization script that prevents duplicate entries and seeds initial task profiles.
- `static/style.css` — Modern, fluid CSS formatting designed around clean layout constraints.
- `templates/login.html` — Administrative authentication interface.
- `templates/dashboard.html` — Interactive task form built using reactive dropdown lists.

## ⚙️ How to Run the Project Locally

### 1. Install Dependencies
Ensure you have Flask installed in your development environment:
```bash
pip install Flask
2. Initialize the Database
Before running the server, execute the initialization script once to generate your local database.db file and populate it with seed data:

Bash
python init_db.py
3. Launch the Server
Start the Flask local development container:

Bash
python app.py
4. Access the Form
Open your browser and navigate to: http://127.0.0.1:5000

🔐 Preserved Admin Credentials
Use these credentials to clear the authentication block on the login page:

Admin ID: admin

Password: admin123
