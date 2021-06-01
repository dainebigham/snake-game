from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()

    def update_score(self): 
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))
       
    def refresh(self):
        self.score += 1
        self.clear()
        self.update_score()
