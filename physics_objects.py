"""
Aum Desai
Fall 2022
CS152B Project 07

This program is for Project 07. It creates 2 objects a ball and block.
This file can be run by putting python3 physics_objects.py in the terminal.
"""

import graphicsPlus as gr
import random as rand

class Ball():

    def __init__(self,win):

        '''
        Initializer method that takes in 2 parameters.
        '''
        self.win = win
        self.mass = 1
        self.radius = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        

        self.scale = 10
        self.vis = [ gr.Circle(gr.Point(self.position[0]*self.scale, win.getHeight()-self.position[1]*self.scale), self.radius * self.scale)]

    def color(self):

        '''
        Colors!!!!!
        '''

        for item in self.vis:
            color_list= ("green","red","yellow","purple","orange","white","black","lavender","khaki","cyan","magenta")
            item.setFill(rand.choices(color_list))


    def draw(self):

        '''
        This method takes the self parameter and draws self.
        '''

        for i in self.vis:

            i.draw(self.win)

    def undraw(self):
        '''Undraws'''
        for i in self.vis:
            i.undraw()

    def getPosition(self): 

        '''
        Returns a 2-element tuple with the x, y position.
        '''

        return self.position[:]
        
    def setPosition(self, px, py): 

        '''
        px and py are the new x,y values
        '''

        x_old = self.position[0] # assign to x_old the current x position

        y_old = self.position[1] # assign to y_old the current y position

        self.position[0] = px # assign to the x coordinate in self.pos the new x coordinate
        self.position[1] = py # assign to the y coordinate in self.pos the new y coordinate

        dx = (px - x_old) * self.scale # assign to dx the change in the x position times self.scale
        dy = (py - y_old) * self.scale * (-1) # assign to dy the change in the y position times -self.scale

        for item in self.vis: # for each item in the vis field of self
            item.move(dx,dy) # call the move method of the item, passing in dx and dy



        
    def getVelocity(self): 
        
        '''
        returns a 2-element tuple with the x and y velocities.
        '''
        
        return self.velocity[:]


    def setVelocity(self, vx, vy): 

        '''
        vx and vy are the new x and y velocities
        '''

        self.velocity[0] = vx
        self.velocity[1] = vy

    def getAcceleration(self): 
       
        '''
        returns a 2-element tuple with the x and y acceleration values.
        '''

        return self.acceleration[:]

    def setAcceleration(self, ax, ay): 

        '''
        ax and ay are new x and y accelerations.
        '''

        self.acceleration[0] = ax
        self.acceleration[1] = ay

    def getMass(self): 

        '''
        Returns the mass of the object as a scalar value
        '''

        return self.mass

    def setMass(self, m): 

        '''
        m is the new mass of the object
        '''

        self.mass = m

    def getRadius(self): 

        '''
        Returns the radius of the Ball as a scalar value
        '''

        return self.radius

    def update(self, dt):

        '''
        This method updates the object taking 2 parameters.
        '''
        # assign to x_old the current x position
        x_old = self.position[0]

        # assign to y_old the current y position
        y_old = self.position[1]

        x_vel = self.velocity[0]
        x_acc = self.acceleration[0]

        y_vel = self.velocity[1]
        y_acc = self.acceleration[1]

        # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 

        self.position[0] = x_old + x_vel * dt + 0.5 * x_acc * dt * dt
        self.position[1] = y_old + y_vel * dt + 0.5 * y_acc * dt * dt

        x_new = self.position[0]
        y_new = self.position[1]


        # assign to dx the change in the x position times the scale factor (self.scale)
        # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        # for each item in self.vis
            # call the move method of the graphics object with dx and dy as arguments..

        dx = (x_new - x_old) * self.scale
        dy = (y_new - y_old) * self.scale * -1

        for item in self.vis:
            item.move(dx,dy)

        self.velocity[0] = x_acc * dt + x_vel
        self.velocity[1] = y_acc * dt + y_vel
        # update the x velocity by adding the acceleration times dt to its old value
        # update the y velocity by adding the acceleration times dt to its old value




class Block():

    def __init__(self, win, dx, dy):

        '''
        Defining a class called Block
        '''

        self.position = [0,0]
        self.dx = dx
        self.dy = dy
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win
        self.scale = 10
        self.vis = [gr.Rectangle(gr.Point((self.position[0] - self.dx / 2) * self.scale,
                                    win.getHeight() - (self.position[1] - self.dy / 2) * self.scale),
                                gr.Point((self.position[0] + self.dx / 2) * self.scale,
                                    win.getHeight() - (self.position[1] + self.dy / 2) * self.scale))]

    def draw(self):

        '''
        Method that draws block into window
        input: nothing
        output: draws block
        '''

        for item in self.vis:
            item.draw(self.win)

    def undraw(self):

        '''
        Method that undraws block from window
        input: nothing
        ouput: undraws block
        '''

        for item in self.vis:
            item.undraw()

    def getPosition(self):

        '''
        Method that gets the x and y position of the block
        input: nothing
        output: blocks position
        '''

        return self.position[:]

    def setPosition(self, px, py):

        '''
        Method that sets the block's positon. takes 2 parameters px and py
        input: px(new x position) and py(new y position)
        output: sets the blocks new position
        '''

        x_old = self.position[0]
        y_old = self.position[1]

        self.position[0] = px
        self.position[1] = py

        dx = (px - x_old) * self.scale
        dy = (py - y_old) * self.scale * (-1)

        for item in self.vis:
            item.move(dx,dy)

    def getVelocity(self):

        '''
        Method that gets the x and y velocity of the block
        input: nothing
        output: blocks velocity
        '''

        return self.velocity[:]

    def setVelocity(self, vx, vy):

        '''
        Method that sets the block's velocity. takes 2 parameters vx and vy
        input: vx(new x velocity) and vy(new y velocity)
        output: sets the blocks new velocity
        '''

        self.velocity[0] = vx
        self.velocity[1] = vy

    def getAcceleration(self):

        '''
        Method that gets the x and y acceleration of the block
        input: nothing
        output: blocks acceleration
        '''
        
        return self.acceleration[:]

    def setAcceleration(self, ax, ay):

        '''
        Method that sets the block's acceleration. takes 2 parameters ax and ay
        input: ax(new x acceleration) and ay(new y acceleration)
        output: sets the blocks new acceleration
        '''

        self.acceleration[0] = ax
        self.acceleration[1] = ay

    def getWidth(self):

        '''
        Method that return the width of the block
        '''

        return self.dx

    def getHeight(self):

        '''
        Method that return the width of the block
        '''

        return self.dy

    def update(self, dt):

        '''
        method that implements the equations of motion for the block
        input: dt
        output: update on object
        '''

        x_old = self.position[0]
        y_old = self.position[1]

        x_vel = self.velocity[0]
        x_acc = self.acceleration[0]

        y_vel = self.velocity[1]
        y_acc = self.acceleration[1]

        self.position[0] = x_old + x_vel * dt + 0.5 * x_acc * dt * dt
        self.position[1] = y_old + y_vel * dt + 0.5 * y_acc * dt * dt

        x_new = self.position[0]
        y_new = self.position[1]
        
        dx = (x_new - x_old) * self.scale
        dy = (y_new - y_old) * self.scale * (-1)

        for item in self.vis:
            item.move(dx,dy)

        self.velocity[0] = x_acc * dt + x_vel
        self.velocity[1] = y_acc * dt + y_vel




    def collision(self, ball):

        '''
        function that takes 2 parameters and detects a collision
        '''

        blockpos = self.getPosition()
        ballpos = ball.getPosition()

        radius = ball.getRadius()
        height = self.getHeight()
        width = self.getWidth()

        dx = ballpos[0] - blockpos[0]
        dy = ballpos[1] - blockpos[1]

        if abs(dy) <= radius + (height / 2) and abs(dx) <= radius + (width / 2):
            return True

    
    def color(self):

        '''
        Colors!!!!!
        '''

        for item in self.vis:
            color_list= ("green","red","yellow","purple","orange","white","black","lavender","khaki","cyan","magenta")
            item.setFill(rand.choices(color_list))







