# Student Enrollment System

This is a simple command-line application for managing a university's student enrollment system. It's built with Python and uses SQLite for the database. This project was created to practice fundamental database concepts like schema design, normalization, and SQL querying.

---

## Features

* Creates a complete database schema from a `.sql` file.
* Adds new students and courses to the database.
* Enrolls students in available courses.
* Queries the database to find which courses a specific student is taking.

---

## Technologies Used

* Language: Python 3
* Database: SQLite 3

---

##  How to Run

1.  Prerequisites: Make sure you have Python 3 installed on your computer.

2.  Clone the repository:
    ```bash
    git clone [https://github.com/YourUsername/student-database-project.git](https://github.com/Aweldeme/student-database-project.git)
    ```
    

3.  Navigate to the project directory:
    ```bash
    cd student-database-project
    ```

4.  Run the script:
    ```bash
    python university.py
    ```

5.  Expected Output: The script will first create the `university.db` file. Then, it will print a confirmation of the students and courses being added, followed by a list of courses for the student Amanuel.

---

##  Database Schema

The database consists of four tables:

* Students: Stores student information.
    * `student_id` (Primary Key)
    * `first_name`
    * `last_name`
    * `email`
* Courses: Stores course information.
    * `course_id` (Primary Key)
    * `course_name`
    * `credits`
* Professors: Stores professor information (can be expanded later).
    * `professor_id` (Primary Key)
* Enrollments: A linking table that connects students to the courses they are enrolled in.
    * `enrollment_id` (Primary Key)
    * `student_id` (Foreign Key)
    * `course_id` (Foreign Key)
