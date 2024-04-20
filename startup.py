from psychopy import visual
from psychopy.hardware import keyboard

win = visual.Window(size = [800, 800],
                    fullscr = False,
                    screen = 0,
                    monitor = 'Home2',
                    color = (0,0,0))

win.mouseVisible = False

kb = keyboard.Keyboard()