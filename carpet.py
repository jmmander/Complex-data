import turtle

COLOR_MAP = ['blue', 'red', 'green', 'cyan', 'yellow', 'violet', 'orange']

def drawRectangle(coord, colour, myTurtle):
    myTurtle.fillcolor(colour)
    myTurtle.begin_fill()
    for point in coord:
        myTurtle.goto(point)

    myTurtle.goto(coord[0])
    myTurtle.end_fill()

def sierpinski(coord, degree, myTurtle):

    drawRectangle(coord, colours[degree], myTurtle)

    if degree > 0:
        origin = coord[0] * (2 / 3)  # vectors multiply by a scalar, but not divide

        coord = [point * (1 / 3) for point in coord]  # new rectangle is 1/3 size of old rectangle

        width, height = coord[2] - coord[0]  # vector subtraction

        for y in range(3):
            for x in range(3):
                if x == 1 == y:
                    continue  # leave hole in the center

                offset = origin + turtle.Vec2D(width * x, height * y)

                sierpinski([offset + point for point in coord], degree - 1, myTurtle)


coord = [turtle.Vec2D(0, 0), turtle.Vec2D(0, 300), turtle.Vec2D(300, 300), turtle.Vec2D(300, 0)]









colours = [(255, 204, 255), (204, 204, 255), (204, 255, 255), (204, 255, 204), (255, 255, 204), (230, 241, 255)]


myTurtle = turtle.Turtle()
myTurtle.shape('turtle')
screen = turtle.Screen()
screen.colormode(255)
myTurtle.penup()
sierpinski(coord, 4, myTurtle)






