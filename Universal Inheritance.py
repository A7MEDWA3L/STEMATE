class human :
    def __init__(self ,height , weight , job = False ) :
        self.height = height
        self.weight = weight
        self.job = job

    def eat(self):
        self.weight += 1
    def play_sport(self):
        self.height+=1
    def check_for_job(self):
        if self.job != False :
            print("I have a job !!")
        else :
            print("I don't have a job!!")
    def get_info(self):
        print("I am",self.height,"CM")
        print("I am",self.weight,"KG")
        print("I work as a",self.job )


class gangaster(human):
    def __init__(self,height,weight,weapon,money,yo_exp):
        self.weapon=weapon
        self.money=money
        self.yo_exp=yo_exp
        self.height=height
        self.weight=weight
    def job_info(self):
        print("I am",self.height,"CM")
        print("I am",self.weight,"KG")
        print("my weapon is",self.weapon)
        print("I have",self.money,"$")
        print("I have",self.yo_exp,"years  of experience")

#ahmed=(human(188,12,"hacker"))
#print(ahmed.get_info())

ahmed=gangaster(200,77,"AK47",9999,99)
print(ahmed.job_info())