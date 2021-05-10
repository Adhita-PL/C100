class Car(object) :
    def __init__(self, company, colour, model, speed_limit) :
        self.company = company
        self.colour = colour
        self.model = model
        self.speed_limit = speed_limit

    def start(self) :
        print("The car has started")

    def stop(self) :
        print("The car has stopped")

    def accelerate(self) :
        print("accelerating...")
    
    def change_gear(self, gear_type) :
        print("The gear has changed to ", gear_type, "gear")

audi = Car("audi", "red", "X101", 100) 

print(audi.start()) 
print(audi.accelerate())
print(audi.change_gear(3))
print(audi.stop()) 
print(audi.colour) 
