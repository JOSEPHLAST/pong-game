from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("grey")
        self.penup()
        self.l_p_score = 0
        self.r_p_score = 0
        self.blit_l_p_score()
        self.blit_r_p_score()

    def blit_l_p_score(self):
        self.goto(-150, 170)
        self.write(f"{self.l_p_score}", False, "left", ("Courier", 60, "bold"))

    def blit_r_p_score(self):
        self.goto(150, 170)
        self.write(f"{self.r_p_score}", False, "right", ("Courier", 60, "bold"))

    def l_p_update_score(self):
        self.l_p_score += 1
        self.clear()
        self.blit_l_p_score()
        self.blit_r_p_score()

    def r_p_update_score(self):
        self.r_p_score += 1
        self.clear()
        self.blit_l_p_score()
        self.blit_r_p_score()