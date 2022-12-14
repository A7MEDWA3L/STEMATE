class dogs:
    def __init__(self,size,lifetime,hair,ferocity,weight):
        self.size=size
        self.lifetime=lifetime
        self.hair=hair
        self.ferocity=ferocity
        self.weight=weight
    def eat(self):
        self.eat +=1

class shiwawa(dogs):
    def bark(self):
        print("woof")

class germen(dogs):
    def bark(self):
        print("wooof wooof")

dog = dogs("normal",12,"medium","stupid",25)
print(dog.lifetime)
stupid_dog = shiwawa("tiny",12,"long","stupid",1234)
print(stupid_dog.size)
d = germen("big",1999,"midium","stupid",999)
print(d.ferocity)
