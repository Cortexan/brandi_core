# env imports
import numpy as np
from psychopy import visual
from psychopy.hardware import keyboard

# local imports
from settings import color_set

# create visual window
win = visual.Window(
	size=[2560, 1440],
	fullscr=True,
	screen=1,
	winType="pyglet",
	monitor="Home2",
	colorSpace="hex",
	color=color_set["bgColor"],
	checkTiming=False,
	infoMsg="Just a moment...",
)

# hide the mouse
win.mouseVisible = False

# warm up the window
for x in range(50):
	win.flip()

# get the frame duration
frame_test = []
for i in range(10):
	frame_time = 1.0 / round(win.getActualFrameRate(infoMsg="Just a moment..."))
	frame_test.append(frame_time)
frame_dur = 1000 * np.median(frame_test)

kb = keyboard.Keyboard()
