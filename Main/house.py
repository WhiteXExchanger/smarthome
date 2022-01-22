import random as rnd

class City(object):
    """ City - Main-class   \n
    Property - Sub-class    \n
    Room - Sub-class    \n
    Window, Lamp, Temp_Sensor - Sub-classes
    """
    def __init__(self):
        self.properties = []
        self.properties_count = 0
        self.id = id(self)
        
    def create_property(self, name:str): #Create House Object
        self.properties.append(Property(name, self.id))
        self.properties_count+=1

    def delete_property(self, id:int): #Delete House Object
        list_lenght = len(self.properties)
        for i in range(list_lenght):
            if (self.properties[i].id == id):
                del self.properties[i]
                self.properties_count-=1
                break

    
    def generate_data(self):
        """# Generates data
            Generates data for testing purposes
        """
        for i in range(rnd.randint(2,3)):
            self.create_property("Building"+str(i+1))

        for i in range(self.properties_count):
            x = rnd.randint(1,3)
            self.properties[i].create_floor(0)
            for j in range(x):
                self.properties[i].floors[0].create_room()
            for j in range(x):
                self.properties[i].floors[0].rooms[j].change_garage(bool(rnd.getrandbits(1)))
                for l in range(rnd.randint(1,3)):
                    self.properties[i].floors[0].rooms[j].create_window("window"+str(l))
                for l in range(rnd.randint(1,3)):
                    self.properties[i].floors[0].rooms[j].create_lamp("lamp"+str(l))
                for l in range(rnd.randint(1,3)):
                    self.properties[i].floors[0].rooms[j].create_temp_sensor("temp_sen"+str(l))

class Property(City):
    def __init__(self, name:str, parent_id:int):
        self.id = id(self)
        self.name = name
        self.parent_id = parent_id
        
        self.floors = []

    def create_floor(self, no):
        self.floors.append(Floor(no,self.id))

    def delete_floor(self, id):
        for i in range(len(self.floors)):
            if (self.floors[i].id == id):
                del self.floors[i]
                break

class Floor(Property):
    def __init__(self, no:int, parent_id: int):
        self.id = id(self)
        self.no = no
        self.parent_id = parent_id
        self.rooms = []

    def create_room(self):
            self.rooms.append(Room("Room", self.id))

    def delete_room(self, id):
        for i in range(len(self.rooms)):
            if (self.rooms[i].id == id):
                del self.rooms[i]
                break

    def rename_room(self, id, new_name):
        for i in range(len(self.rooms)):
            if (self.rooms[i].id == id):
                self.rooms[i].name = new_name
                break

class Room(Floor):
    def __init__(self, name:str, parent_id:int):
        self.id = id(self)
        self.name = name
        self.parent_id = parent_id
        self.isGarage = False

        self.windows = []
        self.lamps = []
        self.temp_sensors = []

    def change_garage(self, isGarage:bool):
        self.isGarage = True if isGarage else False

    def create_window(self, name:str):
        self.windows.append(Window(name, self.id))

    def create_lamp(self, name:str):
        self.lamps.append(Lamp(name, self.id))

    def create_temp_sensor(self, name:str):
        self.temp_sensors.append(Tempsensor(name, self.id))

    def delete_window(self, id:int):
        for i in range(self.windows_count):
            if (self.windows[i].id == id):
                del self.windows[i]
                break

    def delete_lamp(self, id:int):
        for i in range(self.lamps_count):
            if (self.lamps[i].id == id):
                del self.lamps[i]
                break

    def delete_temp_sensor(self, id:int):
        for i in range(self.temp_sensors_count):
            if (self.temp_sensors[i].id == id):
                del self.temp_sensors[i]
                break

class Window(Room):
    def __init__(self, name:str, parent_id:int):
        self.id = id(self)
        self.name = name
        self.parent_id = parent_id
        self.state = False
        self.pin = 0

class Lamp(Room):
    def __init__(self, name:str, parent_id:int):
        self.id = id(self)
        self.name = name
        self.parent_id = parent_id
        self.state = False
        self.pin = 0
        
class Tempsensor(Room):
    def __init__(self, name:str, parent_id:int):
        self.id = id(self)
        self.name = name
        self.parent_id = parent_id
        self.address = " "

""" Testing
myHouse1 = house(0, "Házam", 0)

print(myHouse1.name)

print(myHouse1.id())"""