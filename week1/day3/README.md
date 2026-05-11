# SQL Joins Assignment

This file demonstrates different types of SQL JOIN operations using PostgreSQL.

## Tables Created
- instructors
- students
- courses
- enrollments

## Operations Performed

### 1. Displayed all students and the courses they are enrolled in
- Used LEFT JOIN
- Included students without enrollments

### 2. Found courses with no students enrolled
- Used LEFT JOIN with NULL checking

### 3. Displayed instructors and the courses they teach
- Included instructors without assigned courses

### 4. Found courses without instructors
- Used NULL condition

### 5. Displayed students and enrollment details using RIGHT JOIN
- Included all enrollment records

### 6. Found students not enrolled in any course
- Used LEFT JOIN and IS NULL

### 7. Used FULL OUTER JOIN on students and enrollments
- Displayed matched and unmatched rows from both tables

### 8. Found courses never present in enrollments
- Identified courses without enrollment records

### 9. Used FULL OUTER JOIN on instructors and courses
- Displayed unmatched instructors and courses

### 10. Created a complete report
- Displayed student name, course name, and instructor name
- Included missing course and instructor information using LEFT JOINs

## Concepts Practiced
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- NULL handling
- Multi-table joins
