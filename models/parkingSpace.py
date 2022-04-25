class ParkingSpace:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def changeParkingStatus(self):
        if(self.status == "available"):
            self.status = "unavailable"
        else:
            self.status = "available"
        print("Status of the space with the id " + str(self.id) + " has been changed to " + self.status)