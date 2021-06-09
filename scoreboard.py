from turtle import Turtle

# constants for font and alignment of text
ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")

# create class score that is a Turtle super
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # open file hi_score.txt, cast the contents to an int and save them to the hi_score variable
        with open('hi_score.txt') as data:
            self.hi_score = int(data.read())
        self.color('white')
        self.pu()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()

    # write out the current score to screen
    def update_score(self): 
        self.clear()
        self.write(f"Score: {self.score} Hi Score: {self.hi_score}", align=ALIGNMENT, font=(FONT))

    # set hi score then convert to a string and write to the file hi_score.txt
    # then reset the score and scoreboard
    def reset(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
        
        with open('hi_score.txt', mode='w') as data:
            data.write(f"{self.hi_score}")

        self.score = 0
        self.update_score()
    
    # refresh score by clearing current score and incrementing score 
    def refresh(self):
        self.score += 1
        self.update_score()
