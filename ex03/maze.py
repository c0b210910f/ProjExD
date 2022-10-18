import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習問題１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() #練習問題２

    root.mainloop()