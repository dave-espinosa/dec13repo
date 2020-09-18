import turtle
from math import sqrt
from random import randrange

def colorgen ():
    color_matrix = ["red", "green", 'blue', "yellow", "orange", "violet"]
    color_choosen = color_matrix[randrange(0, len(color_matrix))]
    return (color_choosen)

wn = turtle.Screen()
dave = turtle.Turtle()
dave.pensize(4)



#a = int(input("Insert Hexagon Side Dimension:"))
a =60
for _ in range(6):
    dave.color(colorgen())
    dave.forward(a)
    dave.right(60)

dave.right(30)
b = a*sqrt(3)

dave.color(colorgen())
dave.forward(b)
dave.right(120)
dave.color(colorgen())
dave.forward(b)
dave.right(120)
dave.color(colorgen())
dave.forward(b)
dave.up()

dave.right(90)
dave.color(colorgen())
dave.forward(a)
dave.right(90)
dave.down()

dave.color(colorgen())
dave.forward(b)
dave.right(120)
dave.color(colorgen())
dave.forward(b)
dave.right(120)
dave.color(colorgen())
dave.forward(b)