# Conway's Game of life made by Benjamin Lichtman

import tkinter as tk

window = tk.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
pixelVirtual = tk.PhotoImage(width=1, height=1)
mouseDown = False


def on_mouse_up(event):
    global mouseDown
    mouseDown = ~mouseDown


class Life:

    def bring_to_life2(self):
        self.switch = False
        self.alive = True
        self.btn.configure(background="white")

    def kill2(self):
        self.switch = False
        self.alive = False
        self.btn.configure(background="black")

    def bring_to_life(self, event):
        global mouseDown
        if mouseDown:
            self.alive = True
            self.btn.configure(background="white")

    def __init__(self):
        self.switch = False
        self.alive = False
        self.adjacent = 0
        self.btn = tk.Button(window, width=int((width / 64)-4), height=int((height / 36)-4), bg='black',
                             image=pixelVirtual, compound="c", bd=1, state=tk.DISABLED)
        self.btn.bind("<Enter>", self.bring_to_life)


arr = []
for a in range(64):
    col = []
    for aa in range(36):
        b = Life()
        b.btn.grid(row=aa, column=a)
        col.append(b)
    arr.append(col)


def adjacent(c, r):
    count = 0
    try:
        if arr[c-1][r].alive:
            count = count+1
    except IndexError:
        pass
    try:
        if arr[c+1][r].alive:
            count = count+1
    except IndexError:
        pass
    try:
        if arr[c-1][r-1].alive:
            count = count+1
    except IndexError:
        pass
    try:
        if arr[c+1][r+1].alive:
            count = count+1
    except IndexError:
        pass
    try:
        if arr[c-1][r+1].alive:
            count = count+1
    except IndexError:
        pass
    try:
        if arr[c+1][r-1].alive:
            count = count+1
    except IndexError:
        pass
    try:
        if arr[c][r+1].alive:
            count = count+1
    except IndexError:
        pass
    try:
        if arr[c][r-1].alive:
            count = count + 1
    except IndexError:
        pass
    return count


def check():
    for ii in range(64):
        for jj in range(36):
            if arr[ii][jj].alive and (adjacent(ii, jj) < 2 or adjacent(ii, jj) > 3):
                arr[ii][jj].switch = True
            elif (not arr[ii][jj].alive) and (adjacent(ii, jj) == 3):
                arr[ii][jj].switch = True
            else:
                arr[ii][jj].switch = False
    for i in range(64):
        for j in range(36):
            if arr[i][j].switch and arr[i][j].alive:
                arr[i][j].kill2()
            elif arr[i][j].switch and (not arr[i][j].alive):
                arr[i][j].bring_to_life2()
    window.after(200, check)


window.bind("<ButtonRelease-1>", on_mouse_up)
window.title("Conway's Game of Life")
window.geometry(str(width)+"x"+str(height))
window.attributes("-fullscreen", True)
window.after(15000, check)
window.mainloop()







