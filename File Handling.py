import os
from os import*
"""
## only read file
file=open('C:/Users/1/Desktop/TEST.txt','r')
line=file.readlines()
q=0
for i in range(4):
    print(line[q])
    q+=1
"""


"""
## read specific number of lines
file=open('C:/Users/1/Desktop/TEST.txt','r')
line=file.readlines()
q=0
while q!=4:
    print(line[q])
    q+=1
"""


"""
## overwright  text to the file
file=open('C:/Users/1/Desktop/TEST.txt','w')
file.write("sheeeeeeeeeesh")
file.close()
file=open('C:/Users/1/Desktop/TEST.txt','r')
print(file.read())
"""


"""
## add text to the file
file=open('C:/Users/1/Desktop/TEST.txt','a')
file.write("shawarma\n")
file.close()
file=open('C:/Users/1/Desktop/TEST.txt','r')
print(file.read())
"""


# file=open('C:/Users/1/Desktop/TEST1.txt','x')  ## creat a new file


# file=replace('C:/Users/1/Desktop/TEST.txt','C:/Users/1/Desktop/TEST F/TEST.txt')  ## moves to folder


# file=rename('C:/Users/1/Desktop/TEST.txt','C:/Users/1/Desktop/TEST2.txt')  ## rename file
