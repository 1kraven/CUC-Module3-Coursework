import tkinter as tk
from tkinter import messagebox
import sqlite3
import sys
import subprocess

def login():
    username = username_entry.get()
    password = password_entry.get()

    connect = sqlite3.connect("student.db")
    cursor = connect.cursor()
    connect.execute('''CREATE TABLE IF NOT EXISTS logininformation (
                        username TEXT PRIMARY KEY,
                        password TEXT)''')
    connect.commit()

    cursor.execute("SELECT * FROM logininformation WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    connect.close()

    if result:
        messagebox.showinfo("Login successful", "Welcome, " + username + "!")
        #sys.open("main.py")
        win.destroy()
        subprocess.call(["python", "main.py"])
    else:
        messagebox.showerror("Login failed", "Invalid username or password")

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