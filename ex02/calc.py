import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("500x700")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)


def click_equal(event):
    equal = entry.get()
    #if equal in "×":
    #equal.replace("×","*")
    res = eval(equal)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

#ACを押すとentryをリセットする機能
def click_AC(event):
    entry.delete(0, tk.END)


#数字ボタンを追加
for num in range(10):
    button = tk.Button(root, text=9-num, font=("Times New Roman", 30), width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row=num//3+1,column=num%3)

#演算子ボタンを追加
operator_list = ["/", "*", "-", "+"]
for ol in operator_list:
    button = tk.Button(root, text=ol, font=("Times New Roman", 30), width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row=operator_list.index(ol)+1,column=4)


#.(小数点)ボタンを追加
button = tk.Button(root, text=".", font=("Times New Roman", 30), width=4, height=2)
button.bind("<1>", button_click)
button.grid(row=4,column=1)

#=で実行する機能を追加
button = tk.Button(root, text="=", font=("Times New Roman", 30), width=4, height=2)
button.bind("<1>", click_equal)
button.grid(row=4,column=2)

#ACのボタンを追加

button = tk.Button(root, text="AC", font=("Times New Roman", 30), width=4, height=2,)
button.bind("<1>", click_AC)
button.grid(row=0,column=4)

#()ボタンを追加
kakko_list = ["(", ")"]
for kl in kakko_list:
    button = tk.Button(root, text=kl, font=("Times New Roman", 30), width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row=kakko_list.index(kl)+1,column=5)



entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)

root.mainloop()