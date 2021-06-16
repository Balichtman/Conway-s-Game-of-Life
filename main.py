# Conway's Game of life made by Benjamin Lichtman

import tkinter as tk

window = tk.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
pixelVirtual = tk.PhotoImage(width=1, height=1)


class Life:
    def bring_to_life2(self):
        self.alive = True
        self.btn.configure(background="white")

    def kill2(self):
        self.alive = False
        self.btn.configure(background="black")

    def bring_to_life(self, event):
        self.alive = True
        self.btn.configure(background="white")

    def kill(self, event):
        self.alive = False
        self.btn.configure(background="black")

    def __init__(self):

        self.alive = False
        self.adjacent = 0
        self.btn = tk.Button(window, width=int((width / 64)-4), height=int((height / 36)-4), bg='black',
                             image=pixelVirtual, compound="c", bd=1)
        self.btn.bind("<Enter>", self.bring_to_life)


arr = []
for i in range(64):
    col = []
    for j in range(36):
        b = Life()
        b.btn.grid(row=j, column=i)
        col.append(b)
    arr.append(col)


def adjacent(c, r):
    count = 0
    try:
        if arr[c-1][r].alive:
            count = count+1
    except IndexError:
        count = count
    try:
        if arr[c+1][r].alive:
            count = count+1
    except IndexError:
        count = count
    try:
        if arr[c-1][r-1].alive:
            count = count+1
    except IndexError:
        count = count
    try:
        if arr[c+1][r+1].alive:
            count = count+1
    except IndexError:
        count = count
    try:
        if arr[c-1][r+1].alive:
            count = count+1
    except IndexError:
        count = count
    try:
        if arr[c+1][r-1].alive:
            count = count+1
    except IndexError:
        count = count
    try:
        if arr[c][r+1].alive:
            count = count+1
    except IndexError:
        count = count
    try:
        if arr[c][r-1].alive:
            count = count + 1
    except IndexError:
        count = count
    return count


def check():
    for i in range(64):
        for j in range(36):
            print(adjacent(i, j))
            if arr[i][j].alive and (adjacent(i, j) < 2 or adjacent(i, j) > 3):
                arr[i][j].kill2()
            elif ~arr[i][j].alive and (adjacent(i, j) == 3):
                arr[i][j].bring_to_life2()
    window.after(200, check)


window.title("The Game of Life")
window.geometry(str(width)+"x"+str(height))
window.attributes("-fullscreen", True)
window.after(15000, check)
window.mainloop()







