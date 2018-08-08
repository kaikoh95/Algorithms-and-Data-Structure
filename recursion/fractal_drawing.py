"""Classes for drawing some fractals.
To draw quickly change the TRACER_SETTING from None to 0.
This will turn off animation but still refresh every step.
Changing 0 to an integer n will skip n steps of the drawing and speed up 
even more. For example self.turtleScreen.tracer(9) will skip 9 frames
and effectively update every 10th."""

from tkinter import *
from fractals import FractalCanvas
import math

COUNTER = 0
TRACER_SETTING = 0

class SierpinskiTriangle(FractalCanvas):
    """Implements draw method so that a Sierpinski triangle is drawn."""
    
    count = 0
    def counter(self):
        return count
    def add_count(self):
        count += 1
    def draw(self, width, height):
        global COUNTER
        """Sets up various bits for the initial draw."""
        # Keep the triangle bounded inside a square
        t_size = min(width, height)
            
        # And keep it centred
        outer_triangle = [((width/2)-(t_size/2),-(height/2)-(t_size/2)),
                          (width/2, (-height/2)+(t_size/2)),
                          ((width/2)+(t_size/2),-(height/2)-(t_size/2))]

        # Setup colour gradient from dark orange-brown to light
        step = 255.0 / max(1, self.levels)
        colour_vals = [1*step*k for k in range(self.levels+1)]
        self.colours = [(int(k), int(k/2), int(k/4)) for k in colour_vals]
        
        # Start recursively drawing the triangle
        self.turtle.reset()
        self.turtleScreen.tracer(TRACER_SETTING)
        self.turtle.penup()
        COUNTER += 1
        self.draw_triangle(outer_triangle, self.levels)
        
    def draw_triangle(self, points, level):
        """
        Recursively draws the Sierpinski triangle.
        'points' is a list of (x,y) tuples containing the co-ordinates of where
        to draw the triangle.
        'level' is which level of the triangle we're up to (where 0 is the
        innermost level).
        """
        global COUNTER
        # Set the fill colour
        self.turtle.fillcolor(self.colours[level])
        
        # Draw the triangle
        self.turtle.begin_fill()        
        self.turtle.goto(*points[0])   # Move to the first point
        self.turtle.pendown()          # Put the turtle pen down
        self.turtle.goto(*points[1])   # Draw move round 3 points of triangle
        self.turtle.goto(*points[2])
        self.turtle.goto(*points[0])
        self.turtle.penup()            # Lift the pen up
        self.turtle.end_fill()         # Finish the colour fill
        
        self.update_screen()           
        
        # If we still have more levels to draw...
        if level > 0:
            # Calculate the position of the three inner triangles and recursively
            # draw them and their inner triangles
            inner_points = [points[0], self.midpoint(points[0], points[1]), 
                            self.midpoint(points[0], points[2])]
            COUNTER += 1
            self.draw_triangle(inner_points, level-1)
            inner_points = [points[1], self.midpoint(points[0], points[1]), 
                            self.midpoint(points[1], points[2])]
            COUNTER += 1
            self.draw_triangle(inner_points, level-1)
            inner_points = [points[2], self.midpoint(points[2], points[1]), 
                            self.midpoint(points[0], points[2])]
            COUNTER += 1
            
            self.draw_triangle(inner_points, level-1)
            
    def midpoint(self, p1, p2):
        """Returns a tuple of the midpoint between two (x,y) point tuples."""
        return ((p1[0] + p2[0])/2.0, (p1[1] + p2[1])/2.0)



#-------------------------------------------------------------------------------            
class HilbertCurve(FractalCanvas):
    """Implements draw method so that a Hilbert curve is drawn."""
    
    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtleScreen.tracer(None)
        
        # Scale the line length such that the entire curve fits on the screen
        length = 2**self.levels - (1.0 / 2**self.levels)
        self.line_length = width / length
        self.draw_hilbert(self.levels, 90)
        self.turtleScreeni.update()        
        
    def draw_hilbert(self, level, angle):
        pass



#-------------------------------------------------------------------------------        
class KochCurve(FractalCanvas):
    """Implements draw method so that a Koch curve is drawn."""
    
    # Class level constant
    ANGLE = 60
    # Try an angle of 80 for fun results:)
    
    def draw_koch(self, level, length):
        """Recursive function.
        At level zero just draws a forward line of given length.
        At higher levels does the following:
           draws a (level-1) koch_curve then turns ANGLE degrees left
           draws a (level-1) koch_curve then turns 2*ANGLE degrees right
           draws a (level-1) koch_curve then turns ANGLE degress left
           draws a (level-1) koch_curve.
        then draws another level-1 kochcurve."""
        pass

    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtleScreen.tracer(TRACER_SETTING)
        
        # Position the turtle at the centre-left of the screen
        self.turtle.penup()
        self.turtle.goto(0, -height/2)
        self.turtle.pendown()
        
        # call the recursive draw_koch function
        self.draw_koch(self.levels, width)
        self.turtleScreen.update()



#-------------------------------------------------------------------------------        
class KochSnowflake(KochCurve):
    """Implements draw method so that a Koch snowflake is drawn."""
    
    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtleScreen.tracer(TRACER_SETTING)
        
        # Position the turtle at the centre-top of the screen
        self.turtle.penup()
        self.turtle.goto(width/2, 0)
        self.turtle.pendown()
        self.turtle.right(60)
        length = math.sqrt(math.pow(width/2, 2) + math.pow(height/1.5, 2))
        # Now draw three kock_curves, turning 120o right in between







#-------------------------------------------------------------------------------        
class DragonCurve(FractalCanvas):
    """Implements draw method so that a dragon curve is drawn."""
 
    def draw_dragon(self, level, length, angle):
        """Recursive funciton for drawing dragon curves."""
        pass

    def draw(self, width, height):
        # Reset the turtle
        self.turtle.reset()
        self.turtleScreen.tracer(TRACER_SETTING)
        
        # Position the turtle at the centre of the screen
        self.turtle.penup()
        self.turtle.goto(width/4, -height/3)
        self.turtle.pendown()
        # Call the recursive drawing funciton
        self.draw_dragon(self.levels, width/2, 45)
        self.turtleScreen.update()
        
        
if __name__ == '__main__':
    # Setup tk canvas
    root = Tk()
    frame = Frame(root)
    frame.pack(fill=BOTH,expand=YES)

    # NOTE:
    # Try drawing the 0, 1, and 2 level versions of all of these by hand
    # This will give you a feeling for how they are constructed

    # Only run one fractal at a time, or you will get crazy stacking...
    # If you run without calling any drawings then your shell will be stuck waiting
    # so click on Options - Restart Shell from the shell menu bar.

    # Draw a SierpinskiTriangle to 0 level
    # Drawing level 0 is a good idea as it shows you the
    # base unit when drawing the fractal.
    t = SierpinskiTriangle(frame, 5) 
    # t = SierpinskiTriangle(frame, 5)
    
    
    # Draw a KochCurve to 0 level
    # Try more levels after you have seen the base case
    #k = KochCurve(frame, 0)
    

    
    # Draw full snowflake at level 0
    # Try more levels after you have seen the base case
    #f = KochSnowflake(frame, 0)




    
    #Draw a dragon curve at level 0
    # Try more levels after you have seen the base case
    #d=DragonCurve(frame, 0)


    root.mainloop()
