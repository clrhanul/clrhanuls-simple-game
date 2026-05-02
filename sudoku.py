import tkinter as tk

root = tk.Tk(__name__)
root.title("Sudoku (Made By clrhanul)")
root.geometry("400x470")
root.resizable(False, False)

group = tk.Frame(root, background="black", border=3)
group.pack(padx=10, pady=(10, 0))

dp_blocks = []
for y in range(9):
    line = tk.Frame(group, background="black")
    line.pack(anchor="center", pady=(0, 3 if y in [2, 5] else 0))
    for x in range(0, 9):
        btn = tk.Button(line, text=f"{x}{y}", width=3, height=1, font=("Arial", 14), border=1)
        btn.pack(side="left", padx=(0, 3 if x in [2, 5] else 0))
        dp_blocks.append(btn)

selection = []
line = tk.Frame(root, background="black", border=2)
line.pack(side="bottom", pady=(0, 10))
for x in range(1, 10):
    btn = tk.Button(line, text=f"{x}", width=3, height=1, font=("Arial", 14), border=0)
    btn.pack(side="left", padx=(0, 0 if x == 9 else 2))
    selection.append(btn)

root.mainloop()