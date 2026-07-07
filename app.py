from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

# Create Flas app
app = Flask(__name__)

# Secret key is used for login session
app.secret_key = 'your_super_secret_session_key'


# Connect to MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",          # Enter your MySQL password
        database="your_database_name"      # Enter your database name
    )
    return conn


# Login page
@app.route('/', methods=['GET', 'POST'])
def login():

    # Check if login form is submitted
    if request.method == 'POST':

        # Get Admin ID and Password from form
        admin_id = request.form['admin_id']
        password = request.form['password']

        # Connect to database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if Admin ID and Password are correct
        cursor.execute(
            'SELECT * FROM admins WHERE admin_id = %s AND password = %s',
            (admin_id, password)
        )

        admin = cursor.fetchone()

        # Close database connection
        cursor.close()
        conn.close()

        # If login is successful
        if admin:
            session['admin_id'] = admin['admin_id']
            return redirect(url_for('dashboard'))

        # If login fails
        else:
            flash('Invalid Admin ID or Password', 'error')

    # Show login page
    return render_template('login.html')


# Dashboard page
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    # Check if admin is logged in
    if 'admin_id' not in session:
        return redirect(url_for('login'))

    # Connect to database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # If update button is clicked
    if request.method == 'POST':

        # Get selected task and status
        selected_title = request.form.get('task_title')
        completion_status = request.form.get('completed')

        # Update task status
        cursor.execute(
            'UPDATE tasks SET completed = %s WHERE task_title = %s',
            (completion_status, selected_title)
        )

        conn.commit()

        # Show success message
        flash(f'Successfully updated status for {selected_title}!', 'success')

    # Get all tasks from database
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    # Close database connection
    cursor.close()
    conn.close()

    # Get selected task
    selected_task_title = request.args.get('task_title', 'task 1')

    # Find selected task
    current_task = next(
        (t for t in tasks if t['task_title'] == selected_task_title),
        None
    )

    # Open dashboard page
    return render_template(
        'dashboard.html',
        tasks=tasks,
        current_task=current_task
    )


# Logout page
@app.route('/logout')
def logout():

    # Remove admin session
    session.pop('admin_id', None)

    # Go back to login page
    return redirect(url_for('login'))


# Run the project
if __name__ == '__main__':
    app.run(debug=True)
