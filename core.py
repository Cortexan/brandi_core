from settings import *
from functions import pRands, radGrid, waitSpace
# from stimuli import square, win
from psychopy import visual, core
from psychopy.hardware import keyboard
from startup import win
from stimuli import *

kb = keyboard.Keyboard()

shapes = [square, diamond, triangle, circle, cross, hexagon, rectangle, oval]


for shape in shapes:
    shape.draw()
    win.flip()
    kb.waitKeys(keyList=['space'])


square.draw()
diamond.draw()
triangle.draw()
circle.draw()
cross.draw()
hexagon.draw()
rectangle.draw()
oval.draw()
win.flip()
kb.waitKeys(keyList=['space'])
