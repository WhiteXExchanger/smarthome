import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.messagebox import showinfo

from matplotlib import container

class SettingsValues(object):
    def __init__(self):
        self.background = self.Background()
        self.text = self.Text()
        self.image = self.Image()

    class Background():
        def __init__(self):
            self.color = '#000000'
            self.faverites = ['#300F47','#330e45']
    
    class Text():
        def __init__(self):
            self.font = 24
            self.color = '#FFFFFF'
                
    class Image():
        def __init__(self):
            pass

settings = SettingsValues()

class MainWindow(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.geometry(str(height)+'x'+str(height)) # Main window resolution

        defaultColor = settings.background.color # Hexadecimal value for Main window color.

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

            self.create_floors()

        def create_floors(self):
            self.FloorFrame(self)
            self.FloorFrame(self)

            for widget in self.winfo_children():
                widget.pack(side='bottom', padx=10, pady=10, ipadx=10, ipady=10, expand=True, fill='both')

        class FloorFrame(tk.Frame):
            def __init__(self, container):
                super().__init__(container, bg='yellow')
                self.pack(
                    side='bottom',
                    padx=5,
                    pady=5,
                    expand=True,
                    fill='both')

        class CellFrame(tk.Frame):
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
