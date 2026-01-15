# Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns disintegrate (Laser), crush (Claw), or ring (SmartPhone).
class Action:
    def __init__(self, act):
        self.act = act

class Laser(Action):
    def __init__(self, name, act):
        self.name = name
        super().__init__(act)

class Claw(Action):
    def __init__(self, name, act):
        self.name = name
        super().__init__(act)

class SmartPhone(Action):
    def __init__(self, name, act):
        self.name = name
        super().__init__(act)

laser = Laser("Laser", "Disintegrate")
print(laser.name, laser.act)
claw = Claw("Claw", "crush")
print(claw.name, claw.act)
smart_phone = SmartPhone("SmartPhone", "ring")
print(smart_phone.name, smart_phone.act)
