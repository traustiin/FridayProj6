import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + number)

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widget
entry = tk.Entry(root, width=40, state="disabled")
entry.pack()

# Define buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the frame
for i, btn_text in enumerate(buttons):
    btn = tk.Button(buttons_frame, text=btn_text, width=7, height=3,
                    command=lambda btn_text=btn_text: button_click(btn_text) if btn_text not in {'=', 'C'} else calculate() if btn_text == '=' else clear_display())
    btn.grid(row=i // 4, column=i % 4)

# Disable entry widget
entry.config(state="normal")

# Run the main loop
root.mainloop()




