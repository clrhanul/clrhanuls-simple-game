import tkinter as tk
from random import randint


def up(ev):
    global grid
    grid = rotate90(
        push_right(
    rotate90(rotate90(rotate90(grid)))))
    generate_num()
    re_render()

def left(ev):
    global grid
    grid = rotate90(rotate90(
        push_right(
    rotate90(rotate90(grid)))))
    generate_num()
    re_render()

def down(ev):
    global grid
    grid = rotate90(rotate90(rotate90(
        push_right(
    rotate90(grid)))))
    generate_num()
    re_render()

def right(ev):
    global grid
    grid = push_right(grid)
    generate_num()
    re_render()

def rotate90(array: list[list]):
    line = array[0] + array[1] + array[2] + array[3]
    dump = [0 for _ in range(16)]
    # 시계 방향이 아니라, 반 시계 방향으로 돌아감 ;;;
    pos = {
         1:13,  2:9,   3:5,  4:1,
         5:14,  6:10,  7:6,  8:2,
         9:15, 10:11, 11:7, 12:3,
        13:16, 14:12, 15:8, 16:4
    }
    for i in range(1, 17):
        dump[pos[i]-1] = line[i-1]

    return [[dump.pop(0) for _ in range(4)] for _ in range(4)]

def push_right(array: list[list[int]]):
    d = array[:]
    for y in range(4):
        pivot = 3
        for x in range(3, -1, -1):
            if d[y][x] == 0:
                continue
            if pivot == x:
                pivot -= 1
                continue
            d[y][pivot] = d[y][x]
            pivot -= 1
            d[y][x] = 0

    for x in range(3, 0, -1):
        for y in range(4):
            if d[y][x] == d[y][x-1]:
                d[y][x] *= 2
                d[y][x-1] = 0

    for y in range(4):
        pivot = 3
        for x in range(3, -1, -1):
            if d[y][x] == 0:
                continue
            if pivot == x:
                pivot -= 1
                continue
            d[y][pivot] = d[y][x]
            pivot -= 1
            d[y][x] = 0
    return d


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

group = tk.Frame(root, bg="black", border=1)
group.pack(padx=10, pady=10, expand=True, fill="both")
dp_grid = []
for y in range(4):
    dp_grid.append([])
    line = tk.Frame(group, bg="black")
    line.pack(expand=True, fill="both")
    for x in range(4):
        obj = tk.Label(line, text=0, width=10)
        obj.pack(expand=True, fill="both", side='left', padx=1, pady=1)
        dp_grid[-1].append(obj)

grid = [[0 for _ in range(4)] for _ in range(4)]

generate_num()
re_render()

root.mainloop()