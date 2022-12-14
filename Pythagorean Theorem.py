import math
from math import *

while True:
    q=float(input("Enter the first side of the triangle: "))
    w=float(input("Enter the second side of the triangle: "))

    a=q**2
    s=w**2

    print("The hypotenuse is equal:",sqrt(a+s))
    print("")