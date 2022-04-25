from guizero import *
from screens.mainScreen import *

from screens.splashScreen import *

from models.parkingSpace import ParkingSpace
from models.tailGate import TailGate

from utils.constants import *
from utils.helper import *

totalParkingSpaces = 3
totalTailGates = 1
parkingSpaces = list()
tailGate = TailGate(0, "close")
app = App(title=appTitle, bg=appBackgroundColor)
# app.set_full_screen()
window = Window(app, title="Splash Screen",bg=appBackgroundColor)
# window.tk.attributes("-fullscreen",True)


def initializeComponents():
    #Parking Space initialization
    for iteration in range(0, totalParkingSpaces):
        parkingSpaces.append(ParkingSpace(iteration, "available"))
        print("Parking Space id: " +
              str(parkingSpaces[iteration].id) + ", Status: " + parkingSpaces[iteration].status)

def appFuncationality():
    splashScreen(window)
    mainScreen(app,parkingSpaces,tailGate)
    app.display()  

def main():
    initializeComponents()
    appFuncationality()
    

if __name__ == "__main__":
    main()