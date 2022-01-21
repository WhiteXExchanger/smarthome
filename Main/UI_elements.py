import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.messagebox import showinfo

from matplotlib import container


class MainWindow(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.geometry(str(height)+'x'+str(height)) # Main window resolution

        defaultColor = '#300F47' # Hexadecimal value for Main window color.
        colorList = ['#300F47','#330e45'] # Some other colors

        self['bg'] = defaultColor # Binding Main window color to: defaultColor

        self.menu = self.MenuBar(self) # Creating menu widget.
        self.app = self.AppFrame(self,2) # Creating application widget.

    def close(self):
        self.quit()

    class MenuBar(tk.Menu):
        def __init__(self, container):
            super().__init__(container, bg='grey')
            
            self.filemenu = Menu(self, tearoff=0)
            self.filemenu.add_command(label="New", command='')
            self.filemenu.add_command(label="Open", command='')
            self.filemenu.add_command(label="Save", command='')
            self.filemenu.add_separator()
            self.filemenu.add_command(label="Exit", command=container.quit, activebackground='red')
            self.add_cascade(label="File", menu=self.filemenu)

            self.viewmenu = Menu(self, tearoff=0)
            self.viewmenu.add_command(label="Background", command='')
            self.add_cascade(label="View", menu=self.viewmenu)

            self.helpmenu = Menu(self, tearoff=0)
            self.helpmenu.add_command(label="About", command='')
            self.add_cascade(label="Help", menu=self.helpmenu)

            container.config(menu=self) # Sending back the menu for the Main window

    class AppFrame(tk.Frame):
        def __init__(self, container, floors):
            super().__init__(container, bg='blue')
            self.pack(
                expand=True,
                fill='both',
                padx=50,
                pady=50)
            self.floors=floors

            self.create_floors()

        def create_floors(self):
            for floor in range(self.floors):
                tk.Button(self, text="img", font=24, bg="green")
                tk.Button(self, text="img", font=18, bg="green")
                tk.Button(self, text="img", font=12, bg="green")

            for widget in self.winfo_children():
                widget.pack(side='bottom', padx=5, pady=5, expand=True)

        class Cell_Frame(tk.Frame):
            """Button / Image (Cell) frame\n
            Main button -> Open\n
            Img\n
            Rename button\n
            Set_image button\n
            Del button
            """

            def __init__(self, container):
                super().__init__(container)

                self= tk.Frame(container)

                self.button = tk.Button(self)
                self.button.pack()

class Example_Frame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label
        self.label = tk.Label(self, text='Hello, Tkinter!')
        self.label.pack(**options)
        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack(**options)

        # show the frame on the container
        self.pack(**options)

    def button_clicked(self):
        showinfo(title='',
                 message='Hello, Tkinter!')

"""
# Create a treeview
tree = ttk.Treeview(root)
"""

"""
def rename(str):
    for selected_item in tree.selection():
        tree.item(selected_item,text=str) #Meg kell oldani

def item_selected(event):
    print(event)
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
"""
"""
tree.bind('<<TreeviewSelect>>', )
#image = make_image_label(root, 10, 10, 10, 40)
image= Button(root, image=img, command=lambda: rename(), width=100, height=100,
borderwidth=0)

for property in city.properties:
    tree.insert('', tk.END, text=property.name, iid=property.id, open=False)
    for room in property.rooms:
        tree.insert(property.id, tk.END, text=room.name,
                    iid=room.id, open=False, values=str(room.isGarage))
        for window in room.windows:
            tree.insert(room.id, tk.END, text=window.name,
                        iid=window.id, open=False)
        for lamp in room.lamps:
            tree.insert(room.id, tk.END, text=lamp.name,
                        iid=lamp.id, open=False)
        for temp_sensor in room.temp_sensors:
            tree.insert(room.id, tk.END, text=temp_sensor.name,
                        iid=temp_sensor.id, open=False)
"""

if __name__ == "__main__":
    width=1024
    height=768
    app = MainWindow(width,height)

    app.mainloop()
else:
    pass
