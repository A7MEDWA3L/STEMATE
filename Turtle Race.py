import turtle
import random
import time
from time import *
from turtle import *
from random import *
from time import *
turtle_1 = Turtle()
turtle_1.getscreen()
turtle_2 = Turtle()
turtle_2.getscreen()
turtle_1.shape("turtle")
turtle_2.shape("turtle")
height = turtle.window_height()
turtle_1.penup()
turtle_2.penup()

speed1 = randint(1,4)
turtle_1.goto((height/2),90) #target
turtle_1.dot(50)
turtle_1.goto(-(height/2),90) # start point


speed2= randint(1,4)
turtle_2.goto((height/2),-90) #target
turtle_2.dot(50)
turtle_2.goto(-(height/2), -90) #start poijnt

time1 = time()
turtle_2.speed(speed2)
turtle_2.goto((height/2),-90) #target
time2 =time()
total_time1 = time2 - time1

time3 = time()
turtle_1.speed(speed1)
turtle_1.goto((height/2),90) #target
time4 = time()
total_time2 = time4- time3

if total_time1 > total_time2 :
    print("TURTLE 1 WON !!! ")
else :
    print("TURTULE 2 WON !!! ")

sleep(5)