import tkinter as tk
def button_click():
 print=("ujalla ")
 lable.config(bg='yellow')
 button.config(bg='green')
 print("You typed", entry.get())

window=tk.Tk()

window.title("UJALLA fa24-b")
window.geometry("400x200")
button=tk.Button(window, text="click me", command=button_click)
button.pack()
lable = tk.Label(window, text="Hello, Tkinter!", bg= "green" ,font=("Arial",16))
lable.pack()
lable1 = tk.Label(window, text="Welcome To My App!", bg= "green" ,font=("Arial",16))
lable1.pack()

entry = tk.Entry(window, width=30)
entry.pack()
window.mainloop()