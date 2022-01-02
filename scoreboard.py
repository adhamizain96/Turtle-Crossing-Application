#!/usr/bin/env python
# coding: utf-8

# In[5]:


import turtle as t
#constant is a type of variable whose value cannot be changed.
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        #t.hideturtle() - make the turtle invisible.
        self.hideturtle()
        #t.penup() - pull the pen up - no drawing when moving.
        self.penup()
        #t.goto() - move turtle to an absolute position.
        self.goto(-250, 250)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align = ALIGNMENT, font = FONT)
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        #user loses
        #t.goto() - move turtle to an absolute position.
        self.goto(0, 0)
        self.write(f'Game Over', align = ALIGNMENT, font = FONT)


# In[ ]:




