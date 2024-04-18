from psychopy import visual
from startup import win
from numpy import pi


# scaling constants:
cir_const = 7978
scale_factor = 1


square      =   visual.ShapeStim(win = win,
                                 vertices=((-1, -1),
                                           (-1,  1),
                                           ( 1,  1),
                                           ( 1, -1)),
                                 size = scale_factor * 0.5,
                                 ori = 0,
                                 units = 'deg',
                                 fillColor='red',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)

diamond     =   visual.ShapeStim(win = win,
                                 vertices=((-1, -1),
                                           (-1,  1),
                                           ( 1,  1),
                                           ( 1, -1)),
                                 size = scale_factor * 0.5,
                                 ori = 45,
                                 units = 'deg',
                                 fillColor='green',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)

triangle    =   visual.ShapeStim(win = win,
                                 vertices=(( 0, 1.7546),
                                           (-1.5195, -0.8773),
                                           ( 1.5195, -0.8773)),
                                 size = scale_factor * 0.5,
                                 units = 'deg',
                                 fillColor='blue',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)

circle      =   visual.ShapeStim(win = win, #TODO needs scale factor adjustments
                                 vertices=360,
                                 size = scale_factor * 1.1284,
                                 units = 'deg',
                                 fillColor='yellow',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)

cross       =   visual.ShapeStim(win = win,
                                 vertices=((-1.341,  0.447), (-1.341, -0.447),
                                           (-0.447, -0.447), (-0.447, -1.341),
                                           ( 0.447, -1.341), ( 0.447, -0.447),
                                           ( 1.341, -0.447), ( 1.341,  0.447),
                                           ( 0.447,  0.447), ( 0.447,  1.341),
                                           (-0.447,  1.341), (-0.447,  0.447)),
                                 size = scale_factor * 0.5,
                                 ori = 0,
                                 units = 'deg',
                                 fillColor='purple',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)

hexagon     =   visual.ShapeStim(win = win,
                                 vertices=(( 1.2408, 0.0),     ( 0.6204, 1.0746),
                                           (-0.6204, 1.0746),  (-1.2408, 0.0),
                                           (-0.6204, -1.0746), ( 0.6204, -1.0746)),
                                 size = scale_factor * 0.5,
                                 ori = 0,
                                 units = 'deg',
                                 fillColor='red',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)

rectangle   =   visual.ShapeStim(win = win,
                                 vertices=((-1.272, -0.7862),
                                           ( 1.272, -0.7862),
                                           ( 1.272, 0.7862),
                                           (-1.272, 0.7862)),
                                 size = scale_factor * 0.5,
                                 ori = 0,
                                 units = 'deg',
                                 fillColor='green',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)

oval        =   visual.ShapeStim(win = win, #TODO needs scale factor adjustments
                                 vertices=360,
                                 size = (scale_factor * 0.8871,
                                         scale_factor * 1.4353),
                                 units = 'deg',
                                 fillColor='yellow',
                                 lineColor='black',
                                 lineWidth = 0,
                                 opacity  = 0.5)