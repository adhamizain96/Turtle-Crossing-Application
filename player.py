#!/usr/bin/env python
# coding: utf-8

# In[5]:


import turtle as t
#constant is a type of variable whose value cannot be changed.
START_POS = (0, -250)
MOVE_DIS = 10
FINISH_LINE = 250

class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup
        self.start_position()
        self.setheading(100)
    def go_up(self):
        #t.forward() - move the turtle forward by the specified distance, in the direction the turtle is headed.
        self.forward(MOVE_DIS)
    def start_position(self):
        #t.goto() - move turtle to an absolute position.
        self.goto(START_POS)
    def finish_line(self):
        #user wins
        if self.ycor() > FINISH_LINE:
            return True
        #user loses
        else:
            return False


# In[ ]:




