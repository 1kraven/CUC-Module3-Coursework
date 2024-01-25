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