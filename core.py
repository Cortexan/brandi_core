# Importing necessary modules, functions, and settings from other local files
from psychopy import core
from functions import pRands, radGrid, waitSpace
from startup import win, kb
from settings import *
from stimuli import Shape, Fix

#%% - creating stimuli
#region - click carrot to expand
# creating all of the stimuli - these are all instances of the Shape class, which is defined in stimuli.py
# the Shape class requires a shape name (string) and a scale (float) as arguments
# you can create multiple instances of the same shape, as long as you give them different variable names.
# then, each instance can be drawn and displayed on the screen independently.
# however, the shape name must be one of the keys in the shapes dictionary in stimuli.py.
# the scale is a float that will be multiplied by the size of the shape in degrees visual angle.
# all shapes have an equal surface area for a given scale, so they will all be the same size on the screen.
# you can change the size of the shapes by changing the scale value.
#endregion

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

# group stimuli
shapes = [square, diamond, triangle, circle, cross, hexagon, rectangle, oval, gate]

#%% - creating radial grid positions for each ring

# # create radial grid positions for each ring -- not in use yet
# r1_postions = radGrid(n_stim_r1, r1_radius)
# r2_postions = radGrid(n_stim_r2, r2_radius)

#%% - setup colors
#region
# select colors from color_set (defined in settings.py) - 
# I'm using list comprehension to get all the values from the dictionary,
# but you could also just list them out manually, calling each color (or 'key') by name.
#endregion
colors = [color for color in color_set.values()]


# Main loop example:

# this sets the fixation to draw on every frame, without needing to call draw() on it.
# Call "fix.setAutoDraw(False)" to stop drawing it.
fix.setAutoDraw(True)
# "flipping" the window is like refreshing the screen - 
# it shows all the stimuli that have been drawn since the last flip.
win.flip()

# "enumerate" is a built-in function that returns both the index and the value of each item in a list.
for idx, shape in enumerate(shapes):
    # the "setColor" method sets the color of the shape -
    # you can similarly set various parameters such as orientation, size, color, position, opacity, etc.
    shape.setColor(colors[idx])

for shape in shapes:
    # the "draw" method draws the shape on the screen, but only for the next flip.
    shape.draw()
    win.flip()
    # "waitKeys" waits for a key press, and returns the key that was pressed.
    # you can also specify a list of keys to wait for, and only those keys will be accepted.
    # this is useful for making sure the participant doesn't accidentally press the wrong key.
    # it also captures their response time
    kb.waitKeys(keyList=['space'])
    win.flip()
    # "core.wait" pauses the script for a specified amount of time in seconds.
    core.wait(0.1)

for shape in shapes:
    shape.draw()
win.flip()

kb.waitKeys(keyList=['space'])

# the win.close() method closes the window, and core.quit() exits the script.
win.close()
core.quit()
