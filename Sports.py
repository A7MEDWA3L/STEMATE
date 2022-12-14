class sport_man:
    def __init__(self,name,age,weight,height,muscles,agility,endurance,stamina):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.muscles=muscles
        self.agility=agility
        self.endurance=endurance
        self.stamina = stamina
    def get_info(self):
        print("My name is",self.name)
        print("I am",self.age,"Years old")
        print("I am",self.weight,"KG")
        print("I am",self.height,"CM")
        print("My muscle level is",self.muscles)
        print("My agility level is",self.agility)
        print("My endurance level is", self.endurance)
        print("My stamina level is", self.stamina)

class body_builder(sport_man):
    def train(self):
        self.muscles+=5
        self.endurance+=3
        self.weight+=5
        self.stamina+=3

class lifter(sport_man):
    def lift(self):
        self.muscles+=3
        self.endurance+=5
        self.weight+=2
        self.height-=3
        self.stamina+=4
class fitness_man(sport_man):
    def strech(self):
        self.agility+=5
        self.height+=0.9

class cardio_man(sport_man):
    def cardio(self):
        self.stamina+=5
        self.endurance+=3

ahmed=body_builder("ahmed",22,100,200,9999,100,9999,9999)
ahmed.train()
ahmed.get_info()
print("")
aabas=lifter("aabas",40,123,123,124,50,500,300)
aabas.lift()
aabas.get_info()
print("")
mohamed=cardio_man("mohamed",20,70,170,100,400,600,9999)
mohamed.cardio()
mohamed.get_info()
print("")
mazen=fitness_man("mazen",30,60,200,50,999,300,200)
mazen.strech()
mazen.get_info()