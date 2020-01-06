import turtle

ttl = turtle.Turtle()



def drawlines(x, y, length, reps):
    if reps > 1:
        ttl.penup()
        ttl.goto(x, y)
        ttl.pendown()
        ttl.goto(x+length, y)
        ttl.penup()

        drawlines(x, y-5, length/3, reps - 1)
        drawlines(x+((length*2)/3), y-5, length/3, reps - 1)





x = 0
y = 50
length = 500
reps = 10

ttl.pensize(3)
drawlines(x,y,length, reps)




turtle.getscreen()._root.mainloop()