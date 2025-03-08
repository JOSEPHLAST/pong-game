import time
from turtle import Turtle, Screen
from paddle import Paddle
from score_board import Scoreboard
from ball import Ball

t = Turtle()
s = Screen()
s.setup(800, 500)
s.title("MY PONG GAME")
s.bgcolor("black")
s.tracer(0)
t.hideturtle()
t.penup()
t.goto(0, 240)
t.setheading(270)
t.pensize(7)
t.color("silver")
t.speed(0)

paddle = Paddle()
score = Scoreboard()
ball = Ball()

s.listen()
s.onkey(paddle.l_paddle_up, "w")
s.onkey(paddle.l_paddle_down, "s")
s.onkey(paddle.r_paddle_up, "Up")
s.onkey(paddle.r_paddle_down, "Down")

while t.ycor() >= -240:
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(25)

def pong_game():
    global SPEED

    # Detect collision with wall.
    if ball.ycor() >= 240 or ball.ycor() <= -240:
        ball.bounce_from_wall()

    # Detect collision with paddle.
    if ball.distance(paddle.l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_from_paddle()
    else:
        if ball.xcor() < -400:
            score.r_p_update_score()
            ball.reset_position()

    if ball.distance(paddle.r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_from_paddle()
    else:
        if ball.xcor() > 400:
            score.l_p_update_score()
            ball.reset_position()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    pong_game()

s.exitonclick()