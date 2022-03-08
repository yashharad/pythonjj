class Car(object):
    def __init__(self,model,color,compony,speed_limit):
        self.color=color
        self.compony=compony
        self.speed_limit=speed_limit
        self.model=model
hbmn 
    def start(self):
        print("car started")

    def stop(self):
        print("emergency brake applied car stopped")

    def acclerate(self):
        print("acclerating")

    def change_gear(self,Gear_type):
        print("gear changed to sports mode pedal shifting applied")
 