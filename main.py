from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_turtle = Paddle(350)
l_turtle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(r_turtle.r_up,"Up")
screen.onkeypress(r_turtle.r_down,"Down")
screen.onkeypress(l_turtle.l_up,"w")
screen.onkeypress(l_turtle.l_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #detect collision with wall
    if ball.ycor() >280 or ball.ycor() < -280 :
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_turtle) < 50 and ball.xcor() > 320 or ball.distance(l_turtle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if right paddle misses ball
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    #detect if left paddle misses ball
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()