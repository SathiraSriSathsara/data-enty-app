import tkinter as tk
from tkinter import ttk, PhotoImage
import csv
import os

# Create the main window (actual application code)
def create_main_window():
    root = tk.Tk()
    root.title("Product Entry Application")
    root.geometry("600x600")
    root.resizable(False, False)  # Remove window resizing

    # Modern themed style
    style = ttk.Style(root)
    style.theme_use('clam')

    # Success message label (will update after each product entry)
    success_message = tk.StringVar()
    success_message.set("Product ID: 1")
    success_label = ttk.Label(root, textvariable=success_message, font=("Arial", 12), foreground="green")
    success_label.pack(pady=10)

    # Auto-increment ID based on CSV file contents
    if not os.path.exists("products.csv"):
        current_id = 1
    else:
        with open("products.csv", "r") as file:
            last_id = 0
            reader = csv.reader(file)
            for row in reader:
                if row and row[0].isdigit():
                    last_id = int(row[0])
            current_id = last_id + 1

    # Function to save data to CSV file
    def save_data(event=None):
        nonlocal current_id
        barcode = barcode_entry.get()
        name = name_entry.get()
        price = price_entry.get()
        stock = stock_entry.get()
        category = category_entry.get()
        unit = unit_entry.get()

        if barcode and name and price and stock and category and unit:  # Ensure all fields are filled
            # Write the data to the CSV file
            with open("products.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([current_id, barcode, name, price, stock, category, unit])

            success_message.set(f"Product ID {current_id} saved successfully!")
            
            current_id += 1  # Increment the ID for the next entry

            # Clear the entry fields
            clear_fields()

            # Focus back to the first entry field
            barcode_entry.focus()
        else:
            success_message.set("All fields must be filled out!")  # Error message if any field is empty

    # Clear the input fields function
    def clear_fields():
        barcode_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        unit_entry.delete(0, tk.END)

    # Form labels and entry boxes
    ttk.Label(root, text="Barcode:").pack(pady=5)
    barcode_entry = ttk.Entry(root)
    barcode_entry.pack(pady=5)

    ttk.Label(root, text="Name:").pack(pady=5)
    name_entry = ttk.Entry(root)
    name_entry.pack(pady=5)

    ttk.Label(root, text="Price:").pack(pady=5)
    price_entry = ttk.Entry(root)
    price_entry.pack(pady=5)

    ttk.Label(root, text="Stock:").pack(pady=5)
    stock_entry = ttk.Entry(root)
    stock_entry.pack(pady=5)

    ttk.Label(root, text="Category:").pack(pady=5)
    category_entry = ttk.Entry(root)
    category_entry.pack(pady=5)

    ttk.Label(root, text="Unit of Measurement:").pack(pady=5)
    unit_entry = ttk.Entry(root)
    unit_entry.pack(pady=5)

    # Bind the Enter key to navigate between fields, and auto-save at the last field
    def navigate(event, next_entry=None):
        if next_entry:
            next_entry.focus()
        else:
            save_data()

    barcode_entry.bind("<Return>", lambda event: navigate(event, name_entry))
    name_entry.bind("<Return>", lambda event: navigate(event, price_entry))
    price_entry.bind("<Return>", lambda event: navigate(event, stock_entry))
    stock_entry.bind("<Return>", lambda event: navigate(event, category_entry))
    category_entry.bind("<Return>", lambda event: navigate(event, unit_entry))
    unit_entry.bind("<Return>", save_data)  # Save data on pressing Enter in the last input

    # Save Button
    save_button = ttk.Button(root, text="Save", command=save_data)
    save_button.pack(pady=10)

    # Clear Button
    clear_button = ttk.Button(root, text="Clear", command=clear_fields)
    clear_button.pack(pady=5)

    root.mainloop()

# Function to show the main window after the splash screen
def show_main_window():
    splash.destroy()  # Close the splash screen
    create_main_window()  # Show the main window

# Function to fade in the splash screen
def fade_in(window, alpha=0):
    if alpha < 1:
        alpha += 0.05  # Increment the alpha value
        window.attributes("-alpha", alpha)  # Set the window transparency
        window.after(50, fade_in, window, alpha)  # Continue fading in
    else:
        # After fade-in, proceed to show the main window
        window.after(1000, show_main_window)  # Add a slight delay before moving to the main window

# Create the splash screen
splash = tk.Tk()
splash.geometry("300x300")
splash.overrideredirect(True)  # Remove window borders and controls
splash.attributes("-topmost", True)  # Keep splash screen on top
splash.attributes("-alpha", 0.0)  # Start with full transparency for fade effect

# Add the logo to the splash screen
logo = PhotoImage(file="logo.png")  # Replace with your logo file path
logo_label = ttk.Label(splash, image=logo)
logo_label.pack(pady=50)

# Loading message (optional)
loading_label = ttk.Label(splash, text="Loading, please wait...", font=("Arial", 12))
loading_label.pack(pady=20)

# Center the splash screen on the screen
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = (screen_width // 2) - (300 // 2)
y = (screen_height // 2) - (300 // 2)
splash.geometry(f"300x300+{x}+{y}")

# Start fading in the splash screen
fade_in(splash)

# Start the splash screen event loop
splash.mainloop()
