from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_super_secret_session_key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin_id = request.form['admin_id']
        password = request.form['password']
        
        conn = get_db_connection()
        admin = conn.execute('SELECT * FROM admins WHERE admin_id = ? AND password = ?', 
                             (admin_id, password)).fetchone()
        conn.close()
        
        if admin:
            session['admin_id'] = admin['admin_id']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Admin ID or Password', 'error')
            
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    
    if request.method == 'POST':
        selected_title = request.form.get('task_title')
        completion_status = request.form.get('completed')
        
        conn.execute('UPDATE tasks SET completed = ? WHERE task_title = ?', 
                     (completion_status, selected_title))
        conn.commit()
        flash(f'Successfully updated status for {selected_title}!', 'success')

    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    
    selected_task_title = request.args.get('task_title', 'task 1')
    current_task = next((t for t in tasks if t['task_title'] == selected_task_title), None)
    
    return render_template('dashboard.html', tasks=tasks, current_task=current_task)

@app.route('/logout')
def logout():
    session.pop('admin_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
