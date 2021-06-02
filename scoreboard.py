from turtle import Turtle

# constants for font and alignment of text
ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")

# create class score that is a Turtle super
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()

    # write out the current score to screen
    def update_score(self): 
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))

    # spawn game over text in the centre of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT))
    
    # refresh score by clearing current score and incrementing score 
    def refresh(self):
        self.score += 1
        self.clear()
        self.update_score()
