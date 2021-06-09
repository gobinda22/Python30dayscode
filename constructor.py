class Vehicle:
    def __init__(self,milage,cost):
        self.milage = milage
        self.cost =cost


    def show_details(self):
        print("its milage",self.milage)
        print("its cost",self.milage)

v1=Vehicle(500,500)
v1.show_details()

class car(Vehicle):
    def show_car(self):
        print("Gobicar")
c1=car(2000,4000000) #inherinting the super class(Vehical)
c1.show_details()
c1.show_car()

class car(Vehicle):#overriding the init class
    def __init__(self,milage,cost,hp,tr):
        super().__init__(milage,cost)
        self.hp=hp
        self.tr=tr

    def show_car_details(self):
        print("its host power",self.hp)
        print("its tier",self.tr)


c2=car(300,800000,999,4)
c2.show_details()#its overriding the parent class
c2.show_car_details()#its overriding the child class
