while True:
    q=input("enter an operation:")
    print("")
    operations=["plus","addition","minus","subtraction","division","times","multiplication","floor division","modulus","power"]
    if q not in operations:
        print("Invalid operation.")
    else:
        break

while True:
    w=int(input("enter the first number:"))
    print("")
    e=int(input("enter the second number:"))
    print('')
    if "plus" in q or "addition" in q:
        print(w+e)
        print('')
        q = input("enter an operation:")

    elif "minus" in q or "subtraction" in q:
        print(w-e)
        print('')
        q = input("enter an operation:")

    elif "times" in q or "multipliction" in q:
        print(w*e)
        print('')
        q = input("enter an operation:")

    elif "division" in q:
        print(float(w/e))
        print('')
        q = input("enter an operation:")

    elif "floor division" in q:
        print(float(w//e))
        print('')
        q = input("enter an operation:")

    elif "power" in q:
        print(w**e)
        print('')
        q = input("enter an operation:")

    elif "modulus" in q:
        print(float(w%e))
        print('')
        q = input("enter an operation:")