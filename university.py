# This file runs our database project.
import sqlite3

# This function runs the SQL code from our schema.sql file.
def setup_database(db_name):
    # Connects to the database file.
    conn = sqlite3.connect(db_name)
    # Reads the SQL file.
    with open('schema.sql', 'r') as f:
        sql_code = f.read()
    # Runs the SQL code to create the tables.
    conn.executescript(sql_code)
    # Closes the connection.
    conn.close()
    print("Database tables created.")

# This function adds one new student to the database.
def add_student(conn, first_name, last_name, email):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (first_name, last_name, email) VALUES (?, ?, ?)",
        (first_name, last_name, email)
    )
    conn.commit()
    print(f"Added student: {first_name} {last_name}")

# This function adds one new course to the database.
def add_course(conn, course_name, credits):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Courses (course_name, credits) VALUES (?, ?)",
        (course_name, credits)
    )
    conn.commit()
    print(f"Added course: {course_name}")
    
# This function puts a student into a course.
def enroll_student(conn, student_id, course_id):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )
    conn.commit()
    print(f"Enrolled student #{student_id} in course #{course_id}")

# This function gets all the courses for one student.
def get_student_courses(conn, student_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.course_name
        FROM Courses c
        JOIN Enrollments e ON c.course_id = e.course_id
        WHERE e.student_id = ?
    """, (student_id,))
    
    courses = cursor.fetchall()
    # Puts the course names into a simple list.
    return [course[0] for course in courses]

# --- This is where the program starts running ---
if __name__ == "__main__":
    db_name = "university.db"

    # 1. Create the database and tables first.
    setup_database(db_name)

    # 2. Connect to the database to add and get data.
    conn = sqlite3.connect(db_name)

    # Add some students and courses.
    add_student(conn, "Amanuel", "Weldemeskel", "amanuel.w@example.com") # student_id will be 1
    add_student(conn, "Abigail", "Seyoum", "abigail.s@example.com")   # student_id will be 2
    add_course(conn, "Databases 101", 3)                     # course_id will be 1
    add_course(conn, "Python Basics", 4)                     # course_id will be 2
    
    # Enroll students in courses.
    enroll_student(conn, 1, 1) # Enroll Amanuel in Databases 101
    enroll_student(conn, 1, 2) # Enroll Amanuel in Python Basics
    enroll_student(conn, 2, 1) # Enroll Abigail in Databases 101
        
    print("\n--- Let's check our work ---")

    # 3. Test our function.
    amanuels_courses = get_student_courses(conn, 1)
    print("Found these courses for Amanuel:")
    for course in amanuels_courses:
        print(f"- {course}")
        
    
