from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Simple in-memory data stores (replace with a real database for production)
announcements = [
    {
        'title': 'Important: Campus Closure',
        'author': 'Administration',
        'date': '2025-09-15',
        'body': 'Due to unforeseen circumstances, the campus will be closed today. All classes are canceled.'
    },
    {
        'title': 'Student Union Meeting',
        'author': 'Student Union',
        'date': '2025-09-14',
        'body': 'There will be an important student union meeting on Friday at 3:00 PM in the Auditorium. All students are encouraged to attend.'
    }
]

lecturers = [
    {
        'name': 'Prof. J Dadzie',
        'department': 'Department of Computer Science',
        'email': 'jdadzie@atu.edu',
        'hours': 'Mon,Fri 8:00 AM - 4:00 PM'
    },
    {
        'name': 'Prof. K.O Ampadu',
        'department': 'Department of Computer Science',
        'email': 'ampadu@atu.edu',
        'hours': 'Tue, Wed 8:00 AM - 4:00 PM'
    },
    {
        'name': 'Prof. A .Odonkor',
        'department': 'Department of Computer Science',
        'email': 'odonkor@atu.edu',
        'hours': 'Tue, Thu 8:00 AM - 4:00 PM'
    },
    {
        'name': 'Prof Nana .A . Preprah',
        'department': 'Department of Computer Science',
        'email': 'preprah@atu.edu',
        'hours': 'Wed, Thu 8:00 AM - 4:00 PM'
    }
]

students = [
    {
        'name': 'John Doe',
        'program': 'Computer Science',
        'year': 2,
        'email': 'john.doe@example.com'
    },
    {
        'name': 'Jane Smith',
        'program': 'Electrical Engineering',
        'year': 3,
        'email': 'jane.smith@example.com'
    },
    {
        'name': 'Michael Brown',
        'program': 'Business Administration',
        'year': 1,
        'email': 'michael.brown@example.com'
    }
]

timetable_data = {
    'Monday': [('BCP 106 Probability and Statistics for Computer Science', 'Prof. J. Dadzie', 'Great Hall A')],
    'Tuesday': [('PRJ 102 Problem Solving, Identification and Solution', 'Prof. A .Odonkor', 'Great Hall A')],
    'Wednesday': [],
    'Thursday': [('BCP 104 Programming with Python', 'Prof Nana .A . Preprah', 'Great Hall A, BTech Com Lab Large')],
    'Friday': []
}

# Ensure the 'templates' folder exists for the app to find HTML files
if not os.path.exists('templates'):
    os.makedirs('templates')
    print("Created 'templates' directory. Please place your HTML files inside.")

@app.route('/')
def home():
    """Renders the main index page."""
    return render_template('index.html')

@app.route('/accounts.html', methods=['GET', 'POST'])
def accounts():
    """Handles account registration form submissions."""
    if request.method == 'POST':
        full_name = request.form['username']
        student_id = request.form['studentid']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Basic validation
        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect(url_for('accounts'))
        
        # Here you would typically save the user data to a database
        print(f"New user registered: {full_name}, {student_id}, {email}")
        flash("Account created successfully!")
        return redirect(url_for('home'))
    
    return render_template('accounts.html')

@app.route('/annoucement.html', methods=['GET', 'POST'])
def announcement_page():
    """Displays announcements and handles adding new ones."""
    if request.method == 'POST':
        title = request.form['announcement_title']
        author = request.form['announcement_author']
        body = request.form['announcement_body']
        new_announcement = {
            'title': title,
            'author': author,
            'date': '2025-09-17',  # Or a dynamically generated date
            'body': body
        }
        announcements.append(new_announcement)
        flash("Announcement added successfully!")
        return redirect(url_for('announcement_page'))
    
    return render_template('annoucement.html', announcements=announcements)

@app.route('/department.html')
def department_page():
    """Renders the department selection page."""
    return render_template('department.html')

@app.route('/lecturer.html')
def lecturer_page():
    """Displays the lecturer directory with optional search functionality."""
    search_query = request.args.get('search_lecturers', '').lower()
    if search_query:
        filtered_lecturers = [
            l for l in lecturers if search_query in l['name'].lower() or search_query in l['department'].lower()
        ]
    else:
        filtered_lecturers = lecturers
    return render_template('lecturer.html', lecturers=filtered_lecturers)

@app.route('/slides.html')
def slides_page():
    """Renders the slides and materials page."""
    return render_template('slides.html')

@app.route('/student.html')
def student_page():
    """Displays the student directory with optional search functionality."""
    search_query = request.args.get('search_input', '').lower()
    if search_query:
        filtered_students = [
            s for s in students if search_query in s['name'].lower() or search_query in s['program'].lower()
        ]
    else:
        filtered_students = students
    return render_template('student.html', students=filtered_students)

@app.route('/timetable.html')
def timetable_page():
    """Renders the timetable page with the timetable data."""
    return render_template('timetable.html', timetable=timetable_data)

if __name__ == '__main__':
    app.run(debug=True)