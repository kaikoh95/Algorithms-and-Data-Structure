from turtle import *
from random import *
colormode(255)

def spiral(n_steps):
    # pencolor(10,100, int(255/n_steps))
    for i in range(1,n_steps):
        real_i = float(i)
        pensize((real_i/n_steps)*20)
        forward(i)
        right(20)



def spiral2(n_steps):
    if n_steps < 2:
        pass
    else:
        pencolor(10,100, int(255/n_steps))
        i = 100 - n_steps
        real_i = float(i)
        pensize((real_i/n_steps)*2)
        forward(i)
        right(20)
        spiral2(n_steps-1)


def triangle(length, level):
    if level == 0:
        forward(length)
    else:
        triangle(length/1.2, level - 1)
        right(120)
        triangle(length/1.2, level - 1)
        right(120)
        triangle(length/1.2, level - 1)
        right(120)
    


def simple_tree(length,level):
    if not(level==0):
        forward(length)
        pos=position()
        left(20)
        simple_tree(length/1.2,level-1)
        goto(pos)
        right(40)
        simple_tree(length/1.2,level-1)
        goto(pos)
        left(20)


def random_tree(size,level):
    """
    Draws a funky fractal tree.
    Feel free to experiment with parameters...
    """
    if level!=0:
        forward(random()*size)
        x = pos()
        angle=random()*20
        right(angle)
        random_tree(size*.8,level-1)
        setpos(x)
        left(angle)
        angle=random()*-20
        right(angle)
        random_tree(size*.8,level-1)
        left(angle)
        setpos(x)
        
        
def square(size,level):
    if not(level==0):
        right(20)
        square(size/2,level-1)	
        right(20)
        square(size/2,level-1)
        right(20)
        square(size/2,level-1)
        right(20)
        square(size/2,level-1)
        forward(size)
        right(90)
        forward(size)
        right(90)
        forward(size)
        right(90)
        forward(size)
        right(90)


#simple_tree(100,6)
#left(180)
#random_tree(100,4)
#square(200,4)
#max_steps = 100
#spiral(100)
#spiral2(100)
#triangle(200,3)
shape('turtle')
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(-90)
forward(100)
right(-90)
forward(50)
left(90)
forward(100)