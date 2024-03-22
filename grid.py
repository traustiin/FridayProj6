import tkinter as tk

def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)
    # You can perform further actions here such as saving the data to a file or database

# Create main window
root = tk.Tk()
root.title("Sign Up Page")

# Labels
name_label = tk.Label(root, text="Name:")
email_label = tk.Label(root, text="Email:")
password_label = tk.Label(root, text="Password:")

# Entry widgets
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # Show asterisks for password entry

# Button
sign_up_button = tk.Button(root, text="Sign Up Now", command=sign_up)

# Grid layout
name_label.grid(row=0, column=0, sticky="w")
email_label.grid(row=1, column=0, sticky="w")
password_label.grid(row=2, column=0, sticky="w")
name_entry.grid(row=0, column=1, padx=10, pady=5)
email_entry.grid(row=1, column=1, padx=10, pady=5)
password_entry.grid(row=2, column=1, padx=10, pady=5)
sign_up_button.grid(row=3, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
