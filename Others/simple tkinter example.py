import tkinter as tk

root = tk.Tk()
root.resizable(width=0, height=0)
root.title("some application")

# menu left
menu_left = tk.Frame(root, width=150, bg="pink")
menu_left.grid(row=0, column=0, rowspan=2, sticky="ns")

menu_left_upper = tk.Frame(menu_left, width=150, height=150, bg="red")
menu_left_upper.pack()
menu_left_lower = tk.Frame(menu_left, width=150, height=150, bg="blue")
menu_left_lower.pack()

# this label breaks the design   
#test = tk.Label(menu_left, text="test")
#test.pack()

# right area
some_title_frame = tk.Frame(root, bg="white")
some_title_frame.grid(row=0, column=1, sticky="we")

some_title = tk.Label(some_title_frame, text="some title", bg="white")
some_title.pack()

canvas_area = tk.Canvas(root, width=500, height=400, background="grey")
canvas_area.grid(row=1, column=1)

root.mainloop()