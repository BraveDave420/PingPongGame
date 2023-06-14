import turtle
from tkinter import *
import functools
import os
import time

wn = turtle.Screen()
wn.title("Pong by DavidHoelewyn")
wn.bgcolor("blue")
wn.setup(width = 800, height = 600)
wn.tracer(0)

paused = False
gameSpeed = 1.5
game_Started = False
EndGame = False

def startGame(x, y):
    global game_Started
    game_Started = True
    print("game started!")

def restart():
    global game_Started
    game_Started = False
    print("game restarted")

def endGame(x, y):
    global EndGame
    EndGame = True
    print("game ended!")

def speedCalc(paddle_obj, ball_obj):
    if ball_obj.ycor() <= paddle_obj.ycor() + 20 and ball_obj.ycor() >= paddle_obj.ycor() - 20:
        ball_obj.dx *= -1
        ball_obj.dy *= 1
        os.system("aplay bounce.wav&")

    if ball_obj.ycor() > paddle_obj.ycor() + 20 and ball_obj.ycor() <= paddle_obj.ycor() + 40:
        ball_obj.dx *= -1
        ball_obj.dy += 0.03125
        os.system("aplay bounce.wav&")

    if ball_obj.ycor() > paddle_obj.ycor() + 40 and ball_obj.ycor() <= paddle_obj.ycor() + 50:
        ball_obj.dx *= -1
        ball_obj.dy += 0.0625
        os.system("aplay bounce.wav&")

    if ball_obj.ycor() < paddle_obj.ycor() - 20 and ball_obj.ycor() >= paddle_obj.ycor() - 40:
        ball_obj.dx *= -1
        ball_obj.dy -= 0.03125
        os.system("aplay bounce.wav&")

    if ball_obj.ycor() < paddle_obj.ycor() - 40 and ball_obj.ycor() >= paddle_obj.ycor() - 50:
        ball_obj.dx *= -1
        ball_obj.dy -= 0.0625
        os.system("aplay bounce.wav&")
    return

def pause(pen_obj):
    global paused
    paused = not paused
    pen_obj.goto(0,0)
    pen_obj.write("Paused", align="center", font = ("Courier", 48, "normal"))
    wn.update()
    if paused != True:
        pen_obj.clear()
        pen_obj.goto(0, 260)
        pen_obj.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))
        wn.update()
      # Start watching for global to be changed.
      
def paddle_a_up(paddle_obj):
    if paused == False:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down(paddle_obj):
    if paused == False:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up(paddle_obj):
    if paused == False:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down(paddle_obj):
    if paused == False:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

def debugger(ball_obj):
    ball_obj.sety(0)
    ball_obj.setx(0)
    ball_obj.dy = 0
        
def grabStartMenu(pen_obj):
    pen_obj.clear()
    pen_obj.goto(0, 0)
    pen_obj.write("Pong\nBy David Hoelewyn", align="center", font = ("Courier", 48, "normal"))


##################################################################################################################
#This loop begins the newgame cycle for as many times as the player wishes to run the game
#After the player clicks the Quit button, the loop will break and the window should close
##################################################################################################################


Pen_is = False
MenuStart_is = False
ExitBtn_is = False

while EndGame == False:
    wn.bgcolor("blue")
    ##################################################################################################################
    #This code initializes the start menu functionality
    #The pen is intended to be used inside the main game loop as well for writing text
    ##################################################################################################################
    wn.update()
    if Pen_is != True:
        print("writing title")
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        #pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))
        pen.goto(0, 0)
        pen.write("Pong By David Hoelewyn", align="center", font = ("Courier", 36, "normal"))
        Pen_is = True
    
    if MenuStart_is != True:
        print("creating start button")
        MenuStart = turtle.Turtle()
        MenuStart.speed(0)
        MenuStart.shape("square")
        MenuStart.color("white")
        MenuStart.shapesize(stretch_wid = 1,stretch_len = 5)
        MenuStart.penup()
        MenuStart.goto(-100, -50)
        MenuStart.write("Start", align="center", font = ("Courier", 24, "normal"))
        
        MenuStart_is = True

    if ExitBtn_is != True:
        print("creating exit button")
        ExitBtn = turtle.Turtle()
        ExitBtn.speed(0)
        ExitBtn.shape("square")
        ExitBtn.color("white")
        ExitBtn.shapesize(stretch_wid = 1,stretch_len = 5)
        ExitBtn.penup()
        ExitBtn.goto(100, -50)
        ExitBtn.write("Quit", align="center", font = ("Courier", 24, "normal"))
        
        ExitBtn_is = True
        
    MenuStart.onclick(startGame)
    ExitBtn.onclick(endGame)

    #Check to see if the player ended the game session
    if EndGame == True:
        print("Game session ended")
        break

    
    if game_Started == True:
        print("Creating Game Screen")
        #If the loop reaches this point, it's time to erase the start menu and draw the game screen
        wn.clear()
        wn.title("Pong by DavidHoelewyn")
        wn.bgcolor("blue")
        wn.tracer(0)
        
        #Score
        score_a = 0
        score_b = 0
        

        # Paddle A
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("white")
        paddle_a.shapesize(stretch_wid = 5,stretch_len = 1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # Paddle B
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("white")
        paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # Ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 0.0625
        ball.dy = 0.0625

        # Pen
        pen.clear()
        pen.penup()
        pen.goto(0, 260)
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))

        #Function
        # Keyboard binding
        wn.listen()
        wn.onkeypress(functools.partial(paddle_a_up, paddle_a), "w")
        wn.onkeypress(functools.partial(paddle_a_down, paddle_a), "s")
        wn.onkeypress(functools.partial(paddle_b_up, paddle_b), "Up")
        wn.onkeypress(functools.partial(paddle_b_down, paddle_b), "Down")
        wn.onkeypress(functools.partial(pause, pen), "space")
        wn.onkeypress(functools.partial(debugger, ball), "p")

        #main game loop
        while True:
            wn.update()
            
            #Move the ball
            if paused != True:
                ball.setx(ball.xcor() + ball.dx*gameSpeed)
                ball.sety(ball.ycor() + ball.dy*gameSpeed)
            if score_a == 10 or score_b == 10:
                restart()
                wn.clear()
                break
        

            #Border checking
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
                os.system("aplay bounce.wav&")

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
                os.system("aplay bounce.wav&")

            if ball.xcor() > 390:
                score_a += 1
                ball.goto(0, 0)
                ball.dx *= -1
                os.system("aplay scoresound.wav&")
                if (score_a + score_b) % 10 == 0 and (score_a + score_b) < 30:
                    gameSpeed *= 1.5
                pen.clear()
                pen.goto(0, 260)
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))

            if ball.xcor() < -390:
                score_b += 1
                ball.goto(0, 0)
                ball.dx *= -1
                os.system("aplay scoresound.wav&")
                if (score_a + score_b) % 10 == 0 and (score_a + score_b) < 30:
                    gameSpeed *= 1.5
                pen.clear()
                pen.goto(0, 260)
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))

    #Debugger Functions
    #List of Checkers


    #If ball hits the middle of the paddle, maintain vertical speed

            if round(ball.xcor()) == paddle_a.xcor():
                speedCalc(paddle_a, ball)

            if round(ball.xcor()) == paddle_b.xcor():
                speedCalc(paddle_b, ball)
        wn.bgcolor("blue")
        pen.goto(0,0)
        if score_a > score_b:
            pen.write("Player A Wins!", align="center", font = ("Courier", 48, "normal"))
        else:
            pen.write("Player B Wins!", align="center", font = ("Courier", 48, "normal"))
            
        os.system("aplay Winner.wav&")
        time.sleep(5)
        wn.clear()
        print(game_Started)
        gameSpeed = 1.5
        Pen_is = False
        MenuStart_is = False
        ExitBtn_is = False
        wn.bgcolor("blue")

turtle.bye()
