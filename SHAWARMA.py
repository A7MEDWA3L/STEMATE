"""
this code has a class and two other classes that inherit from it a function
"""
class soory_man:
    def __init__(self,food):
        self.food=food
    def taste(self):
        print("GIGA CHAD")

class shawarma(soory_man):
    def __init__(self,tomiya):
        self.tomiya=tomiya
    def taste(self):
        print("very noice")

class batates(soory_man):
    def __init__(self,tatbila):
        self.tatbila=tatbila
    def taste(self):
        print("wawi")

e=soory_man("NOICE")
q=shawarma("very good")
w=batates("noice")

print(q.taste())
print("")
print(w.taste())
print("")
print(e.taste())