import time
import turtle
from turtle import*
from time import*
t1=Turtle()
t2=Turtle()
t3=Turtle()

t1.penup()

t2.penup()
t3.penup()

t1.shape("turtle")
t1.pencolor("red")
t1.goto(-(window_height()/2),100)

t2.shape("turtle")
t2.pencolor("blue")
t2.goto(-(window_height()/2),-100)

t3.shape("circle")
t3.goto((window_height()/2),-100)
t3.dot(50,"yellow")
t3.goto((window_height()/2),100)
t3.dot(50,"green")

t1.goto((window_height()/2),100)
t2.goto((window_height()/2),-100)
sleep(5)