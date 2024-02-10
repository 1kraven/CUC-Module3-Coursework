import tkinter as tk
from tkinter import ttk
import sqlite3
from classes import *
from database import *

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
c = conn.cursor()

# Function to add a record
def add_record():
    # Get the input values
    name = name_entry.get()
    value = value_entry.get()

    # Insert the new record into the table
    c.execute("INSERT INTO example_table (name, value) VALUES (?, ?)", (name, value))

    # Commit changes and update the table
    conn.commit()
    update_table()

# Function to view all records
def view_records():
    # Clear the previous table
    table.delete(*table.get_children())

    # Fetch all records from the table
    records = c.execute("SELECT * FROM example_table").fetchall()

    # Add the records to the table
    for record in records:
        table.insert("", "end", values=record)

# Function to delete a record
def delete_record():
    # Get the selected record
    selected = table.focus()

    # If a record is selected, delete it
    if selected:
        c.execute("DELETE FROM example_table WHERE id=?", (table.item(selected, 'values')[0],))
        conn.commit()
        update_table()

# Function to update the table
def update_table():
    # Clear the previous table
    table.delete(*table.get_children())

    # Fetch all records from the table
    records = c.execute("SELECT * FROM example_table").fetchall()

    # Add the records to the table
    for record in records:
        table.insert("", "end", values=record)

# Create the main window
window = tk.Tk()

#Set the geometry of tkinter frame
#window.geometry("750x270")

# Set the window title
window.title('Test')

def find_square():
   no =  int(tk.Entry.get())
   tk.Label(window, text=no*no).pack()

# Add a label and entry for the name
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

# Add a label and entry for the value
value_label = tk.Label(window, text="Value:")
value_label.grid(row=1, column=0)
value_entry = tk.Entry(window)
value_entry.grid(row=1, column=1)

# Add a button to add a record
add_button = tk.Button(window, text="Add Record", command=add_record)
add_button.grid(row=2, column=0)

# Add a button to view all records
view_button = tk.Button(window, text="View Records", command=view_records)
view_button.grid(row=2, column=1)

# Create a table to display records
table_header = ["ID", "Name", "Value"]
table = ttk.Treeview(window, columns=table_header, show="headings")
table.grid(row=3, column=0, columnspan=2)

# Configure the table columns
for col in table_header:
    table.heading(col, text=col)

# Add a scrollbar to the table
scrollbar = ttk.Scrollbar(window, orient="vertical", command=table.yview)
scrollbar.grid(row=3, column=2, sticky="ns")
table.configure(yscrollcommand=scrollbar.set)

# Run the main loop
window.mainloop()