#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
import time
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width = 500, height = 500)
#t.tracer() - turn turtle animation on/off and set delay for update drawings.
screen.tracer(0)

player = Player()
car_manager = Car_Manager()
scoreboard = Scoreboard()

#t.listen() - set focus on TurtleScreen (in order to collect key-events). 
screen.listen()
#t.onkey() - bind fun to key-release event of key. 
screen.onkey(player.go_up, 'w')

turtle_cross_on = True
while turtle_cross_on:
    #time.sleep() - suspends execution for the given number of seconds.
    #note - adjust speed to make it faster or slower
    time.sleep(0.1)
    #screen.update() - perform a TurtleScreen update. 
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        #t.distance() - return the distance from the turtle to (x,y), the given vector, or the given other turtle, in turtle step units.
        #user loses
        if car.distance(player) < 20:
            turtle_cross_on = False
            scoreboard.game_over()
        #user wins
        if player.finish_line():
            player.start_position()
            car_manager.level_up()
            scoreboard.increase_level()

screen.exitonclick()


# In[ ]:




