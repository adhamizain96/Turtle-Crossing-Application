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
        #t.penup() - pull the pen up - no drawing when moving.
        self.penup
        self.start_position()
        #t.setheading() - set the orientation of the turtle to to_angle
        self.setheading(90)
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




