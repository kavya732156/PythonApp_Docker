import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Evaluate the expression in the entry
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")  # Width x Height

# Entry widget to display input/output
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create buttons dynamically
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), height=2, width=5)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

# Run the Tkinter event loop
root.mainloop()

