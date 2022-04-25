from guizero import *

def splashScreen(window):
    window.set_full_screen()
    splashBox = Box(window, width="fill",align="left")
    picture = Picture(splashBox, image="images/parkingSplashScreen.gif",width=300,height=300)
    picture.after(time=3000,function=hideSplashScreen, args=[window])        
    
def hideSplashScreen(window):
    window.hide()
    

