class TailGate:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def changeParkingStatus(self):
        if(self.status == "open"):
            self.status = "close"
        else:
            self.status = "open"
        print("Status of the tail gate with the id " + str(self.id) + " has been changed to " + self.status)