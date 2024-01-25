import sqlite3
from student import Student # Import the Student class from the student module

def create_tables():
    # Connect to the database and create a cursor object
    connection = sqlite3.connect('school.db')
    cursor = connection.cursor()

    # Create the StudentsCoursesRegistrations table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS StudentsCoursesRegistrations (
                        StudentID INTEGER PRIMARY KEY,
                        StudentName TEXT,
                        CourseID INTEGER,
                        Course_Details TEXT,
                        TeacherID INTEGER,
                        Teacher_name TEXT,
                        Registration_Date TEXT)''')
    # Commit the changes and close the connection
    connection.commit()
    connection.close()

def main_menu():
    # Print the main menu options
    print('what would you like to manage:\n press 1 for Students,\n 2 for teachers,\n 3 for courses,\n 4 for enrollment')
    choice = input('Input your choice: ')
    if choice == '1':
        # Print the student management menu options
        print('\n\nYou have chosen Student Management,\n press 1 to add a new student,\n 2 to update an existing student,\n 3 to delete a student,\n 4 to view all students details')
        student_management_choice = input('Input your choice: ')
        if student_management_choice == '1':
            # Add a new student
            student_id = input('input student id: ')
            student_name = input('input student name: ')
            s = Student(student_id, student_name)
            s.add_new_student(cursor, connection)
            s.print_student_details()
        elif student_management_choice == '2':
            # Update an existing student
            student_id = input('Which student detail you want to update: input student id: ')
            student_name = input('input an updated student name: ')
            s = Student(student_id, student_name)
            s.update_student(cursor, connection)
            s.print_student_details()
        elif student_management_choice == '3':
            # Delete a student
            student_id = input('Input the student ID you want to delete: ')
            Student.delete_student(student_id, cursor, connection)
        elif student_management_choice == '4':
            # Print all students details
            Student.print_all_students_details(cursor, connection)
        else:
            print('input is not valid')

if __name__ == "__main__":
    # Connect to the database and create a cursor object
    connection = sqlite3.connect('school.db')
    cursor = connection.cursor()
    # Create the tables
    create_tables()
    # Display the main menu
    main_menu()
    # Close the connection
    connection.close()