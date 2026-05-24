from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import pickle


with open('brean.pkl','rb') as br:
    cpu=pickle.load(br)



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0),color="white",x=5,y=1)
l_paddle = Paddle((-350, 0),color="white",x=5,y=1)





ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



def brean_cpu(paddle_r,y):
    paddle_r.goto(350,y)






game_is_on = True
while game_is_on:
    time.sleep(0.01) 
    screen.update()
    ball.move()

    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball_x=ball.xcor()
        ball_y=ball.ycor()

        cpue=cpu.predict([[ball_x,ball_y]])[0]

        brean_cpu(r_paddle,cpue)
        

        
        

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
        
        

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

