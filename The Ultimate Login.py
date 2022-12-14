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
acount=[q,e]
r=input("enter your username to login:")
t=input("enter your password to login:")
if r not in acount or t not in acount:
    print("this username or password are not correct")
    exit()
else:
    print("congratulations you have logged in successfully.")