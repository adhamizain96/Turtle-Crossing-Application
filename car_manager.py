#!/usr/bin/env python
# coding: utf-8

# In[3]:


import turtle as t
import random
#constant is a type of variable whose value cannot be changed.
#3 primary colors - red, yellow, blue / 3 secondary colors - orange, green, violet
COLORS = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
START_MOVE_DIS = 5
MOVE_INCREMENT = 5

class Car_Manager:
    def __init__(self):
        #create a list
        self.all_cars = []
        self.car_speed = START_MOVE_DIS
    def create_cars(self):
        rand_choice = random.randint(1, 6)
        if rand_choice == 1:
            new_car = t.Turtle('square')
            #t.shapesize() - return or set the pen’s attributes x/y-stretchfactors and/or outline.
            #t.shapesize() - stretch_wid = None, stretch_len = None, outline = None
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            #t.penup() - pull the pen up - no drawing when moving.
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            #t.goto() - move turtle to an absolute position.
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            #t.backward() - move the turtle backward by distance, opposite to the direction the turtle is headed.
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT


# In[ ]:




