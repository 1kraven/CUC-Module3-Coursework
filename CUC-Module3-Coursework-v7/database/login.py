import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import sqlite3
import sys
import subprocess

def login():
    username = username_entry.get()
    password = password_entry.get()

    connect = sqlite3.connect("managementsystem_db.db")
    cursor = connect.cursor()
    connect.execute('''CREATE TABLE IF NOT EXISTS logininformation (
                        username TEXT PRIMARY KEY,
                        password TEXT)''')
    connect.commit()

    cursor.execute("SELECT * FROM logininformation WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    # This piece of code allows me to insert new usernames and passwords into the database using the GUI
    #if not result:
        #cursor.execute("INSERT INTO logininformation (username, password) VALUES (?, ?)", (username, password))
        #connect.commit()
        #messagebox.showinfo("Account created", "Welcome, " + username + "! Your account has been created successfully.")

    connect.close()

    if result:
        global current_username
        current_username = username
        messagebox.showinfo("Login successful", "Welcome, " + username + "!")
        #sys.open("main.py")
        win.destroy()
        login_go_to()
        #subprocess.call(["python", "studentmanagement.py"])
    else:
        messagebox.showerror("Login failed", "Invalid username or password")


def login_go_to():
    logingoto = tk.Tk()
    logingoto.title("Go To")

    options_frame = ttk.LabelFrame(logingoto, text="Options")
    options_frame.pack(padx=10, pady=10)
    # Get the screen resolution
    screen_width = logingoto.winfo_screenwidth()
    screen_height = logingoto.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (350 // 2)
    y = (screen_height // 2) - (200 // 2)

    logingoto.geometry("350x200+{}+{}".format(x, y))

    option_var = tk.StringVar()

    def go_to_selected_option():
        option = option_var.get()
        if option == "Students":
            subprocess.call(["python", "studentmanagement.py"])
        elif option == "Teachers":
            subprocess.call(["python", "teachermanagement.py"])

    ttk.Radiobutton(options_frame, text="Students", variable=option_var, value="Students", command=go_to_selected_option).pack(padx=10, pady=5)
    ttk.Radiobutton(options_frame, text="Teachers", variable=option_var, value="Teachers", command=go_to_selected_option).pack(padx=10, pady=5)

    go_button = ttk.Button(options_frame, text="Go", command=go_to_selected_option)
    go_button.pack(padx=10, pady=10)

# Create the login window
win = tk.Tk()
win.title("Login")

# Get the screen resolution
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (300 // 2)
y = (screen_height // 2) - (200 // 2)

win.geometry("300x200+{}+{}".format(x, y))

# Create the username and password labels and entry fields
username_label = tk.Label(win, text="Username:")
username_label.place(relx=0.5, rely=0.2, anchor='center')
username_entry = tk.Entry(win)
username_entry.place(relx=0.5, rely=0.3, anchor='center', width=200, height=20)

password_label = tk.Label(win, text="Password:")
password_label.place(relx=0.5, rely=0.5, anchor='center')
password_entry = tk.Entry(win, show="*")
password_entry.place(relx=0.5, rely=0.6, anchor='center', width=200, height=20)

# Create the login button
login_button = tk.Button(win, text="Login", command=login)
login_button.place(relx=0.5, rely=0.8, anchor='center', width=100, height=30)

# Run the window's main loop
win.mainloop()