from turtle import Screen, Turtle
from paddle import Paddle  # to import Paddle class from paddle.py
from ball import Ball    # to import Ball class from ball.py
from scoreboard import Scoreboard # to import class Scoreboard class from scoreboard.py
import time      # to import time module

screen = Screen()
screen.bgcolor("black")  # set screen color to black
screen.setup(width=800, height=600) # set screen dimensions
screen.title("Pong")   # set screen title to Pong
screen.tracer(0)     # to control animation of turtle

r_paddle = Paddle((350, 0))  # create right side paddle from Paddle class
l_paddle = Paddle((-350, 0)) # create left side paddle from Paddle class
ball = Ball()    # create an instance of Ball class
scoreboard = Scoreboard() # create instance of Scoreboard class

screen.listen()  # to make screen listen to keystrokes
screen.onkey(r_paddle.go_up, "Up") # bind function with 'Up' key
screen.onkey(r_paddle.go_down, "Down") # bind function with 'Down' key
screen.onkey(l_paddle.go_up, "w") # bind function with 'w' key
screen.onkey(l_paddle.go_down, "s") # bind function with 's' key

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
     # winner selection criteria and stop the game   
    if abs(scoreboard.l_score-scoreboard.r_score) >= 5:
            if scoreboard.l_score > scoreboard.r_score:
                scoreboard.winner_l()
                time.sleep(2)
                game_on = False
                screen.exitonclick()
            if scoreboard.r_score > scoreboard.l_score:
                scoreboard.winner_r()
                time.sleep(2)
                game_on = False
                screen.exitonclick()


