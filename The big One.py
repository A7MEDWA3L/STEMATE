q = input("enter your username:")
len(q)
if len(q) < 5 or " " in q:
    print("username must be more then 5 characters and must not contain spaces")
    exit()
w = input("enter your password:")
len(w)
if len(w) < 8:
    print("the password must be more than 8 characters ")
    exit()
if "12345678" in w or " " in w:
    print("your password must not be weak or contain spaces")
    exit()
e=input("confirm password:")
if e==w:
    print("username and password are accepted")
else:
    print("the confirmation must be the same as password")
    print("you have logged in successfully.")
print("PC avilable: super pc - midd pc - potato pc - AMD pc - trash pc")
super_pc={
    "Processor" : "intel i9 10 GEN",
    "Ram" : "23 GB DDR5",
    "Graphic card" : "RTX 40 90",
    "Price" : "500,000"
}
midd_pc={
    "Processor" : "intel i5 7 GEN",
    "Ram" : "8 GB DDR3",
    "Graphic card" : "RTX 40 60",
    "Price" : "5,000"
}
potato_pc={
    "Processor" : "intel patiume 4",
    "Ram" : "2 GB DDR1",
    "Graphic card" : "not avilable",
    "Price" : "200"
}
idiot_pc={
    "Processor" : "AMD ryzen 7000",
    "Ram" : "16 GB DDR3",
    "Graphic card" : "RX 6000",
    "Price" : "for free"
}

trash_pc={
    "Processor" : "intel pantium 1",
    "Ram" : "1 GB DDR0",
    "Graphic card" : "not avilable",
    "Price" : "100"
}
r=input("Enter the PC build you want:")
if "super pc" in r:
    print(super_pc)
    exit()
if "midd pc" in r:
    print(midd_pc)
    exit()
if "potato pc" in r:
    print(potato_pc)
    exit()
if "trash pc" in r:
    print(trash_pc)
    exit()
if "amd pc" in r:
    print(idiot_pc)
    print("i advice you not to buy this crapy piece of shit or you are idiot")
    exit()
else:
    print("this pc is not avalable or sold out")
t=input("do you want to buy this build")
if "yes" in t:
    y=input("enter your cridit card ")
if "no" in t:
    print("thanks for wasting my time")