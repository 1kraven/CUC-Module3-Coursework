# importing needed libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os


# database connection
connect=sqlite3.connect("student.db")
cursor = connect.cursor()

connect.execute('''CREATE TABLE IF NOT EXISTS StudentInformation (
                        StudentName TEXT,
                        StudentID INTEGER PRIMARY KEY,
                        Gender TEXT,
                        DateOfBirth TEXT,
                        Address TEXT,
                        ContactPhoneNo TEXT,
                        Email TEXT,
                        Course TEXT,
                        Attendance INTEGER)''')
#cursor.execute("SELECT * FROM StudentInformation")
#connect.commit()
#connect.close()


# creating tkinter window and giving it the dimension and title
win = tk.Tk()
win.title("CUC Student Management System")

# Get the screen resolution
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (1350 // 2)
y = (screen_height // 2) - (700 // 2)

win.geometry("1350x700+{}+{}".format(x, y))


# title within the application
title_label = tk.Label(win,text="CUC Student Management System",font=("Calibri",30,"bold"),border=12,relief=tk.GROOVE,bg="lightgrey")
title_label.pack(side=tk.TOP,fill=tk.X)


# title on the left side of the application
detail_frame = tk.LabelFrame(win,text="Student Details",font=("Calibri",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=20,y=90,width=420,height=575)

data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=810,height=575)

# variables
studentname = tk.StringVar()
studentid = tk.IntVar()
gender = tk.StringVar()
dob = tk.StringVar()
address = tk.StringVar()
contactnumber = tk.StringVar()
email = tk.StringVar()
course = tk.StringVar()
attendance = tk.IntVar()

search_by = tk.StringVar()


# definition of buttons

# this fetches all the data from the database
def fetch_data():
    connect = sqlite3.connect("student.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM StudentInformation")
    rows = cursor.fetchall()
    connect.close()

    student_table.delete(*student_table.get_children())
    for row in rows:
        student_table.insert('', 'end', values=row)

# this function gives a purpose to the "Add button"
def add_func():
    if studentname.get() == '' or studentid.get() == '' or gender.get() == '' or dob.get() == '':
        messagebox.showerror('Error','Please fill all fields')
    else:
        connect = sqlite3.connect("student.db")
        cursor = connect.cursor()
        insert = str("INSERT INTO StudentInformation(StudentName, StudentID, Gender, DateOfBirth, Address, ContactPhoneNo, Email, Course, Attendance)" "VALUES(?,?,?,?,?,?,?,?,?)")
        cursor.execute(insert, (studentname.get(),int(studentid.get()),gender.get(),dob.get(),address.get(),contactnumber.get(),email.get(),course.get(),int(attendance.get())))
        connect.commit()
        connect.close()

# this function prints all the data from the database out on the right hand side when the program is opened
def populate_fields(event):
    selected_row = student_table.focus()
    if selected_row:
        data = student_table.item(selected_row)
        values = data['values']
        studentname_ent.delete(0, tk.END)
        studentname_ent.insert(0, values[0])
        studentid_ent.delete(0, tk.END)
        studentid_ent.insert(0, values[1])
        gender_ent.set(values[2])
        dob_ent.delete(0, tk.END)
        dob_ent.insert(0, values[3])
        address_ent.delete(0, tk.END)
        address_ent.insert(0, values[4])
        contactnumber_ent.delete(0, tk.END)
        contactnumber_ent.insert(0, values[5])
        email_ent.delete(0, tk.END)
        email_ent.insert(0, values[6])
        course_ent.delete(0, tk.END)
        course_ent.insert(0, values[7])
        attendance_ent.delete(0, tk.END)
        attendance_ent.insert(0, values[8])

# this function gives the "Update" button the purpose to update any already existing data from the database
def update_data():
    selected_row = student_table.focus()
    if selected_row:
        data = student_table.item(selected_row)
        values = data['values']
        connect = sqlite3.connect("student.db")
        cursor = connect.cursor()
        update = str("UPDATE StudentInformation SET StudentName=?, StudentID=?, Gender=?, DateOfBirth=?, Address=?, ContactPhoneNo=?, Email=?, Course=?, Attendance=? WHERE StudentID=?")
        cursor.execute(update, (studentname.get(), int(studentid.get()), gender.get(), dob.get(), address.get(), contactnumber.get(), email.get(), course.get(), int(attendance.get()), values[1]))
        connect.commit()
        connect.close()
        fetch_data()
        clear_fields()

# function to clear all the fields
def clear_fields():
    studentname.set("")
    studentid.set("")
    gender.set("")
    dob.set("")
    address.set("")
    contactnumber.set("")
    email.set("")
    course.set("")
    attendance.set("")

# call the function to clear all the fields
clear_fields()

# this function give a purpose to the "Delete" button that it will delete the row which is currently selected in the table
def delete_func():
    selected_row = student_table.focus()
    if selected_row:
        data = student_table.item(selected_row)
        values = data['values']
        student_id = values[1]
        connect = sqlite3.connect("student.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM StudentInformation WHERE StudentID=?", (student_id,))
        connect.commit()
        connect.close()
        fetch_data()
        clear_fields()

def go_to():
    top = tk.Toplevel()
    top.title("Go To")

    options_frame = ttk.LabelFrame(top, text="Options")
    options_frame.pack(padx=10, pady=10)
    # Get the screen resolution
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (350 // 2)
    y = (screen_height // 2) - (200 // 2)

    top.geometry("350x200+{}+{}".format(x, y))

    option_var = tk.StringVar()

    def go_to_selected_option():
        option = option_var.get()
        if option == "Department":
            os.system("python department.py")
            top.destroy()
            win.destroy()
        elif option == "Course":
            os.system("python course.py")
            top.destroy()
            win.destroy()
        elif option == "Teachers":
            os.system("python teachers.py")
            top.destroy()
            win.destroy()

    ttk.Radiobutton(options_frame, text="Department", variable=option_var, value="Department", command=go_to_selected_option).pack(padx=10, pady=5)
    ttk.Radiobutton(options_frame, text="Course", variable=option_var, value="Course", command=go_to_selected_option).pack(padx=10, pady=5)
    ttk.Radiobutton(options_frame, text="Teachers", variable=option_var, value="Teachers", command=go_to_selected_option).pack(padx=10, pady=5)

    go_button = ttk.Button(options_frame, text="Go", command=go_to_selected_option)
    go_button.pack(padx=10, pady=10)


def search_students():
    search_text = search_by.get().lower()
    student_table.delete(*student_table.get_children())
    connect = sqlite3.connect("student.db")
    cursor = connect.cursor()

    cursor.execute(
        "SELECT * FROM StudentInformation WHERE lower(StudentName) LIKE ? OR lower(Course) LIKE ? OR lower(StudentID) LIKE ?",
        ("%" + search_text + "%", "%" + search_text + "%", "%" + search_text + "%"),
    )
    rows = cursor.fetchall()
    connect.close()

    for row in rows:
        student_table.insert('', 'end', values=row)


# all the allocated spaces where the admin can insert data
studentname_lbl = tk.Label(detail_frame,text="Student Name ",font=("Arial",15),bg="lightgrey")
studentname_lbl.grid(row=0,column=0,padx=2,pady=2)

studentname_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=studentname)
studentname_ent.grid(row=0,column=1,padx=2,pady=2)

studentid_lbl = tk.Label(detail_frame,text="Student ID ",font=("Arial",15),bg="lightgrey")
studentid_lbl.grid(row=1,column=0,padx=2,pady=2)

studentid_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=studentid)
studentid_ent.grid(row=1,column=1,padx=2,pady=2)

gender_lbl = tk.Label(detail_frame,text="Gender ",font=("Arial",15),bg="lightgrey")
gender_lbl.grid(row=2,column=0,padx=2,pady=2)

gender_ent = ttk.Combobox(detail_frame,font=("Arial",15),width=17,textvariable=gender)
gender_ent['values'] = ("Male", "Female")
gender_ent.grid(row=2,column=1,padx=2,pady=2)

dob_lbl = tk.Label(detail_frame,text="Date of birth ",font=("Arial",15),bg="lightgrey")
dob_lbl.grid(row=3,column=0,padx=2,pady=2)

dob_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=dob)
dob_ent.grid(row=3,column=1,padx=2,pady=2)

address_lbl = tk.Label(detail_frame,text="Address ",font=("Arial",15),bg="lightgrey")
address_lbl.grid(row=4,column=0,padx=2,pady=2)

address_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=address)
address_ent.grid(row=4,column=1,padx=2,pady=2)

contactnumber_lbl = tk.Label(detail_frame,text="Contact Phone No. ",font=("Arial",15),bg="lightgrey")
contactnumber_lbl.grid(row=5,column=0,padx=2,pady=2)

contactnumber_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=contactnumber)
contactnumber_ent.grid(row=5,column=1,padx=2,pady=2)

email_lbl = tk.Label(detail_frame,text="Email ",font=("Arial",15),bg="lightgrey")
email_lbl.grid(row=6,column=0,padx=2,pady=2)

email_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=email)
email_ent.grid(row=6,column=1,padx=2,pady=2)

course_lbl = tk.Label(detail_frame,text="Course ",font=("Arial",15),bg="lightgrey")
course_lbl.grid(row=7,column=0,padx=2,pady=2)

course_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=course)
course_ent.grid(row=7,column=1,padx=2,pady=2)

attendance_lbl = tk.Label(detail_frame,text="Attendance ",font=("Arial",15),bg="lightgrey")
attendance_lbl.grid(row=8,column=0,padx=2,pady=2)

attendance_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=attendance)
attendance_ent.grid(row=8,column=1,padx=2,pady=2)


# buttons to add, update, delete, clear data

btn_frame = tk.Frame(detail_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=42,y=390,width=310,height=120)

add_btn = tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Calibri"),width=12,cursor='hand2',command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="lightgrey",text="Update",bd=7,font=("Calibri"),width=12,command=update_data)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Calibri"), width=12, cursor='hand2', command=delete_func)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="lightgrey",text="Clear",bd=7,font=("Calibri"),width=12, command=clear_fields)
clear_btn.grid(row=1,column=1,padx=3,pady=2)

go_to_btn = tk.Button(btn_frame, bg="lightgrey", text="Go To", bd=4, font=("Calibri", 8, "bold"), width=5, height=2, cursor='hand2', command=go_to)
go_to_btn.grid(row=0&1, column=2, padx=3, pady=2, columnspan=2)


# search function

search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Calibri", 14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in = tk.Entry(search_frame, font=("Calibri", 14), textvariable=search_by)
search_in.grid(row=0, column=1, padx=12, pady=2)
search_in.bind("<FocusIn>", lambda event: search_in.config(state="normal"))
search_in.bind("<FocusOut>", lambda event: search_in.config(state="readonly"))

search_btn = tk.Button(
    search_frame, text="Search", font=("Calibri", 13), bd=9, width=14, bg="lightgrey", command=search_students)
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame,text="Show All",font=("Calibri",13),bd=9,width=14,bg="lightgrey", command=fetch_data)
showall_btn.grid(row=0,column=3,padx=12,pady=2)


# database frame

main_frame = tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)


student_table = ttk.Treeview(main_frame,column=("Student Name", "Student ID", "Gender", "Date of birth", "Address", "Contact Phone No.", "Email", "Course", "Attendance"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Student Name",text="Student Name")
student_table.heading("Student ID",text="Student ID")
student_table.heading("Gender",text="Gender")
student_table.heading("Date of birth",text="Date of birth")
student_table.heading("Address",text="Address")
student_table.heading("Contact Phone No.",text="Contact Phone No.")
student_table.heading("Email",text="Email")
student_table.heading("Course",text="Course")
student_table.heading("Attendance",text="Attendance")

student_table['show'] = 'headings'

student_table.column("Student Name",width=100)
student_table.column("Student ID",width=100)
student_table.column("Gender",width=100)
student_table.column("Date of birth",width=150)
student_table.column("Address",width=150)
student_table.column("Contact Phone No.",width=170)
student_table.column("Email",width=170)
student_table.column("Course",width=150)
student_table.column("Attendance",width=100)


student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()
student_table.bind("<ButtonRelease-1>", populate_fields)

win.mainloop()