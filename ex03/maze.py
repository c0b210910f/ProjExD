import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習問題１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() #練習問題２

    tori = tk.PhotoImage(file="fig/1.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") #練習問題３

    root.mainloop()