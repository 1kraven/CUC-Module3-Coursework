# dictionary to store permissions for different users
permissions = {
    "admin": ["add_btn", "clear_btn", "update_btn", "delete_btn", "go_to_btn", "search_btn", "showall_btn", "search_in"],
    "teacher": ["clear_btn", "go_to_btn", "search_btn", "showall_btn", "search_in"]
}

# function to check if a user has permission to use a button
def check_permission(user, button):
    if user not in permissions:
        return False
    if button not in permissions[user]:
        return False
    return True

# function to check if a user has permission to use a button, and show an error message if they don't
def check_permission_or_error(user, button):
    if not check_permission(user, button):
        import tkinter as tk
        tk.messagebox.showerror("Permission denied", "No permission allowed")