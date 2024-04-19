from startup import win
from settings import *
from stimuli import *
from psychopy import visual, core
from psychopy.hardware import keyboard
from functions import pRands, radGrid, waitSpace

kb = keyboard.Keyboard()

shapes = [square, diamond, triangle, circle, cross, hexagon, rectangle, oval, gate]

for shape in shapes:
    shape.draw()
    win.flip()
    kb.waitKeys(keyList=['space'])

for shape in shapes:
    shape.draw()
win.flip()

kb.waitKeys(keyList=['space'])

win.close()
core,quit()
