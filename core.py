# Importing necessary modules, functions, and settings from other local files
# ruff: noqa: F401, F403, F405, F821
# env imports
from psychopy import core

from settings import *

# from functions import pRands, radGrid, waitSpace
from startup import frame_dur, kb, win
from stimuli import Fix, Shape

# %% - creating stimuli
# creating all the stimuli - these are all instances of the Shape class, which is defined in stimuli.py
# the Shape class requires a shape name (string) and a scale (float) as arguments
# you can create multiple instances of the same shape, as long as you give them different variable names.
# then, each instance can be drawn and displayed on the screen independently.
# however, the shape name must be one of the keys in the shapes dictionary in stimuli.py.
# the scale is a float that will be multiplied by the size of the shape in degrees visual angle.
# all shapes have an equal surface area for a given scale, so they will all be the same size on the screen.
# you can change the size of the shapes by changing the scale value.
# endregion

square = Shape(shape="square", scale=shape_dva)
diamond = Shape(shape="diamond", scale=shape_dva)
triangle = Shape(shape="triangle", scale=shape_dva)
circle = Shape(shape="circle", scale=shape_dva)
cross = Shape(shape="cross", scale=shape_dva)
hexagon = Shape(shape="hexagon", scale=shape_dva)
rectangle = Shape(shape="rectangle", scale=shape_dva)
oval = Shape(shape="oval", scale=shape_dva)
gate = Shape(shape="gate", scale=shape_dva)
fix = Fix(shape="o", scale=fix_dva, color=color_set["fixColor"])

# group stimuli
shapes = [square, diamond, triangle, circle, cross, hexagon, rectangle, oval, gate]

# %% - creating radial grid positions for each ring

# # create radial grid positions for each ring -- not in use yet
# r1_positions = radGrid(n_stim_r1, r1_radius)
# r2_positions = radGrid(n_stim_r2, r2_radius)

# %% - setup colors
# region click carrot to expand
# select colors from color_set (defined in settings.py) -
# I'm using list comprehension to get a different color value from the dictionary for each shape,
# but you could also just list them out manually, calling each color (or 'key') by name.
# the dictionary is a convenient way to be able to refer to each colour by a name rather than a number
# (e.g. color_set[0] vs color_set['red']). There are various alternative ways this could be set up.
# endregion
colors = [color for color in color_set.values()]
colors = colors[: len(shapes) + 1]

# convert fixed event timings in ms to frames based on framerate
iti_dur = round(iti_ms / frame_dur)
isi_dur = round(isi_ms / frame_dur)


# Main loop example:

# this sets the fixation to draw on every frame, without needing to call draw() on it.
# Call "fix.setAutoDraw(False)" to stop drawing it.
fix.setAutoDraw(True)

# "flipping" the window is like refreshing the screen -
# it shows all the stimuli that have been drawn since the last flip.
for frame in range(iti_dur):
	win.flip()
kb.waitKeys(keyList=["space"])


# "enumerate" is a built-in function that returns both the index and the value of each item in a list.
for idx, shape in enumerate(shapes):
	# the "setColor" method sets the color of the shape -
	# you can similarly set various parameters such as orientation, size, color, position, opacity, etc.
	shape.setColor(colors[idx])
	# draw the shape on screen for a set duration of time
	# (defined in "flips", which have the duration of a single frame)
	for frame in range(isi_dur):
		# the "draw" method draws the shape on the screen, but only for the next flip.
		shape.draw()
		win.flip()

	# here we flip without calling draw, causing a blank screen to appear.
	win.flip()

	# "waitKeys" waits for a key press, and returns the key that was pressed.
	# you can also specify a list of keys to wait for, and only those keys will be accepted.
	# this is useful for making sure the participant doesn't accidentally press the wrong key.
	# it also captures their response time
	kb.waitKeys(keyList=["space"])

for shape in shapes:
	shape.draw()
win.flip()

kb.waitKeys(keyList=["space"])

# the win.close() method closes the window, and core.quit() exits the script.
win.close()
core.quit()
