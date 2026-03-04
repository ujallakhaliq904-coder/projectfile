import tkinter as tk
def change_color():
    background_color=button.cget("bg")
    if background_color=="green":
        button.config(bg="red")
    else:
        button.config(bg="red")
window = tk.Tk()
window.mainloop()