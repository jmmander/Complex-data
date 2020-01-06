import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        if branchLen <15:
            t.color("red")
        elif branchLen < 25:
            t.color("orange")
        elif branchLen < 35:
            t.color("yellow")
        elif branchLen < 45:
            t.color("pink")
        elif branchLen < 55:
            t.color("purple")
        elif branchLen < 65:
            t.color("blue")
        angle = random.randint(15, 35)
        red = random.randint(8,12)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-red, t)
        t.left(angle*2)
        tree(branchLen-red, t)
        t.right(angle)
        if branchLen > 65:
            t.color("green")
        elif branchLen > 55:
            t.color("blue")
        elif branchLen > 45:
            t.color("purple")
        elif branchLen > 35:
            t.color("pink")
        elif branchLen > 25:
            t.color("yellow")
        elif branchLen >15:
            t.color("orange")
        t.backward(branchLen)



t = turtle.Turtle()
screen = turtle.Screen()

t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
tree(75,t)

screen.exitonclick()