from house import *
from UI_elements import *
import random as rnd

city = City()
app = MainWindow()

# Generates data for tests
city.generate_data()

app.mainloop()

"""# Print every item
for property in city.properties:
    print("\n"+property.name+"\t------------")
    for room in property.rooms:
        print("\n"+room.name, room.isGarage)
        for item in room.windows:
            print(item.name)
        for item in room.lamps:
            print(item.name)
        for item in room.temp_sensors:
            print(item.name)"""
