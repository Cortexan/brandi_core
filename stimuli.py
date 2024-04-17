from psychopy import visual
from startup import win


square = visual.ShapeStim(win = win,
                          vertices=((-1, -1),
                                    (-1, 1),
                                    (1, 1),
                                    (1, -1)),
                          fillColor='black',
                          lineColor='black')