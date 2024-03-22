import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)
    # You can perform further actions here such as authentication

# Create main window
root = tk.Tk()
root.title("Login Page")

# Labels
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")

# Entry widgets
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # Show asterisks for password entry

# Button
login_button = tk.Button(root, text="Login", command=login)

# Place layout
username_label.place(x=50, y=30)
password_label.place(x=50, y=60)
username_entry.place(x=150, y=30)
password_entry.place(x=150, y=60)
login_button.place(x=100, y=100)

# Run the main loop
root.mainloop()
