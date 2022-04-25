from utils.constants import *

def availableSpaces(parkingSpaces):
    count = 0
    for item in parkingSpaces:
        if(item.status == "available"):
            count+=1
    return count

def getTailGateStatus(tailGate,parkingSpaces):
    spacesLeft = availableSpaces(parkingSpaces)
    if(spacesLeft > 0):
        if(tailGate.status == "open"):
            return gateOpenText
        else:
            return gateClosedText
    else:
        return noSpaceAvailableText

def getParkingColor(parkingSpaces, parkingId):
    if(parkingSpaces[parkingId].status == "available"):
        return parkingAvailableColor
    else:
        return parkingUnavailableColor