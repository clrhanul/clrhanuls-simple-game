import tkinter as tk
from random import randint


def up(ev):
    generate_num()
    re_render()
def left(ev):
    generate_num()
    re_render()
def down(ev):
    generate_num()
    re_render()
def right(ev):
    generate_num()
    re_render()


def re_render():
    global grid, dp_grid
    for x in range(4):
        for y in range(4):
            dp_grid[x][y].config(text=" " if not grid[x][y] else grid[x][y])

def generate_num():
    if sum(map(lambda y: sum(map(lambda x: x!=0, y)), grid)) == 16:
        return game_over()
    x, y = (randint(0,3), randint(0,3))
    while grid[x][y] != 0:
        x, y = (randint(0,3), randint(0,3))
    grid[x][y] = [2,4][randint(0,1)]

def game_over():
    print("game_over")


root = tk.Tk(__name__)
root.title("2048 (Made By clrhanul)")
root.geometry("348x348")
root.resizable(False, False)

root.bind("<Up>", up)
root.bind("w", up)
root.bind("<Left>", left)
root.bind("a", left)
root.bind("<Down>", down)
root.bind("s", down)
root.bind("<Right>", right)
root.bind("d", right)

group = tk.Frame(root, bg="black")
group.pack(padx=10, pady=10, expand=True, fill="both")
dp_grid = []
for y in range(4):
    dp_grid.append([])
    line = tk.Frame(group, bg="black")
    line.pack(expand=True, fill="both")
    for x in range(4):
        obj = tk.Label(line, text=0)
        obj.pack(expand=True, fill="both", side='left', padx=1, pady=1)
        dp_grid[-1].append(obj)

grid = [[0 for _ in range(4)] for _ in range(4)]

generate_num()
re_render()

root.mainloop()