from startup import win, kb
from settings import *
from stimuli import Shape, Fix
from psychopy import visual, core
from psychopy.hardware import keyboard
from functions import pRands, radGrid, waitSpace

win.mouseVisible = False

shape_dva = 1

square      = Shape('square', shape_dva)
diamond     = Shape('diamond', shape_dva)
triangle    = Shape('triangle', shape_dva)
circle      = Shape('circle', shape_dva)
cross       = Shape('cross', shape_dva)
hexagon     = Shape('hexagon', shape_dva)
rectangle   = Shape('rectangle', shape_dva)
oval        = Shape('oval', shape_dva)
gate        = Shape('gate', shape_dva)
fix         = Fix()

shapes = [square, diamond, triangle, circle, cross, hexagon, rectangle, oval, gate]
colors = ['red', 'green', 'blue', 'yellow', 'black', 'purple', 'orange', 'pink', 'white']

fix.setAutoDraw(True)
win.flip()

for idx, shape in enumerate(shapes):
    shape.setColor(colors[idx])

for shape in shapes:
    shape.draw()
    win.flip()
    kb.waitKeys(keyList=['space'])
    win.flip()
    core.wait(0.1)

for shape in shapes:
    shape.draw()
win.flip()

kb.waitKeys(keyList=['space'])

win.close()
core.quit()
