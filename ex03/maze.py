import tkinter as tk
import maze_maker as mm #練習問題８
import tkinter.messagebox as tkm
import sys

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    global cx, cy
    global jid
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] != 1:
        cx, cy = mx*100+50, my*100+50 #練習問題１１
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1

    canv.coords("tori", cx, cy)
    if maze_lst[my][mx] == maze_lst[7][14]:
        root.after_cancel(jid)
        tkm.showinfo("ゴール！", "ゴール！おめでとう！！")
        sys.exit()
    if maze_lst[my][mx] == 4:
        tkm.showwarning("ゲームオーバー","ゲームオーバー！！また挑戦してね！")
        sys.exit()

    root.after(100, main_proc)

def count_up():
    global tmr, jid
    tmr += 1
    label["text"] = tmr
    jid = root.after(1000, count_up)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習問題１
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() #練習問題２
    tori = tk.PhotoImage(file="fig/1.png")
    mx, my = 0, 1
    cx, cy = 300, 400
    key = "" #練習問題４
    root.bind("<KeyPress>", key_down) #練習問題５
    root.bind("<KeyRelease>", key_up) #練習問題６
    maze_lst = mm.make_maze(15,9) #練習問題９
    mm.show_maze(canv, maze_lst) #練習問題１０
    main_proc() #練習問題７
    canv.create_image(cx, cy, image=tori, tag="tori") #こうかとんを迷路の上に
    label = tk.Label(root, font=("", 80))
    label.pack()
    tmr = 0
    jid = None
    root.after(1000, count_up)
    root.mainloop()