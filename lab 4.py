# import tkinter as tk
#
# window = tk.Tk()
#
# label = tk.Label(window, text="Hello, Tkinter!", fg="blue", bg="yellow", padx=10, pady=5)
# label.pack()
#
# button = tk.Button(window, text="Click Me", width=15, command=lambda: print("Button clicked!"))
# button.pack()
#
# window.mainloop()
# import tkinter as tk
# window = tk.Tk()
# label = tk.Label(window, text="Initial Text")
# label.pack()
# current_text = label.cget("text")
# print("Current text:", current_text)
# current_bg = label.config()["bg"][-1]
# print("Current background:", current_bg)
# window.mainloop()
# import tkinter as tk
# window = tk.Tk()
# label = tk.Label(window, text="Initial Text")
# label.pack()
# label.config(text="Updated Text", fg="red", font=("Arial",16))
# label["bg"] = "lightgreen"
# window.mainloop()
# import tkinter as tk
# def handle_click(event):
#     print("Mouse clicked at", event.x, event.y)
# def handle_key(event):
#     print("Key pressed:", event.char)
# window = tk.Tk()
# button = tk.Button(window, text="Click Me")
# button.pack()
# entry = tk.Entry(window)
# entry.pack()
# button.bind("<Button-1>", handle_click)
# entry.bind("<Key>", handle_key)
# window.mainloop()
import tkinter as tk
def change_color(event):
    event.widget.config(bg="lightblue")
def reset_color(event):
    event.widget.config(bg="SystemButtonFace")
window = tk.Tk()
button = tk.Button(window, text="Hover Me")
button.pack(padx=20, pady=20)
button.bind("<Enter>", change_color)
button.bind("<Leave>", reset_color)
window.mainloop()




