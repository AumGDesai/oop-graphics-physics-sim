"""
Aum Desai
Fall 2022
CS152B Project 07

This program is for Project 07. 
You can run it by putting python3 testFall+block.py in the terminal.
This file explores the motion of a falling ball and the collsion with a block.
"""

import graphicsPlus as gr
import physics_objects as pho
import random as rand
import time

# main function for implementing the test code
def main():

    '''
    Main function that holds the creation and implementation of the objects.
    '''

    # create a graphics window
    win = gr.GraphWin("Falling", 500, 500, False)
    win.setBackground("white")



    # create a ball
    ball = pho.Ball(win)
    # move it to the center of the screen and draw it
    
    block = pho.Block(win, dx = 6, dy = 3)
    block.setPosition(20,5)

    block1 = pho.Block(win, dx = 6, dy = 3)
    block1.setPosition(30,5)
    

    block.draw()
    block1.draw()
    
    
    ball.setPosition(25,25)

    p = ball.getPosition()
    print( 'Position:', p[0], p[1])
    ball.draw()

    # give it a random velocity
    ball.setVelocity( rand.randint(-1,1), rand.randint(-1,1) )

    v = ball.getVelocity()
    print( 'New Velocity:', v[0], v[1])

    # set the acceleration to (0, -20)
    ball.setAcceleration(0,-20)

    
    

 
    

    while True:
        dt = 0.033
        # call the ball's update method with a dt of 0.033
        ball.update(dt)
        time.sleep( 0.033 ) # have the animation go at the same speed

        if block.collision( ball):
            
            block.undraw()

        if block1.collision( ball):
            
            block1.undraw()

        if win.checkKey() == 'q': # did the user type a 'q'?
            break
        
        if win.checkMouse(): # did the user click the mouse?
            break
        
        
        pos = ball.getPosition()
        print(pos)
        # if the ball is outside the window

        if pos[0] <= 0 or pos[0] >= 50 or pos[1] <= 0 or pos[1] >= 50:

           # reposition the ball to the center of the window

            ball.setPosition(25,25)
            
            print(ball.getPosition())
            # ball.setVelocity(0,0)
            # ball.setAcceleration(0,0)
            
           
           # give it a random velocity
            ball.setVelocity(rand.randint(-1,1), rand.randint(-1,1))
           
           
    win.close()

if __name__ == "__main__":
    main()