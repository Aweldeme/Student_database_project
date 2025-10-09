-- This file makes the tables for our database.

-- Deletes old tables so we can start fresh.
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Professors;

-- Makes the Students table.
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    enrollment_date DATE
);

-- Makes the Professors table.
CREATE TABLE Professors (
    professor_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department TEXT
);

-- Makes the Courses table.
CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    credits INTEGER,
    professor_id INTEGER
);

-- Makes the Enrollments table to connect students and courses.
CREATE TABLE Enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    grade TEXT
);