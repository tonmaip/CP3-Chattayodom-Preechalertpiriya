class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirCon(self):
        print("Turn On : Air")

class Car (Vehicle):
    pass

class PickUp (Vehicle):
    pass

class Van (Vehicle):
    pass

class Estatecar (Vehicle):
    pass

car1 = Car()
car1.turnOnAirCon()

pickup1 = PickUp()
pickup1.turnOnAirCon()

van1 = Van()
van1.turnOnAirCon()

estatecar1 = Estatecar()
estatecar1.turnOnAirCon()

