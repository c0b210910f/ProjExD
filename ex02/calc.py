import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x600")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)

def click_equal(event):
    equal = entry.get()
    res = eval(equal)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

#数字
for num in range(10):
    button = tk.Button(root, text=9-num, font=("Times New Roman", 30), width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row=num//3+1,column=num%3)

#+演算子
button = tk.Button(root, text="+", font=("Times New Roman", 30), width=4, height=2)
button.bind("<1>", button_click)
button.grid(row=4,column=1)

#=
button = tk.Button(root, text="=", font=("Times New Roman", 30), width=4, height=2)
button.bind("<1>", click_equal)
button.grid(row=4,column=2)

entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)

root.mainloop()