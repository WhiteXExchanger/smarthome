import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

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

class Main(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.geometry(str(width)+'x'+str(height)) # Main window resolution

        self['bg'] = settings.background.color # Binding Main window color to: hexadecimal value

        self.menu = self.Menu(self) # Creating menu widget.
        self.app = self.App(self) # Creating application widget.

    def refresh():
        """for widget in self.winfo_children():
        widget.pack(side='bottom', padx=10, pady=10, ipadx=10, ipady=10, expand=True, fill='both')"""
        pass

    def close(self):
        self.quit()

    class Menu(tk.Menu):
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

    class App(tk.Frame):
        def __init__(self, container):
            super().__init__(container, bg='blue')
            """self.pack(
                    expand=True,
                    fill='both',
                    padx=50,
                    pady=50
                )"""
            self.pack()
            
            self.floors = []

            self.floors.append(self.create_floors())

        def create_floors(self):
            self.Floor(self)

        class Floor(tk.Frame):
            def __init__(self, container):
                super().__init__(container, bg='yellow')
                """self.pack(
                        side='bottom',
                        padx=10,
                        pady=10,
                        expand=True,
                        fill='both'
                    )"""
                self.pack()
                
                self.create_cell()

            def create_cell(self):
                self.Room(self)

            class Room(tk.Frame):
                def __init__(self, container):
                    super().__init__(container, width=300, height=100, bg='brown')
                    """self.pack(
                            side='left',
                            padx=10,
                            fill='x'
                    )"""

                    self.pack()

                    self.columnconfigure(0, weight=1)
                    self.columnconfigure(1, weight=3)
                    self.columnconfigure(2, weight=1)

                    self.create_buttons()

                def create_buttons(self):
                    self.RoomElements(self)

                class RoomElements(object):
                    def __init__(self, container):
                        
                        self.delete = tk.Button(container, bg='red', text="kuka", width=20, height=20, command=lambda: self.dele(container))
                        self.delete.grid(row=0, column=0)

                        self.label = tk.Label(container, text='Room', width=60, height=20)
                        self.label.grid(row=0, column=1)

                        self.rename = tk.Button(container, bg='white', text="rename", width=20, height=20, command=lambda: self.dele(self.rename))
                        self.rename.grid(row=0, column=2)

                        self.move = tk.Button(container, bg='yellow', text="move", width=20, height=20, command=lambda: self.dele(self.move))
                        self.move.grid(row=3, column=0)

                        self.img = tk.Button(container, bg='green', text="img", width=20, height=20, command=lambda: self.dele(self.img))
                        self.img.grid(row=3, column=1)

                    def dele(self,object):
                        object.destroy()

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
    #width=1024
    #height=768
    app = Main(1024,768)

    app.mainloop()
else:
    pass
