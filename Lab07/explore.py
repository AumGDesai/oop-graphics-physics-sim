"""
Aum Desai
Fall 2022
CS152B Lab 07

This program is for Lab 07. It explores Zelle Graphics.
You can run it by putting python3 explore.py in the terminal.
This file explores creating circles and their motion.
"""

import zelle as gr
import random as rand
import time

def test1():

    '''
    This is a test function that creates a circle object.
    '''
    
    win = gr.GraphWin('My First Window WhooHoo', 500, 500,False)
    
    point = gr.Point(100,200)
    circle = gr.Circle(point,10)

    circle.draw(win)

    win.update()

    clickPoint = win.getMouse()
    xValue = clickPoint.getX()
    yValue = clickPoint.getY()
    print(str(xValue) + "," + str(yValue))

    win.close()

def test2():

    '''
    This is another test function that plots a circle object made via 
    a mouse click and it also has random motion.
    '''

    win = gr.GraphWin('My Second Window WhooHoo', 500, 500,False)
    win.setBackground("white")

    shapes = []

    while True:

        pos = win.checkMouse()

        if pos != None:

            circle = gr.Circle(pos,10)

            circle.setFill("blue")

            shapes.append(circle)

            circle.draw(win)

        keyString = win.checkKey()

        if keyString  == "q":

            break

        win.update()

        time.sleep(0.033)

        for i in shapes:
            
            i.move(rand.uniform(-50,50), rand.uniform(-50,50))


    win.close()








if __name__ == "__main__":
    test2()



    
    
  
 
