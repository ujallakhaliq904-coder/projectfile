import tkinter as tk
from tkinter import messagebox


# Function to open Dashboard
def open_dashboard():
    username = entry_username.get()
    password = entry_password.get()

    # Simple login check
    if username == "admin" and password == "1234":
        login_window.destroy()  # Close Login Window

        dashboard = tk.Tk()
        dashboard.title("Dashboard")
        dashboard.geometry("300x200")

        label = tk.Label(dashboard, text="Welcome to Dashboard!", font=("Arial", 14))
        label.pack(pady=50)

        dashboard.mainloop()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# Login Window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

# Username
label_username = tk.Label(login_window, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(login_window)
entry_username.pack(pady=5)

# Password
label_password = tk.Label(login_window, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(login_window, show="*")
entry_password.pack(pady=5)

# Login Button
login_button = tk.Button(login_window, text="Login", command=open_dashboard)
login_button.pack(pady=10)

login_window.mainloop()