import sqlite3 # Import the sqlite library for the database to work successfully
from classes import * # Import everything from the 'classes.py' file

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
                        TeacherName TEXT,
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


    if choice == '2':
        print('\n\nYou have chosen Teacher Management,\n press 1 to add a new teacher,\n 2 to update an existing teacher,\n 3 to delete a teacher,\n 4 to view all teachers details')
        teacher_management_choice = input('Input your choice: ')
        if teacher_management_choice == '1':
            teacher_id = input('input teacher id: ')
            teacher_name = input('input teacher name: ')
            t = Teacher(teacher_id, teacher_name)
            t.add_new_teacher(cursor, connection)
            t.print_teacher_details()
        elif teacher_management_choice == '2':
            teacher_id = input('Which teacher detail do you want to update: input teacher id: ')
            teacher_name = input('input an updated teacher name: ')
            t = Teacher(teacher_id, teacher_name)
            t.update_teacher(cursor, connection)
            t.print_teacher_details()
        elif teacher_management_choice == '3':
            teacher_id = input('Input the teacher ID you want to delete: ')
            Teacher.delete_teacher(teacher_id, cursor, connection)
        elif teacher_management_choice == '4':
            Teacher.print_all_teachers_details(cursor, connection)
        else:
            print('input is not valid')


    if choice == '3':
        print('\n\nYou have chosen Course Management,\n press 1 to add a new course,\n 2 to update an existing course,\n 3 to delete a course,\n 4 to view all courses details')
        course_management_choice = input('Input your choice: ')
        if course_management_choice == '1':
            course_id = input('input course id: ')
            course_name = input('input course name: ')
            c = Course(course_id, course_name)
            c.add_new_course(cursor, connection)
            c.print_course_details()
        elif course_management_choice == '2':
            course_id = input('Which course detail do you want to update: input course id: ')
            course_name = input('input an updated course name: ')
            c = Course(course_id, course_name)
            c.update_course(cursor, connection)
            c.print_course_details()
        elif course_management_choice == '3':
            course_id = input('Input the course ID you want to delete: ')
            Course.delete_course(course_id, cursor, connection)
        elif course_management_choice == '4':
            Course.print_all_courses_details(cursor, connection)
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