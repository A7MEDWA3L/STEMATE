class human:
    def __init__(self,name,age,height,weight,IQ):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.IQ=IQ
    def learn(self):
        self.IQ+=1
    def get_info(self):
        print("My name is",self.name)
        print("I am",self.age,"years old")
        print("I am",self.height,"CM")
        print("I am",self.weight,"KG")
        print("My IQ is",self.IQ)

class teacher(human):
    def __init__(self,name,age,height,weight,IQ,quality,salary,subject,anger_issues=True):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.IQ=IQ
        self.quality=quality
        self.salary=salary
        self.subject=subject
        self.anger=anger_issues
    def learn(self):
        self.IQ+=2
    def teach(self):
        print("I teach",self.subject)
    def get_t_info(self):
        self.get_info()
        print("I take",self.salary,"$")
        print("I teach",self.subject)

class student(human):
    def __init__(self,name,age,height,weight,IQ,classe,grades):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.IQ=IQ
        self.classe=classe
        self.grades=grades
    def study(self):
        self.IQ+=3
    def get_s_info(self):
        self.get_info()
        print("I study",self.classe,"class")
        print("My are",self.grades)

ahmed=teacher("ahmed",20,200,70,99999,"legend",99999999999,"Programing",False)
ofis=student("youssef",12,100,30,100,4,"Very good")
dum_dum=human("jaafar",999,100,999,1)

ahmed.get_t_info()
print("")
ofis.get_s_info()
print("")
dum_dum.get_info()