from turtle import Turtle
from random import choice

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_from_wall(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        direction = choice([-1, 1])
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_from_paddle()
        self.y_move *= direction