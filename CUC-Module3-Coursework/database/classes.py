# Define the Student class with methods to add, update, delete, and print student details
class Student:
   def __init__(self, student_id, student_name):
       # Initialize the student object with a unique student ID and student name
       self.student_id = student_id
       self.student_name = student_name

   def add_new_student(self, cursor, connection):
       # Add a new student to the StudentsCoursesRegistrations table in the SQLite database
       cursor.execute('''INSERT INTO StudentsCoursesRegistrations (StudentID, StudentName) VALUES (?,?)''', (self.student_id, self.student_name))
       connection.commit()
       self.print_student_details()

   def update_student(self, cursor, connection):
       # Update the student name for a given student ID in the StudentsCoursesRegistrations table in the SQLite database
       cursor.execute('''UPDATE StudentsCoursesRegistrations SET StudentName = ? WHERE StudentID = ?''', (self.student_name, self.student_id))
       connection.commit()
       self.print_student_details()

   def print_student_details(self):
       # Print the student ID and student name for the current student object
       print(f'Student ID: {self.student_id}, Student Name: {self.student_name}')

   @classmethod
   def delete_student(cls, student_id, cursor, connection):
       # Delete a student from the StudentsCoursesRegistrations table in the SQLite database using the student ID
       cursor.execute("DELETE FROM StudentsCoursesRegistrations WHERE StudentID = ?", (student_id,))
       connection.commit()
       print('Student Deleted Successfully')

   @classmethod
   def print_all_students_details(cls, cursor, connection):
       # Print the details of all students in the StudentsCoursesRegistrations table in the SQLite database
       cursor.execute("SELECT * FROM StudentsCoursesRegistrations")
       rows = cursor.fetchall()
       for row in rows:
           s = Student(row[0], row[1])
           s.print_student_details()

# Define the Teacher class with methods to add, update, delete, and print teacher details
class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

    def add_new_teacher(self, cursor, connection):
        cursor.execute('''INSERT INTO StudentsCoursesRegistrations (TeacherID, TeacherName) VALUES (?,?)''', (self.teacher_id, self.teacher_name))
        connection.commit()
        self.print_teacher_details()

    def update_teacher(self, cursor, connection):
        cursor.execute('''UPDATE StudentsCoursesRegistrations SET TeacherName = ? WHERE TeacherID = ?''', (self.teacher_name, self.teacher_id))
        connection.commit()
        self.print_teacher_details()

    def print_teacher_details(self):
        print(f'Teacher ID: {self.teacher_id}, Teacher Name: {self.teacher_name}')

    @classmethod
    def delete_teacher(cls, teacher_id, cursor, connection):
        cursor.execute("DELETE FROM StudentsCoursesRegistrations WHERE TeacherID = ?", (teacher_id,))
        connection.commit()
        print('Teacher Deleted Successfully')

    @classmethod
    def print_all_teachers_details(cls, cursor, connection):
        cursor.execute("SELECT * FROM StudentsCoursesRegistrations")
        rows = cursor.fetchall()
        for row in rows:
            t = Teacher(row[0], row[1])
            t.print_teacher_details()

#Define the Course class with methods to add, update, delete, and print course details
class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def add_new_course(self, cursor, connection):
        cursor.execute('''INSERT INTO StudentsCoursesRegistrations (CourseID, CourseName) VALUES (?,?)''', (self.course_id, self.course_name))
        connection.commit()
        self.print_course_details()

    def update_course(self, cursor, connection):
        cursor.execute('''UPDATE StudentsCoursesRegistrations SET CourseName = ? WHERE CourseID = ?''', (self.course_name, self.course_id))
        connection.commit()
        self.print_course_details()

    def print_course_details(self):
        print(f'Course ID: {self.course_id}, Course Name: {self.course_name}')

    @classmethod
    def delete_course(cls, course_id, cursor, connection):
        cursor.execute("DELETE FROM StudentsCoursesRegistrations WHERE CourseID = ?", (course_id,))
        connection.commit()
        print('Course Deleted Successfully')
    
    @classmethod
    def print_all_courses_details(cls, cursor, connection):
        cursor.execute()
        rows = cursor.fetchall("SELECT * FROM StudentsCoursesRegistrations")
        for row in rows:
            c = Course(row[0], row[1])
            c.print_course_details()