import turtle

#code that creates two buttons that detect a user click and performs a unique function


def startGame(x, y):
    print("game started!")

def endGame(x, y):
    print("game ended!")

Screen = turtle.Screen()
Screen.title("Simple Fucking Button")
Screen.bgcolor("black")
Screen.setup(width = 800, height = 600)
Screen.tracer(0)

start = turtle.Turtle()
start.speed(0)
start.shape("square")
start.color("white")
start.shapesize(stretch_wid = 1, stretch_len = 5)
start.penup()
start.goto(-200, 0)
start.write("Start", align = "center",font = ("Courier", 24, "normal"))
start.onclick(startGame)

Quit = turtle.Turtle()
Quit.speed(0)
Quit.shape("square")
Quit.color("white")
Quit.shapesize(stretch_wid = 1, stretch_len = 5)
Quit.penup()
Quit.goto(200, 0)
Quit.write("Quit", align = "center",font = ("Courier", 24, "normal"))
Quit.onclick(endGame)

##pen = turtle.Turtle()
##pen.color("blue")
##pen.penup()
##pen.hideturtle()
##pen.goto(-200, -25)
##pen.write("Button", align="center", font = ("Courier", 24, "normal"))

Screen.update()
