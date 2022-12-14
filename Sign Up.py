q = input("enter your username:")
len(q)
if len(q) < 5 or " " in q:
    print("username must be more then 5 characters and must not contain spaces")
    exit()
w = input("enter your password:")
len(w)
if len(w) < 8 or " " in w or "12345678" in w:
    print("the password must be more than 8 characters and must not be weak or contain spaces")
    exit()
e=input("confirm password:")
if e==w:
    print(q.lower())
    print(w)
    print("username and password are accepted")
else:
    print("the confirmation must be the same as password")