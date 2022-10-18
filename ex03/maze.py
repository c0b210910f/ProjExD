import tkinter as tk
import maze_maker as mm #練習問題８

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1

    if key == "Down":
        my += 1

    if key == "Left":
        mx -= 1

    if key == "Right":
        mx += 1

    if maze_lst[my][mx] == 0:
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
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習問題１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() #練習問題２

    tori = tk.PhotoImage(file="fig/1.png")
    mx, my = 1, 1
    cx, cy = 300, 400
    #canv.create_image(cx, cy, image=tori, tag="tori") #練習問題３

    key = "" #練習問題４

    root.bind("<KeyPress>", key_down) #練習問題５

    root.bind("<KeyRelease>", key_up) #練習問題６

    #main_proc() #練習問題７

    maze_lst = mm.make_maze(15,9) #練習問題９

    mm.show_maze(canv, maze_lst) #練習問題１０

    main_proc() #練習問題７

    canv.create_image(cx, cy, image=tori, tag="tori") #こうかとんを迷路の上に


    root.mainloop()