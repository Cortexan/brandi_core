import numpy as np
from numpy import sin, cos, sqrt, deg2rad
from numpy.random import shuffle, choice
from itertools import product
from psychopy import core


def pRands(n_trials, n_reps, values = [1,2,3,4]):
    data = np.zeros((n_trials, n_reps), dtype=int)
    val_combos = list(product(values, repeat=2))
    combo_repeats = (n_trials//len(val_combos))+(1 if n_trials%len(val_combos) else 0)

    # Initialize start_col with balanced values
    start_col = np.tile([1, 2, 3, 4], n_trials // 4)
    shuffle(start_col)
    data[:, 0] = start_col

    for col in range(1, n_reps):
        combo_counts = {combo: combo_repeats for combo in val_combos}
        new_col = []
        for val in data[:, col-1]:
            combos = [c for c, count in combo_counts.items() if c[0] == val and count > 0]
            chosen_combo = choice(len(combos))
            new_val = combos[chosen_combo][1]
            new_col.append(new_val)
            combo_counts[combos[chosen_combo]] -= 1

        data[:, col] = new_col

    return data.tolist()


def radGrid(stim_radius, n_stims):
    pOff = (2 * stim_radius) / sqrt(3)
    rList = [15]
    
    while sum(rList) <= n_stims:
        rList.append(rList[-1] + 6)
    nList = rList[:-1]
    nList.append(n_stims - sum(nList))
    radGrid = []

    for index, val in enumerate(nList):
        n = rList[index]
        cRad = pOff * (n / 3)
        degs = np.array([(i * (360 / val) + 45) % 360 for i in range(val)])
        cords = np.column_stack((cRad * cos(deg2rad(degs)), cRad * sin(deg2rad(degs))))
        radGrid.extend(np.round(cords, 3))

    return radGrid


def get_item(aDict, item):
    for key, value in aDict.items():
        if item == value:
            return key
        elif item == key:
            return value


def waitSpace(kb, trig, win, win2):
    keys = kb.waitKeys(keyList=['escape', 'space'])
    if keys[0] == 'escape':
        trig.close()
        win.close()
        win2.close()
        core.quit()


def closeWin(kb, trig, win, win2):
    keys = kb.getKeys(['escape'])
    if len(keys) != 0:
        trig.close()
        win.close()
        win2.close()
        core.quit()