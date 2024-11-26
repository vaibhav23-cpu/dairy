import tkinter as tk
from tkinter import messagebox, filedialog
import datetime

# Function to save diary entry
def save_entry():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        try:
            # Get the current date
            date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Ask user where to save the file
            file_path = filedialog.asksaveasfilename(
                initialfile=f"Diary_{date}.txt",
                defaultextension=".txt",
                filetypes=[("Text files", ".txt"), ("All files", ".*")]
            )
            if file_path:
                with open(file_path, "w") as file:
                    file.write(content)
                messagebox.showinfo("Success", "Diary entry saved!")
                text_area.delete("1.0", tk.END)  # Clear the text area
        except Exception as e:
            messagebox.showerror("Error", f"Could not save entry: {e}")
    else:
        messagebox.showwarning("Warning", "Diary entry cannot be empty!")

# Function to open and view an existing diary entry
def open_entry():
    try:
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text files", ".txt"), ("All files", ".*")]
        )
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            text_area.delete("1.0", tk.END)  # Clear the text area
            text_area.insert("1.0", content)
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")

# Function to clear the current entry
def clear_entry():
    text_area.delete("1.0", tk.END)

# Main application window
root = tk.Tk()
root.title("Personal Diary")

# GUI Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Text Area for Diary Entry
text_area = tk.Text(frame, wrap="word", font=("Arial", 14), height=15, width=50)
text_area.pack(padx=10, pady=10)

# Button Controls
button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

save_button = tk.Button(button_frame, text="Save Entry", font=("Arial", 12), command=save_entry)
save_button.pack(side="left", padx=5)

open_button = tk.Button(button_frame, text="Open Entry", font=("Arial", 12), command=open_entry)
open_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Clear Entry", font=("Arial", 12), command=clear_entry)
clear_button.pack(side="left", padx=5)

# Run the application
root.mainloop()