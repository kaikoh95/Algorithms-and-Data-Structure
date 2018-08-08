"""Implements a helper class for drawing fractals.
You shouldn't need to write any code here - you should work with the 
fractal_drawing.py file.
You will import FractalCanvas from this module and make child classes that will
have some code to draw the given fractal.
See the SierpinskiTriangle class, where we have done this for you:)
For the other classes you will need to write the recursive draw_xx method.
See the fractal_drawing.py module.
"""
from tkinter import *
from turtle import TurtleScreen, RawTurtle



class FractalCanvas(object):
    
    def __init__(self, parent, levels):
        """ Parent should be a tk frame - see fractal_drawing calls.
        We will use this init function for all children..."""
        

        # levels of recursion when calling recursive draws.        
        self.levels = levels

        # Toggles screen update rate
        self.slow_drawing = False

        # Draw button
        button = Button(parent, text='Draw Fractal', command=self._draw_click)
        button.pack()
        width, height = (600, 600)
        self.canvas = Canvas(parent, width=600, height=600)

        # Constrain resizing to a 1:1 aspect ratio
        self.canvas.winfo_toplevel().aspect(1,1,1,1)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Setup a turtle
        self.turtleScreen = TurtleScreen(self.canvas)

        # 5px of padding
        self.turtleScreen.setworldcoordinates(-5, -height-5, width+5, 5)
        self.turtle = RawTurtle(self.turtleScreen)
        self.turtleScreen.colormode(255)

        # Listen to resize events
        self.canvas.bind('<Configure>', self._resize_and_draw)
            
        # Do an initial draw
        self.slow_drawing = True
        self._resize_and_draw()
        self.slow_drawing = False
        
    def _draw_click(self):
        """Handler for button click."""
        # Draw the fractal slowly when we press the button, but quickly
        # if we're drawing for a resize
        self.slow_drawing = True
        self._resize_and_draw()       
        self.slow_drawing = False
        
    def _resize_and_draw(self,event=None):
        """Handler for when the canvas resizes (due to a window resize)."""
        self.draw(self.canvas.winfo_width(), self.canvas.winfo_height())
        
    def draw(self, width, height):
        """Draws the fractal."""
        pass
    
    def update_screen(self):
        """
        Conditionally updates the screen.
        If self.slow_drawing is set, then this method forces image data to be
        pushed to the screen, otherwise it does nothing.
        """
        if self.slow_drawing:
            self.turtleScreen.update()
    
