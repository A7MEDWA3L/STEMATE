class pc_build:
    def __init__(self,prossecor,RAM,power_supply):
        self.prossecor=prossecor
        self.RAM=RAM
        self.powersupply=power_supply
    def getinfo(self):
        print("your prossecor is:",self.prossecor)
        print("your RAM is:",self.RAM)
        print("your power supply is:",self.powersupply)
    def setinfo(self,q,w,e):
        self.RAM=q
        self.prossecor=w
        self.powersupply=e

my_pc = pc_build("intel i9",32,"1000W")
my_pc.setinfo(999,"intel i100","5000000W")
print(my_pc.getinfo())