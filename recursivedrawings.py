import turtle


def draw_triangle(coord, colour, myturtle):
    myturtle.fillcolor(colour)
    myturtle.up()
    myturtle.goto(coord[0][0],coord[0][1])
    myturtle.down()
    myturtle.begin_fill()
    myturtle.goto(coord[1][0],coord[1][1])
    myturtle.goto(coord[2][0], coord[2][1])
    myturtle.goto(coord[0][0], coord[0][1])
    myturtle.end_fill()

def getmid(c1,c2):
    return ((c1[0] + c2[0]) / 2, (c1[1] + c2[1]) / 2)

def drawsierpinski(coord, degree, myturtle):
    colours = [(255,204,255),(204,204,255),(204,255,255),(204,255,204),(255,255,204), (230,241,255)]
    draw_triangle(coord, colours[degree], myturtle)
    if degree > 0:
        drawsierpinski([coord[0], getmid(coord[0], coord[1]),
                    getmid(coord[0], coord[2])],
                   degree-1, myturtle)
        drawsierpinski([coord[1],
                    getmid(coord[0], coord[1]),
                    getmid(coord[1], coord[2])],
                   degree - 1, myturtle)
        drawsierpinski([coord[2],
                    getmid(coord[2], coord[1]),
                    getmid(coord[0], coord[2])],
                   degree - 1, myturtle)



myturtle = turtle.Turtle()
myturtle.shape('turtle')
screen = turtle.Screen()
screen.colormode(255)
coord = [[-200, -100], [0, 200], [200, -100]]
degree = 5

drawsierpinski(coord, degree, myturtle)
screen.exitonclick()





