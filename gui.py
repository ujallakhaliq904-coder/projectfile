import tkinter as tk

window=tk.Tk()

window.title("My first gui app with fa24-b")
window.geometry("400x200")



lable = tk.Label(window, text="Hello, Tkinter!", bg= "green" ,font=("Arial",16))
lable.pack()
lable1 = tk.Label(window, text="Welcome To My App!", bg= "green" ,font=("Arial",16))
lable1.pack()
button=tk.button(window, text="click me", command=button_click)
button.pack()

window.mainloop()

