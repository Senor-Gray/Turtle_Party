#Turtle Party Project
#by Mr Gray
#Uploaded to git - Jan 16 2024

import turtle
turtle.color("red")

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

def move(len):
    back(-1*len)

def polygon(numsides, size):
    for i in range(numsides):
        turtle.forward(size)
        turtle.left(360/numsides)

def spiral(len, angle):
    for i in range(len, 5, -5):
        turtle.forward(i)
        turtle.right(angle)

spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)

move(150)
for n in range(3,10):
    move(50)
    polygon(n, 100/n)
    back(50)
    turtle.right(360/7)
