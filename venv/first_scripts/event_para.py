import tkinter as tk
from tkinter import messagebox

# Event handler function for button click
def on_button_click():
    messagebox.showinfo("Event Triggered", "Button was clicked!")

# Initialize the main application window
app = tk.Tk()
app.title("Event-Driven Example")
app.geometry("300x200")

# Create a button and attach the event handler
button = tk.Button(app, text="Click Me", command=on_button_click)
button.pack(pady=50)

# Start the event loop
app.mainloop()
