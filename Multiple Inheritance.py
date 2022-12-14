class father:
    def __init__(self,eyes,color):
        self.eyes=eyes
        self.color=color

class mother(father):
    def __init__(self,hair,eyes,color):
        self.hair=hair
        super().__init__(eyes,color)

class child(mother):
    def __int__(self,eyes,color,hair):
        super().__init__(eyes,color,hair)
    def get_info(self):
        print("I have",self.eyes,"eyes.")
        print("I am",self.color + ".")
        print("i have",self.hair,"hair.")

q=input("Enter the child`s name:")
a=0
while a==0:
    w=input("enter the father`s eye color:")
    e=input("Enter the father`s color:")
    r=input("Enter the mother`s hair color:")
    colors=[ "White","Yellow","Blue","Red","Green","Black","Brown","Azure","Ivory","Teal","Silver","Purple","Navy blue","Pea green","Gray","Orange","Maroon","Charcoal","Aquamarine","Coral","Fuchsia","Wheat","Lime","Crimson","Khaki","Hot pink","Magenta","Olden","Plum","Olive","Cyan"]
    skin=["White","Black"]
    if w in colors and r in colors and e in skin:
        a = child(r, w, e)
        print("My name is",q + ".")
        print(a.get_info())
        exit()
    else:
        print("The first letter of the color must be capital.")