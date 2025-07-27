"""
Aum Desai
Fall 2022
CS152B Lab 07

This program is for Lab 07. 
You can run it by putting python3 testFall.py in the terminal.
This file explores the motion of a fall ball.
"""
import zelle as gr
import physics_objects as pho
import random as rand
import time

# main function for implementing the test code
def main():

    # create a graphics window
    win = gr.GraphWin("Falling", 500, 500, False)
    win.setBackground("white")

    # create a ball
    ball = pho.Ball(win)
    # move it to the center of the screen and draw it
    
    
    ball.setPosition(25,25)

    p = ball.getPosition()
    print( 'Position:', p[0], p[1])
    ball.draw()

    # give it a random velocity
    ball.setVelocity( rand.random(), rand.random() )

    v = ball.getVelocity()
    print( 'New Velocity:', v[0], v[1])

    # set the acceleration to (0, -20)
    ball.setAcceleration(0,-20)

    

    while True:
        dt = 0.033
        # call the ball's update method with a dt of 0.033
        ball.update(dt)
        time.sleep( 0.033 ) # have the animation go at the same speed

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
            ball.setVelocity(rand.random(), rand.random())
           
           
    win.close()

if __name__ == "__main__":
    main()