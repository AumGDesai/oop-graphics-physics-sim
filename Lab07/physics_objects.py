"""
Aum Desai
Fall 2022
CS152B Lab 07

This program is for Lab 07. It explores creating objects that have motion.
This file can be run by putting python3 physics_objects.py in the terminal.
"""

import zelle as gr

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




