from psychopy import visual
from psychopy.hardware import keyboard
from settings import color_set

win = visual.Window(size = [800, 800],
                    fullscr = False,
                    screen = 0,
                    monitor = 'Home2',
                    color = color_set['bgColor'])

win.mouseVisible = False

kb = keyboard.Keyboard()