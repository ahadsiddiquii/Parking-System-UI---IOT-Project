from guizero import *

from utils.constants import *
from utils.helper import *

def mainScreen(app,parkingSpaces,tailGate):
    headerContainer(app,parkingSpaces)
    footerContainer(app,parkingSpaces,tailGate)
    midContainerRightPanel(app,parkingSpaces)
    midContainerLeftPanel(app,parkingSpaces)
    
def headerContainer(app,parkingSpaces):
    titleBox = Box(app, width="fill", align="top", layout="grid")
    Text(titleBox, text=spacer, align="left", size=bodyTextSize,
         color=textThemePrimaryColor, grid=[0, 0])
    Text(titleBox, text=mainTitleHeading, align="left",
         size=headingSize, color=textThemePrimaryColor, grid=[1, 1])
    Text(titleBox, text=mainTitleDescription, align="left",
         size=subHeadingSize, color=textThemeSecondaryColor, grid=[1, 2])
    Text(titleBox, text=spacer, align="left",
             size=bodyTextSize, color=textThemePrimaryColor,grid=[0, 3])

def midContainerLeftPanel(app,parkingSpaces):
    
    contentBox = Box(app, align="top", width="fill",layout="grid")
    
    parkingPanelIdBoxes = list()
    parkingPanels = list()
    parkingIcons = list()
    
    
    for iteration in range(0,len(parkingSpaces)):
        positionIndex = iteration + 1 + (iteration * 1)
        Text(contentBox, text=spacer, align="left",
             size=bodyTextSize, color=textThemePrimaryColor,grid=[0,0])
        parkingPanelIdBoxes.append(Text(contentBox, text="Parking ID: "+str(parkingSpaces[iteration].id),
                                 align="top", size=subHeadingSize, color=textThemePrimaryColor,grid=[positionIndex,0]))
        Text(contentBox, text=spacer, align="left",
             size=bodyTextSize, color=textThemePrimaryColor,grid=[1,1])
        parkingPanels.append(Drawing(contentBox, width=80, height=120, align="left",grid=[positionIndex,2]))
        parkingPanels[iteration].bg = getParkingColor(parkingSpaces,iteration)
        parkingIcons.append(Picture(contentBox, image="images/parkingPanelIcon.png",width=60,height=45,grid=[positionIndex,2]))
        parkingIcons[iteration].bg = getParkingColor(parkingSpaces,iteration)
        Text(contentBox, text=spacer, align="left",
             size=bodyTextSize, color=textThemePrimaryColor,grid=[positionIndex + 1,0])
    # button = PushButton(app, command=updateParking,args = [parkingPanelIdBoxes,parkingPanels,parkingIcons,1,parkingSpaces])
    
    # Text(contentBox, text=spacer, align="left",
    #          size=bodyTextSize, color=textThemePrimaryColor,grid=[0,0])
    # parkingPanel1IdBox = Text(contentBox, text="Parking ID: "+str(parkingSpaces[0].id),
    #                              align="top", size=subHeadingSize, color=textThemePrimaryColor,grid=[1,0])
    # Text(contentBox, text=spacer, align="left",
    #          size=bodyTextSize, color=textThemePrimaryColor,grid=[1,1])
    # parkingPanel1 = Drawing(contentBox, width=80, height=120, align="left",grid=[1,2])
    # parkingPanel1.bg = "red"
    # picture = Picture(contentBox, image="images/parkingPanelIcon.png",width=60,height=45,grid=[1,2])
    # picture.bg = "red"
    
    # Text(contentBox, text=spacer, align="left",
    #          size=bodyTextSize, color=textThemePrimaryColor,grid=[2,0])



def updateParking(parkingPanelIdBoxes,parkingPanels,parkingIcons,parkingId,parkingSpaces):
    parkingSpaces[parkingId].changeParkingStatus()
    print(parkingSpaces[parkingId].status)
    if(parkingId<len(parkingSpaces)):
        print("parkingUpdated")
        if(parkingSpaces[parkingId].status == "available"):
            parkingPanels[parkingId].bg = parkingAvailableColor
            parkingIcons[parkingId].bg = parkingAvailableColor
        else:
            parkingPanels[parkingId].bg = parkingUnavailableColor
            parkingIcons[parkingId].bg = parkingUnavailableColor
    else:
        print("Range error")
    
    
    
    
    

def midContainerRightPanel(app,parkingSpaces):
    detailsBox = Box(app, height="fill", align="right")
    Text(detailsBox, text=spacer, align="right",
             size=bodyTextSize, color=textThemePrimaryColor)
    Text(detailsBox, text=spacer, align="right",
             size=bodyTextSize, color=textThemePrimaryColor)
    picture = ""
    if(availableSpaces(parkingSpaces)>0):
        picture = "images/emptySlot.gif"
    else:
        picture = "images/noSpaceLeft.gif"
    Picture(detailsBox, image=picture,width=180,height=170)
    Text(detailsBox, text=spacer,
             size=bodyTextSize, color=textThemePrimaryColor)
    Text(detailsBox, text="Available Spaces",size=largeHeading)
    Text(detailsBox, text=availableSpaces(parkingSpaces),size=jumboText)
    
    


def footerContainer(app,parkingSpaces,tailGate):

    bottomBox = Box(app, width="fill", align="bottom", layout="auto")
    tailGateStatusBox = Text(bottomBox, text=gateClosedText,
                                 align="top", size=subHeadingSize, color=textThemePrimaryColor)
    
    Text(bottomBox, text=spacer, align="left",
             size=bodyTextSize, color=textThemePrimaryColor)

    leftWall = Drawing(bottomBox, width=20, height=60, align="left")
    gate = Drawing(bottomBox, width="fill", height=60, align="left")
    rightWall = Drawing(bottomBox, width=20, height=60, align="left")
    leftWall.bg = gateColor
    rightWall.bg = gateColor

    gate.bg = gateColor
   
    Text(bottomBox, text=spacer, align="left",size = bodyTextSize,color=textThemePrimaryColor)
    # button = PushButton(app, command=updateFooterText,args = [tailGateStatusBox,gate,tailGate,parkingSpaces])

def updateFooterText(tailGateStatusBox,gate,tailGate,parkingSpaces):
    spacesLeft = availableSpaces(parkingSpaces)
    if(spacesLeft > 0):
        tailGate.changeParkingStatus()
        if(tailGate.status == "open"):
            gate.bg = "white"
        else:
            gate.bg = gateColor
    tailGateStatusBox.value = getTailGateStatus(tailGate,parkingSpaces)

    
