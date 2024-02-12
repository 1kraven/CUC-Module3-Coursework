# importing needed libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
import subprocess

# database connection
connect=sqlite3.connect("managementsystem_db.db")
cursor = connect.cursor()

connect.execute('''CREATE TABLE IF NOT EXISTS TeacherInformation (
                        TeacherName TEXT,
                        TeacherID INTEGER PRIMARY KEY,
                        Gender TEXT,
                        DateOfBirth TEXT,
                        Address TEXT,
                        ContactPhoneNo TEXT,
                        Email TEXT,
                        Course TEXT)''')


# creating tkinter window and giving it the dimension and title
win = tk.Tk()
win.title("CUC Teacher Management System")

# Get the screen resolution
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (1350 // 2)
y = (screen_height // 2) - (700 // 2)

win.geometry("1350x700+{}+{}".format(x, y))


# title within the application
title_label = tk.Label(win,text="CUC Teacher Management System",font=("Calibri",30,"bold"),border=12,relief=tk.GROOVE,bg="lightgrey")
title_label.pack(side=tk.TOP,fill=tk.X)


# title on the left side of the application
detail_frame = tk.LabelFrame(win,text="Teacher Details",font=("Calibri",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=20,y=90,width=420,height=575)

data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=810,height=575)

# variables
teachername = tk.StringVar()
teacherid = tk.IntVar()
gender = tk.StringVar()
dob = tk.StringVar()
address = tk.StringVar()
contactnumber = tk.StringVar()
email = tk.StringVar()
course = tk.StringVar()

search_by = tk.StringVar()


# definition of buttons

# this fetches all the data from the database
def fetch_data():
    connect = sqlite3.connect("managementsystem_db.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM TeacherInformation")
    rows = cursor.fetchall()
    connect.close()

    teacher_table.delete(*teacher_table.get_children())
    for row in rows:
        teacher_table.insert('', 'end', values=row)

# this function gives a purpose to the "Add button"
def add_func():
    if teachername.get() == '' or teacherid.get() == '' or gender.get() == '' or dob.get() == '':
        messagebox.showerror('Error','Please fill all fields')
    else:
        connect = sqlite3.connect("managementsystem_db.db")
        cursor = connect.cursor()
        insert = str("INSERT INTO TeacherInformation(TeacherName, TeacherID, Gender, DateOfBirth, Address, ContactPhoneNo, Email, Course)" "VALUES(?,?,?,?,?,?,?,,?)")
        cursor.execute(insert, (teachername.get(),int(teacherid.get()),gender.get(),dob.get(),address.get(),contactnumber.get(),email.get(),course.get()))
        connect.commit()
        connect.close()

# this function prints all the data from the database out on the right hand side when the program is opened
def populate_fields(event):
    selected_row = teacher_table.focus()
    if selected_row:
        data = teacher_table.item(selected_row)
        values = data['values']
        teachername_ent.delete(0, tk.END)
        teachername_ent.insert(0, values[0])
        teacherid_ent.delete(0, tk.END)
        teacherid_ent.insert(0, values[1])
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

# this function gives the "Update" button the purpose to update any already existing data from the database
def update_data():
    selected_row = teacher_table.focus()
    if selected_row:
        data = teacher_table.item(selected_row)
        values = data['values']
        connect = sqlite3.connect("managementsystem_db.db")
        cursor = connect.cursor()
        update = str("UPDATE TeacherInformation SET TeacherName=?, TeacherID=?, Gender=?, DateOfBirth=?, Address=?, ContactPhoneNo=?, Email=?, Course=? WHERE TeacherID=?")
        cursor.execute(update, (teachername.get(), int(teacherid.get()), gender.get(), dob.get(), address.get(), contactnumber.get(), email.get(), course.get(), values[1]))
        connect.commit()
        connect.close()
        fetch_data()
        clear_fields()

# function to clear all the fields
def clear_fields():
    teachername.set("")
    teacherid.set("")
    gender.set("")
    dob.set("")
    address.set("")
    contactnumber.set("")
    email.set("")
    course.set("")

# call the function to clear all the fields
clear_fields()

# this function give a purpose to the "Delete" button that it will delete the row which is currently selected in the table
def delete_func():
    selected_row = teacher_table.focus()
    if selected_row:
        data = teacher_table.item(selected_row)
        values = data['values']
        teacher_id = values[1]
        connect = sqlite3.connect("managementsystem_db.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM TeacherInformation WHERE TeacherID=?", (teacher_id,))
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
        if option == "Students":
            win.destroy()
            subprocess.call(["python", "studentmanagement.py"])

    ttk.Radiobutton(options_frame, text="Students", variable=option_var, value="Students", command=go_to_selected_option).pack(padx=10, pady=5)

    go_button = ttk.Button(options_frame, text="Go", command=go_to_selected_option)
    go_button.pack(padx=10, pady=10)


def search_teachers():
    search_text = search_by.get().lower()
    teacher_table.delete(*teacher_table.get_children())
    connect = sqlite3.connect("managementsystem_db.db")
    cursor = connect.cursor()

    cursor.execute(
        "SELECT * FROM TeacherInformation WHERE lower(TeacherName) LIKE ? OR lower(Course) LIKE ? OR lower(TeacherID) LIKE ?",
        ("%" + search_text + "%", "%" + search_text + "%", "%" + search_text + "%"),
    )
    rows = cursor.fetchall()
    connect.close()

    for row in rows:
        teacher_table.insert('', 'end', values=row)


# all the allocated spaces where the admin can insert data
teachername_lbl = tk.Label(detail_frame,text="Teacher Name ",font=("Arial",15),bg="lightgrey")
teachername_lbl.grid(row=0,column=0,padx=2,pady=2)

teachername_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=teachername)
teachername_ent.grid(row=0,column=1,padx=2,pady=2)

teacherid_lbl = tk.Label(detail_frame,text="Teacher ID ",font=("Arial",15),bg="lightgrey")
teacherid_lbl.grid(row=1,column=0,padx=2,pady=2)

teacherid_ent = tk.Entry(detail_frame,bd=7,font=("Arial",15),width=17,textvariable=teacherid)
teacherid_ent.grid(row=1,column=1,padx=2,pady=2)

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
    search_frame, text="Search", font=("Calibri", 13), bd=9, width=14, bg="lightgrey", command=search_teachers)
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame,text="Show All",font=("Calibri",13),bd=9,width=14,bg="lightgrey", command=fetch_data)
showall_btn.grid(row=0,column=3,padx=12,pady=2)


# database frame

main_frame = tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)


teacher_table = ttk.Treeview(main_frame,column=("Teacher Name", "Teacher ID", "Gender", "Date of birth", "Address", "Contact Phone No.", "Email", "Course"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=teacher_table.yview)
x_scroll.config(command=teacher_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

teacher_table.heading("Teacher Name",text="Teacher Name")
teacher_table.heading("Teacher ID",text="Teacher ID")
teacher_table.heading("Gender",text="Gender")
teacher_table.heading("Date of birth",text="Date of birth")
teacher_table.heading("Address",text="Address")
teacher_table.heading("Contact Phone No.",text="Contact Phone No.")
teacher_table.heading("Email",text="Email")
teacher_table.heading("Course",text="Course")

teacher_table['show'] = 'headings'

teacher_table.column("Teacher Name",width=100)
teacher_table.column("Teacher ID",width=100)
teacher_table.column("Gender",width=100)
teacher_table.column("Date of birth",width=150)
teacher_table.column("Address",width=150)
teacher_table.column("Contact Phone No.",width=170)
teacher_table.column("Email",width=170)
teacher_table.column("Course",width=150)


teacher_table.pack(fill=tk.BOTH,expand=True)

fetch_data()
teacher_table.bind("<ButtonRelease-1>", populate_fields)

win.mainloop()