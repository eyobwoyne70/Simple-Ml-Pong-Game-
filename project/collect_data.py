from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0),color="white",x=3,y=1)
l_paddle = Paddle((-350, 0),color="white",x=5,y=1)

border_line=Paddle((30, 0),color="red",x=50,y=0.1)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.01)  
    screen.update()
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ballxandy=ball.pos() 
        with open('train.csv','a')as data:
            data.write(f'{ballxandy[0]},{ballxandy[1]},')
            

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        wll=r_paddle.pos()
        with open('train.csv','a')as data:
            data.write(f'{wll[1]} \n')
        ball.reset_position()
        

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.reset_position()
        
        

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


    

screen.exitonclick()

