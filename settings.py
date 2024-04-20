# structure settings
n_prac_trials   = 1                 # can be repeat, or can be minimum + repeat
n_trials        = 12                # may need to be from subset for counterbalancing
n_blocks        = 20                # may need to be from subset for counterbalancing
practice_cutoff = 75                # percentile accurate to pass / not repeat
n_reps          = 4                 # the number of stimulus display repetitions per trial
fix_1_ms        = 50                # durration of fixation 1 in ms
fix_2_ms        = 50                # durration of fixation 2 in ms
isi_ms          = 100               # durration of inter-stimulus interval
isi_jit_ms      = [_ for _ in 
                   range(10,55,5)]  # range of jitters +/- to be added to isi
resp_ms         = 1500              # durration of the response window
iti_ms          = 1000              # duration of the inter-trial interval
n_rings         = 2                 # number of concentric rings of stimuli
n_stim_r1       = 10                # number of stimuli in ring 1
n_stim_r2       = 20                # number of stimuli in ring 2
n_distractors   = [_ for _ in range(1,8)]      
                                    # number of distractors
n_xtargs        = [_ for _ in range(1,8)]      
                                    # number of non-targets

# stimuli settings
shape_dva       = 1                 # size of the stimuli in degrees visual angle
r1_radius       = 5                 # radius of r1 in degrees visual angle
r2_radius       = 10                # radius of r2 in degrees visual angle
stim_radius     = 2                 # radius of stimulus frame (for scaling object sizes)
t_r1_prop       = 0.5               # proportion of trials where target is in r1
t_r2_prop       = 0.5               # proportion of trials where target is in r2
stim_set        = ['shapes',        # which set of stimuli to use
                    'lines']        

# colours
targ_col        = [0,0,0]           # colour(s) of the target object(s)
dist_col        = [0,0,0]           # colour(s) of the distractor object(s)
xtarg_col       = [0,0,0]           # colour(s) of the non-target item(s)
fix_col         = [0,0,0]           # color of fixation cross
bg_col          = [0,0,0]           # screen background colour
green           = [0,255,0]         # e.g., positive positive colour
red             = [255,0,0]         # e.g., negative feedback colour
white           = [255,255,255]     # e.g., text colour
black           = [0,0,0]           # e.g., background colour

# constants - do not change
sec_ms          = 1000              # setting for 1 second (usefull for instructions, delay periods)

# create a colour set (can be hex or RGB, I prefer hex)
color_set = {'red'      : '#FF1010',
             'green'    : '#00FF00',
             'blue'     : '#0000FF',
             'gold'     : '#FFD700',
             'indigo'   : '#4B0082',
             'purple'   : '#800080',
             'orange'   : '#FF6500',
             'pink'     : '#FF00CB',
             'white'    : '#DDDDDD',}
