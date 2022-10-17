﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Sep 29 11:18:28 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'psychopy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'group': ['A', 'B']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/danizhang/Desktop/Miscellaneous (Organized)/Spring 2022/Psych 397-1/psychopy_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1728, 1117], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
key_resp = keyboard.Keyboard()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='This particular experiment aims to measure each participant’s level of prosociality. It is part of a broader experiment designed to increase levels of prosociality through mindfulness meditation interventions.\n\nPress space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Set experiment start values for variable component fontsize
fontsize = 0.05
fontsizeContainer = []

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Consent"
ConsentClock = core.Clock()
key_resp_2 = keyboard.Keyboard()
ConsentText = visual.TextStim(win=win, name='ConsentText',
    text='Your participation in this study is completely voluntary. Your responses will be kept anonymous and confidential. Additionally, any personal information you submit will be kept private as well. In this particular experiment, you will be asked to determine whether a presented image represents an animate or inanimate entity. This research involves no more risk than encountered in everyday life. There is also no direct benefit for you to participate in this study, beyond the compensation agreed upon with the lab. Please note whether you consent to participate in this survey down below.\n\nPress space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "GeneralInstructions"
GeneralInstructionsClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
InstructionText = visual.TextStim(win=win, name='InstructionText',
    text='This experiment involves the use of image stimuli and a joystick. You will be presented with an image that will be either animate or inanimate, but not both. Please use your best judgment if this distinction seems unclear for any of the images. You will need to either push or pull the joystick, depending on whether the image is animate or inanimate. \n\nPress space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "GeneralInstructions2"
GeneralInstructions2Clock = core.Clock()
key_resp_8 = keyboard.Keyboard()
text_7 = visual.TextStim(win=win, name='text_7',
    text='You will be instructed whether to push for animate or pull for animate (along with the instructions for inanimate images, which will be opposite that for animate images) before each phase of the experiment. There will be two phases of the experiment, with each phase containing a total of 90 images–10 of which will be practice images presented before the data collection begins. Please push or pull as quickly as possible, as your reaction time will be measured.\n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeInstructions1"
PracticeInstructions1Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Next, you will begin the practice trial for this phase. Please push the joystick if you believe the image to be animate, or pull the joystick if you believe the image to be inanimate. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "ImageStudyTrial"
ImageStudyTrialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TestInstructions1"
TestInstructions1Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='You will now be presented with the official images that will be used for data collection in this phase. Please inform the researcher if you have any questions thus far, and note that there will be a slight break after every 20 images.\n\nPress space bar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "ImageTests1"
ImageTests1Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Rest"
RestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Rest period. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ImageTest2"
ImageTest2Clock = core.Clock()
key_resp_10 = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Rest"
RestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Rest period. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ImageTest3"
ImageTest3Clock = core.Clock()
key_resp_11 = keyboard.Keyboard()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Rest"
RestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Rest period. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ImageTest4"
ImageTest4Clock = core.Clock()
key_resp_12 = keyboard.Keyboard()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeInstructions2"
PracticeInstructions2Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Next, you will begin the practice trial for this phase. Please push the joystick if you believe the image to be inanimate, or pull the joystick if you believe the image to be animate. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "StudyTrial2"
StudyTrial2Clock = core.Clock()
key_resp_14 = keyboard.Keyboard()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TestInstructions2"
TestInstructions2Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='You will now be presented with the official images that will be used for data collection in this phase. Please inform the researcher if you have any questions thus far, and note that there will be a slight break after every 20 images.\n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "ImageTest5"
ImageTest5Clock = core.Clock()
key_resp_16 = keyboard.Keyboard()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Rest"
RestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Rest period. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ImageTest6"
ImageTest6Clock = core.Clock()
key_resp_17 = keyboard.Keyboard()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Rest"
RestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Rest period. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ImageTest7"
ImageTest7Clock = core.Clock()
key_resp_18 = keyboard.Keyboard()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Rest"
RestClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Rest period. \n\nPress space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "ImageTest8"
ImageTest8Clock = core.Clock()
key_resp_19 = keyboard.Keyboard()
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "End_Experiment"
End_ExperimentClock = core.Clock()
key_resp_20 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='The experiment has now ended. \n \n As noted earlier, this particular experiment aims to measure each participant’s level of prosociality. That was done by measuring the reaction time difference between how long it takes for each participant to push for certain images and to pull for certain other images, as organized by animate/inanimate status and valence. It is part of a broader experiment designed to increase levels of prosociality through mindfulness meditation interventions.\n\nThank you for being part of the experiment, and please feel free to contact the researcher if you have any further questions.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [key_resp, WelcomeText]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *WelcomeText* updates
    if WelcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.tStart = t  # local t and not account for scr refresh
        WelcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        WelcomeText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [text_2]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "Consent"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
ConsentComponents = [key_resp_2, ConsentText]
for thisComponent in ConsentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ConsentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Consent"-------
while continueRoutine:
    # get current time
    t = ConsentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ConsentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ConsentText* updates
    if ConsentText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConsentText.frameNStart = frameN  # exact frame index
        ConsentText.tStart = t  # local t and not account for scr refresh
        ConsentText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConsentText, 'tStartRefresh')  # time at next scr refresh
        ConsentText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ConsentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Consent"-------
for thisComponent in ConsentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('ConsentText.started', ConsentText.tStartRefresh)
thisExp.addData('ConsentText.stopped', ConsentText.tStopRefresh)
# the Routine "Consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [text_2]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "GeneralInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
GeneralInstructionsComponents = [key_resp_3, InstructionText]
for thisComponent in GeneralInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GeneralInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GeneralInstructions"-------
while continueRoutine:
    # get current time
    t = GeneralInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GeneralInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *InstructionText* updates
    if InstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionText.frameNStart = frameN  # exact frame index
        InstructionText.tStart = t  # local t and not account for scr refresh
        InstructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionText, 'tStartRefresh')  # time at next scr refresh
        InstructionText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GeneralInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GeneralInstructions"-------
for thisComponent in GeneralInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('InstructionText.started', InstructionText.tStartRefresh)
thisExp.addData('InstructionText.stopped', InstructionText.tStopRefresh)
# the Routine "GeneralInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [text_2]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "GeneralInstructions2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
GeneralInstructions2Components = [key_resp_8, text_7]
for thisComponent in GeneralInstructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GeneralInstructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GeneralInstructions2"-------
while continueRoutine:
    # get current time
    t = GeneralInstructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GeneralInstructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GeneralInstructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GeneralInstructions2"-------
for thisComponent in GeneralInstructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "GeneralInstructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [text_2]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
controlTaskOrder = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions'+expInfo['group']+'.xlsx'),
    seed=None, name='controlTaskOrder')
thisExp.addLoop(controlTaskOrder)  # add the loop to the experiment
thisControlTaskOrder = controlTaskOrder.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisControlTaskOrder.rgb)
if thisControlTaskOrder != None:
    for paramName in thisControlTaskOrder:
        exec('{} = thisControlTaskOrder[paramName]'.format(paramName))

for thisControlTaskOrder in controlTaskOrder:
    currentLoop = controlTaskOrder
    # abbreviate parameter names if possible (e.g. rgb = thisControlTaskOrder.rgb)
    if thisControlTaskOrder != None:
        for paramName in thisControlTaskOrder:
            exec('{} = thisControlTaskOrder[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    part1 = data.TrialHandler(nReps=nRepsTask1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='part1')
    thisExp.addLoop(part1)  # add the loop to the experiment
    thisPart1 = part1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPart1.rgb)
    if thisPart1 != None:
        for paramName in thisPart1:
            exec('{} = thisPart1[paramName]'.format(paramName))
    
    for thisPart1 in part1:
        currentLoop = part1
        # abbreviate parameter names if possible (e.g. rgb = thisPart1.rgb)
        if thisPart1 != None:
            for paramName in thisPart1:
                exec('{} = thisPart1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "PracticeInstructions1"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        PracticeInstructions1Components = [text_4, key_resp_4]
        for thisComponent in PracticeInstructions1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeInstructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeInstructions1"-------
        while continueRoutine:
            # get current time
            t = PracticeInstructions1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeInstructions1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeInstructions1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeInstructions1"-------
        for thisComponent in PracticeInstructions1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part1.addData('text_4.started', text_4.tStartRefresh)
        part1.addData('text_4.stopped', text_4.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        part1.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            part1.addData('key_resp_4.rt', key_resp_4.rt)
        part1.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        part1.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        # the Routine "PracticeInstructions1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsStudyImages = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImagePractices1.xlsx', selection='0:10'),
            seed=None, name='trialsStudyImages')
        thisExp.addLoop(trialsStudyImages)  # add the loop to the experiment
        thisTrialsStudyImage = trialsStudyImages.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudyImage.rgb)
        if thisTrialsStudyImage != None:
            for paramName in thisTrialsStudyImage:
                exec('{} = thisTrialsStudyImage[paramName]'.format(paramName))
        
        for thisTrialsStudyImage in trialsStudyImages:
            currentLoop = trialsStudyImages
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudyImage.rgb)
            if thisTrialsStudyImage != None:
                for paramName in thisTrialsStudyImage:
                    exec('{} = thisTrialsStudyImage[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageStudyTrial"-------
            continueRoutine = True
            # update component parameters for each repeat
            image.setImage(ImageFile)
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            # keep track of which components have finished
            ImageStudyTrialComponents = [image, key_resp_7]
            for thisComponent in ImageStudyTrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageStudyTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageStudyTrial"-------
            while continueRoutine:
                # get current time
                t = ImageStudyTrialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageStudyTrialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    image.setAutoDraw(True)
                
                # *key_resp_7* updates
                waitOnFlip = False
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                        key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_7.keys == str(AnimateInanimate)) or (key_resp_7.keys == AnimateInanimate):
                            key_resp_7.corr = 1
                        else:
                            key_resp_7.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageStudyTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageStudyTrial"-------
            for thisComponent in ImageStudyTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsStudyImages.addData('image.started', image.tStartRefresh)
            trialsStudyImages.addData('image.stopped', image.tStopRefresh)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_7.corr = 1;  # correct non-response
                else:
                   key_resp_7.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsStudyImages (TrialHandler)
            trialsStudyImages.addData('key_resp_7.keys',key_resp_7.keys)
            trialsStudyImages.addData('key_resp_7.corr', key_resp_7.corr)
            if key_resp_7.keys != None:  # we had a response
                trialsStudyImages.addData('key_resp_7.rt', key_resp_7.rt)
            trialsStudyImages.addData('key_resp_7.started', key_resp_7.tStartRefresh)
            trialsStudyImages.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
            # the Routine "ImageStudyTrial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsStudyImages.addData('text_2.started', text_2.tStartRefresh)
            trialsStudyImages.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsStudyImages'
        
        
        # ------Prepare to start Routine "TestInstructions1"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # keep track of which components have finished
        TestInstructions1Components = [text_6, key_resp_6]
        for thisComponent in TestInstructions1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TestInstructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TestInstructions1"-------
        while continueRoutine:
            # get current time
            t = TestInstructions1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TestInstructions1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            
            # *key_resp_6* updates
            waitOnFlip = False
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TestInstructions1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TestInstructions1"-------
        for thisComponent in TestInstructions1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part1.addData('text_6.started', text_6.tStartRefresh)
        part1.addData('text_6.stopped', text_6.tStopRefresh)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        part1.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            part1.addData('key_resp_6.rt', key_resp_6.rt)
        part1.addData('key_resp_6.started', key_resp_6.tStartRefresh)
        part1.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
        # the Routine "TestInstructions1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTest1_1 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests1.xlsx', selection='0:10'),
            seed=None, name='trialsTest1_1')
        thisExp.addLoop(trialsTest1_1)  # add the loop to the experiment
        thisTrialsTest1_1 = trialsTest1_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_1.rgb)
        if thisTrialsTest1_1 != None:
            for paramName in thisTrialsTest1_1:
                exec('{} = thisTrialsTest1_1[paramName]'.format(paramName))
        
        for thisTrialsTest1_1 in trialsTest1_1:
            currentLoop = trialsTest1_1
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_1.rgb)
            if thisTrialsTest1_1 != None:
                for paramName in thisTrialsTest1_1:
                    exec('{} = thisTrialsTest1_1[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTests1"-------
            continueRoutine = True
            # update component parameters for each repeat
            image_2.setImage(ImageFile)
            key_resp_9.keys = []
            key_resp_9.rt = []
            _key_resp_9_allKeys = []
            # keep track of which components have finished
            ImageTests1Components = [image_2, key_resp_9]
            for thisComponent in ImageTests1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTests1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTests1"-------
            while continueRoutine:
                # get current time
                t = ImageTests1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTests1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_2* updates
                if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.tStart = t  # local t and not account for scr refresh
                    image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                    image_2.setAutoDraw(True)
                
                # *key_resp_9* updates
                waitOnFlip = False
                if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_9.frameNStart = frameN  # exact frame index
                    key_resp_9.tStart = t  # local t and not account for scr refresh
                    key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                    key_resp_9.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_9.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_9.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_9_allKeys.extend(theseKeys)
                    if len(_key_resp_9_allKeys):
                        key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                        key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_9.keys == str(AnimateInanimate)) or (key_resp_9.keys == AnimateInanimate):
                            key_resp_9.corr = 1
                        else:
                            key_resp_9.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTests1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTests1"-------
            for thisComponent in ImageTests1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTest1_1.addData('image_2.started', image_2.tStartRefresh)
            trialsTest1_1.addData('image_2.stopped', image_2.tStopRefresh)
            # check responses
            if key_resp_9.keys in ['', [], None]:  # No response was made
                key_resp_9.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_9.corr = 1;  # correct non-response
                else:
                   key_resp_9.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTest1_1 (TrialHandler)
            trialsTest1_1.addData('key_resp_9.keys',key_resp_9.keys)
            trialsTest1_1.addData('key_resp_9.corr', key_resp_9.corr)
            if key_resp_9.keys != None:  # we had a response
                trialsTest1_1.addData('key_resp_9.rt', key_resp_9.rt)
            trialsTest1_1.addData('key_resp_9.started', key_resp_9.tStartRefresh)
            trialsTest1_1.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
            # the Routine "ImageTests1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTest1_1.addData('text_2.started', text_2.tStartRefresh)
            trialsTest1_1.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTest1_1'
        
        
        # ------Prepare to start Routine "Rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        RestComponents = [text_5, key_resp_5]
        for thisComponent in RestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Rest"-------
        while continueRoutine:
            # get current time
            t = RestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part1.addData('text_5.started', text_5.tStartRefresh)
        part1.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        part1.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            part1.addData('key_resp_5.rt', key_resp_5.rt)
        part1.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        part1.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTest1_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests2.xlsx', selection='0:10'),
            seed=None, name='trialsTest1_2')
        thisExp.addLoop(trialsTest1_2)  # add the loop to the experiment
        thisTrialsTest1_2 = trialsTest1_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_2.rgb)
        if thisTrialsTest1_2 != None:
            for paramName in thisTrialsTest1_2:
                exec('{} = thisTrialsTest1_2[paramName]'.format(paramName))
        
        for thisTrialsTest1_2 in trialsTest1_2:
            currentLoop = trialsTest1_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_2.rgb)
            if thisTrialsTest1_2 != None:
                for paramName in thisTrialsTest1_2:
                    exec('{} = thisTrialsTest1_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTest2"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_10.keys = []
            key_resp_10.rt = []
            _key_resp_10_allKeys = []
            image_3.setImage(ImageFile)
            # keep track of which components have finished
            ImageTest2Components = [key_resp_10, image_3]
            for thisComponent in ImageTest2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTest2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTest2"-------
            while continueRoutine:
                # get current time
                t = ImageTest2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTest2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_10* updates
                waitOnFlip = False
                if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_10.frameNStart = frameN  # exact frame index
                    key_resp_10.tStart = t  # local t and not account for scr refresh
                    key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                    key_resp_10.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_10.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_10.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_10_allKeys.extend(theseKeys)
                    if len(_key_resp_10_allKeys):
                        key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                        key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_10.keys == str(AnimateInanimate)) or (key_resp_10.keys == AnimateInanimate):
                            key_resp_10.corr = 1
                        else:
                            key_resp_10.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_3* updates
                if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_3.frameNStart = frameN  # exact frame index
                    image_3.tStart = t  # local t and not account for scr refresh
                    image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTest2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTest2"-------
            for thisComponent in ImageTest2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_10.keys in ['', [], None]:  # No response was made
                key_resp_10.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_10.corr = 1;  # correct non-response
                else:
                   key_resp_10.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTest1_2 (TrialHandler)
            trialsTest1_2.addData('key_resp_10.keys',key_resp_10.keys)
            trialsTest1_2.addData('key_resp_10.corr', key_resp_10.corr)
            if key_resp_10.keys != None:  # we had a response
                trialsTest1_2.addData('key_resp_10.rt', key_resp_10.rt)
            trialsTest1_2.addData('key_resp_10.started', key_resp_10.tStartRefresh)
            trialsTest1_2.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
            trialsTest1_2.addData('image_3.started', image_3.tStartRefresh)
            trialsTest1_2.addData('image_3.stopped', image_3.tStopRefresh)
            # the Routine "ImageTest2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTest1_2.addData('text_2.started', text_2.tStartRefresh)
            trialsTest1_2.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTest1_2'
        
        
        # ------Prepare to start Routine "Rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        RestComponents = [text_5, key_resp_5]
        for thisComponent in RestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Rest"-------
        while continueRoutine:
            # get current time
            t = RestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part1.addData('text_5.started', text_5.tStartRefresh)
        part1.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        part1.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            part1.addData('key_resp_5.rt', key_resp_5.rt)
        part1.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        part1.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTest1_3 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests3.xlsx', selection='0:10'),
            seed=None, name='trialsTest1_3')
        thisExp.addLoop(trialsTest1_3)  # add the loop to the experiment
        thisTrialsTest1_3 = trialsTest1_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_3.rgb)
        if thisTrialsTest1_3 != None:
            for paramName in thisTrialsTest1_3:
                exec('{} = thisTrialsTest1_3[paramName]'.format(paramName))
        
        for thisTrialsTest1_3 in trialsTest1_3:
            currentLoop = trialsTest1_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_3.rgb)
            if thisTrialsTest1_3 != None:
                for paramName in thisTrialsTest1_3:
                    exec('{} = thisTrialsTest1_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTest3"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_11.keys = []
            key_resp_11.rt = []
            _key_resp_11_allKeys = []
            image_4.setImage(ImageFile)
            # keep track of which components have finished
            ImageTest3Components = [key_resp_11, image_4]
            for thisComponent in ImageTest3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTest3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTest3"-------
            while continueRoutine:
                # get current time
                t = ImageTest3Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTest3Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_11* updates
                waitOnFlip = False
                if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_11.frameNStart = frameN  # exact frame index
                    key_resp_11.tStart = t  # local t and not account for scr refresh
                    key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                    key_resp_11.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_11.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_11.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_11_allKeys.extend(theseKeys)
                    if len(_key_resp_11_allKeys):
                        key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                        key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_11.keys == str(AnimateInanimate)) or (key_resp_11.keys == AnimateInanimate):
                            key_resp_11.corr = 1
                        else:
                            key_resp_11.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_4* updates
                if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_4.frameNStart = frameN  # exact frame index
                    image_4.tStart = t  # local t and not account for scr refresh
                    image_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                    image_4.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTest3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTest3"-------
            for thisComponent in ImageTest3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_11.keys in ['', [], None]:  # No response was made
                key_resp_11.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_11.corr = 1;  # correct non-response
                else:
                   key_resp_11.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTest1_3 (TrialHandler)
            trialsTest1_3.addData('key_resp_11.keys',key_resp_11.keys)
            trialsTest1_3.addData('key_resp_11.corr', key_resp_11.corr)
            if key_resp_11.keys != None:  # we had a response
                trialsTest1_3.addData('key_resp_11.rt', key_resp_11.rt)
            trialsTest1_3.addData('key_resp_11.started', key_resp_11.tStartRefresh)
            trialsTest1_3.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
            trialsTest1_3.addData('image_4.started', image_4.tStartRefresh)
            trialsTest1_3.addData('image_4.stopped', image_4.tStopRefresh)
            # the Routine "ImageTest3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTest1_3.addData('text_2.started', text_2.tStartRefresh)
            trialsTest1_3.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTest1_3'
        
        
        # ------Prepare to start Routine "Rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        RestComponents = [text_5, key_resp_5]
        for thisComponent in RestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Rest"-------
        while continueRoutine:
            # get current time
            t = RestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part1.addData('text_5.started', text_5.tStartRefresh)
        part1.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        part1.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            part1.addData('key_resp_5.rt', key_resp_5.rt)
        part1.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        part1.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTest1_4 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests4.xlsx', selection='0:10'),
            seed=None, name='trialsTest1_4')
        thisExp.addLoop(trialsTest1_4)  # add the loop to the experiment
        thisTrialsTest1_4 = trialsTest1_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_4.rgb)
        if thisTrialsTest1_4 != None:
            for paramName in thisTrialsTest1_4:
                exec('{} = thisTrialsTest1_4[paramName]'.format(paramName))
        
        for thisTrialsTest1_4 in trialsTest1_4:
            currentLoop = trialsTest1_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest1_4.rgb)
            if thisTrialsTest1_4 != None:
                for paramName in thisTrialsTest1_4:
                    exec('{} = thisTrialsTest1_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTest4"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_12.keys = []
            key_resp_12.rt = []
            _key_resp_12_allKeys = []
            image_5.setImage(ImageFile)
            # keep track of which components have finished
            ImageTest4Components = [key_resp_12, image_5]
            for thisComponent in ImageTest4Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTest4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTest4"-------
            while continueRoutine:
                # get current time
                t = ImageTest4Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTest4Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_12* updates
                waitOnFlip = False
                if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_12.frameNStart = frameN  # exact frame index
                    key_resp_12.tStart = t  # local t and not account for scr refresh
                    key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                    key_resp_12.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_12.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_12.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_12_allKeys.extend(theseKeys)
                    if len(_key_resp_12_allKeys):
                        key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                        key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_12.keys == str(AnimateInanimate)) or (key_resp_12.keys == AnimateInanimate):
                            key_resp_12.corr = 1
                        else:
                            key_resp_12.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_5* updates
                if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_5.frameNStart = frameN  # exact frame index
                    image_5.tStart = t  # local t and not account for scr refresh
                    image_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                    image_5.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTest4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTest4"-------
            for thisComponent in ImageTest4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_12.keys in ['', [], None]:  # No response was made
                key_resp_12.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_12.corr = 1;  # correct non-response
                else:
                   key_resp_12.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTest1_4 (TrialHandler)
            trialsTest1_4.addData('key_resp_12.keys',key_resp_12.keys)
            trialsTest1_4.addData('key_resp_12.corr', key_resp_12.corr)
            if key_resp_12.keys != None:  # we had a response
                trialsTest1_4.addData('key_resp_12.rt', key_resp_12.rt)
            trialsTest1_4.addData('key_resp_12.started', key_resp_12.tStartRefresh)
            trialsTest1_4.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
            trialsTest1_4.addData('image_5.started', image_5.tStartRefresh)
            trialsTest1_4.addData('image_5.stopped', image_5.tStopRefresh)
            # the Routine "ImageTest4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTest1_4.addData('text_2.started', text_2.tStartRefresh)
            trialsTest1_4.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTest1_4'
        
        thisExp.nextEntry()
        
    # completed nRepsTask1 repeats of 'part1'
    
    
    # set up handler to look after randomisation of conditions etc
    part2 = data.TrialHandler(nReps=nRepsTask2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='part2')
    thisExp.addLoop(part2)  # add the loop to the experiment
    thisPart2 = part2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPart2.rgb)
    if thisPart2 != None:
        for paramName in thisPart2:
            exec('{} = thisPart2[paramName]'.format(paramName))
    
    for thisPart2 in part2:
        currentLoop = part2
        # abbreviate parameter names if possible (e.g. rgb = thisPart2.rgb)
        if thisPart2 != None:
            for paramName in thisPart2:
                exec('{} = thisPart2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "PracticeInstructions2"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_13.keys = []
        key_resp_13.rt = []
        _key_resp_13_allKeys = []
        # keep track of which components have finished
        PracticeInstructions2Components = [text_8, key_resp_13]
        for thisComponent in PracticeInstructions2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeInstructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeInstructions2"-------
        while continueRoutine:
            # get current time
            t = PracticeInstructions2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeInstructions2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            
            # *key_resp_13* updates
            waitOnFlip = False
            if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_13.frameNStart = frameN  # exact frame index
                key_resp_13.tStart = t  # local t and not account for scr refresh
                key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                key_resp_13.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_13.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_13_allKeys.extend(theseKeys)
                if len(_key_resp_13_allKeys):
                    key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                    key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeInstructions2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeInstructions2"-------
        for thisComponent in PracticeInstructions2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part2.addData('text_8.started', text_8.tStartRefresh)
        part2.addData('text_8.stopped', text_8.tStopRefresh)
        # check responses
        if key_resp_13.keys in ['', [], None]:  # No response was made
            key_resp_13.keys = None
        part2.addData('key_resp_13.keys',key_resp_13.keys)
        if key_resp_13.keys != None:  # we had a response
            part2.addData('key_resp_13.rt', key_resp_13.rt)
        part2.addData('key_resp_13.started', key_resp_13.tStartRefresh)
        part2.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
        # the Routine "PracticeInstructions2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsStudyImages2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImagePractices2_inherently_reversed.xlsx', selection='0:2'),
            seed=None, name='trialsStudyImages2')
        thisExp.addLoop(trialsStudyImages2)  # add the loop to the experiment
        thisTrialsStudyImages2 = trialsStudyImages2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudyImages2.rgb)
        if thisTrialsStudyImages2 != None:
            for paramName in thisTrialsStudyImages2:
                exec('{} = thisTrialsStudyImages2[paramName]'.format(paramName))
        
        for thisTrialsStudyImages2 in trialsStudyImages2:
            currentLoop = trialsStudyImages2
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudyImages2.rgb)
            if thisTrialsStudyImages2 != None:
                for paramName in thisTrialsStudyImages2:
                    exec('{} = thisTrialsStudyImages2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "StudyTrial2"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_14.keys = []
            key_resp_14.rt = []
            _key_resp_14_allKeys = []
            image_7.setImage(ImageFile)
            # keep track of which components have finished
            StudyTrial2Components = [key_resp_14, image_7]
            for thisComponent in StudyTrial2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            StudyTrial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "StudyTrial2"-------
            while continueRoutine:
                # get current time
                t = StudyTrial2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=StudyTrial2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_14* updates
                waitOnFlip = False
                if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_14.frameNStart = frameN  # exact frame index
                    key_resp_14.tStart = t  # local t and not account for scr refresh
                    key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                    key_resp_14.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_14.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_14.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_14_allKeys.extend(theseKeys)
                    if len(_key_resp_14_allKeys):
                        key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                        key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_7* updates
                if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.tStart = t  # local t and not account for scr refresh
                    image_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                    image_7.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in StudyTrial2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "StudyTrial2"-------
            for thisComponent in StudyTrial2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_14.keys in ['', [], None]:  # No response was made
                key_resp_14.keys = None
            trialsStudyImages2.addData('key_resp_14.keys',key_resp_14.keys)
            if key_resp_14.keys != None:  # we had a response
                trialsStudyImages2.addData('key_resp_14.rt', key_resp_14.rt)
            trialsStudyImages2.addData('key_resp_14.started', key_resp_14.tStartRefresh)
            trialsStudyImages2.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
            trialsStudyImages2.addData('image_7.started', image_7.tStartRefresh)
            trialsStudyImages2.addData('image_7.stopped', image_7.tStopRefresh)
            # the Routine "StudyTrial2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsStudyImages2.addData('text_2.started', text_2.tStartRefresh)
            trialsStudyImages2.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsStudyImages2'
        
        
        # ------Prepare to start Routine "TestInstructions2"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_15.keys = []
        key_resp_15.rt = []
        _key_resp_15_allKeys = []
        # keep track of which components have finished
        TestInstructions2Components = [text_9, key_resp_15]
        for thisComponent in TestInstructions2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TestInstructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TestInstructions2"-------
        while continueRoutine:
            # get current time
            t = TestInstructions2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TestInstructions2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                text_9.setAutoDraw(True)
            
            # *key_resp_15* updates
            waitOnFlip = False
            if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_15.frameNStart = frameN  # exact frame index
                key_resp_15.tStart = t  # local t and not account for scr refresh
                key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
                key_resp_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_15.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_15_allKeys.extend(theseKeys)
                if len(_key_resp_15_allKeys):
                    key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                    key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TestInstructions2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TestInstructions2"-------
        for thisComponent in TestInstructions2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part2.addData('text_9.started', text_9.tStartRefresh)
        part2.addData('text_9.stopped', text_9.tStopRefresh)
        # check responses
        if key_resp_15.keys in ['', [], None]:  # No response was made
            key_resp_15.keys = None
        part2.addData('key_resp_15.keys',key_resp_15.keys)
        if key_resp_15.keys != None:  # we had a response
            part2.addData('key_resp_15.rt', key_resp_15.rt)
        part2.addData('key_resp_15.started', key_resp_15.tStartRefresh)
        part2.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
        # the Routine "TestInstructions2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTestImages2_1 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests1_Reversed.xlsx', selection='0:2'),
            seed=None, name='trialsTestImages2_1')
        thisExp.addLoop(trialsTestImages2_1)  # add the loop to the experiment
        thisTrialsTestImages2_1 = trialsTestImages2_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_1.rgb)
        if thisTrialsTestImages2_1 != None:
            for paramName in thisTrialsTestImages2_1:
                exec('{} = thisTrialsTestImages2_1[paramName]'.format(paramName))
        
        for thisTrialsTestImages2_1 in trialsTestImages2_1:
            currentLoop = trialsTestImages2_1
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_1.rgb)
            if thisTrialsTestImages2_1 != None:
                for paramName in thisTrialsTestImages2_1:
                    exec('{} = thisTrialsTestImages2_1[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTest5"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_16.keys = []
            key_resp_16.rt = []
            _key_resp_16_allKeys = []
            image_6.setImage(ImageFile)
            # keep track of which components have finished
            ImageTest5Components = [key_resp_16, image_6]
            for thisComponent in ImageTest5Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTest5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTest5"-------
            while continueRoutine:
                # get current time
                t = ImageTest5Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTest5Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_16* updates
                waitOnFlip = False
                if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_16.frameNStart = frameN  # exact frame index
                    key_resp_16.tStart = t  # local t and not account for scr refresh
                    key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
                    key_resp_16.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_16.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_16.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_16_allKeys.extend(theseKeys)
                    if len(_key_resp_16_allKeys):
                        key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                        key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_16.keys == str(AnimateInanimate)) or (key_resp_16.keys == AnimateInanimate):
                            key_resp_16.corr = 1
                        else:
                            key_resp_16.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_6* updates
                if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_6.frameNStart = frameN  # exact frame index
                    image_6.tStart = t  # local t and not account for scr refresh
                    image_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                    image_6.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTest5Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTest5"-------
            for thisComponent in ImageTest5Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_16.keys in ['', [], None]:  # No response was made
                key_resp_16.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_16.corr = 1;  # correct non-response
                else:
                   key_resp_16.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTestImages2_1 (TrialHandler)
            trialsTestImages2_1.addData('key_resp_16.keys',key_resp_16.keys)
            trialsTestImages2_1.addData('key_resp_16.corr', key_resp_16.corr)
            if key_resp_16.keys != None:  # we had a response
                trialsTestImages2_1.addData('key_resp_16.rt', key_resp_16.rt)
            trialsTestImages2_1.addData('key_resp_16.started', key_resp_16.tStartRefresh)
            trialsTestImages2_1.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
            trialsTestImages2_1.addData('image_6.started', image_6.tStartRefresh)
            trialsTestImages2_1.addData('image_6.stopped', image_6.tStopRefresh)
            # the Routine "ImageTest5" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTestImages2_1.addData('text_2.started', text_2.tStartRefresh)
            trialsTestImages2_1.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTestImages2_1'
        
        
        # ------Prepare to start Routine "Rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        RestComponents = [text_5, key_resp_5]
        for thisComponent in RestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Rest"-------
        while continueRoutine:
            # get current time
            t = RestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part2.addData('text_5.started', text_5.tStartRefresh)
        part2.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        part2.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            part2.addData('key_resp_5.rt', key_resp_5.rt)
        part2.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        part2.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTestImages2_2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests2_Reversed.xlsx', selection='0:2'),
            seed=None, name='trialsTestImages2_2')
        thisExp.addLoop(trialsTestImages2_2)  # add the loop to the experiment
        thisTrialsTestImages2_2 = trialsTestImages2_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_2.rgb)
        if thisTrialsTestImages2_2 != None:
            for paramName in thisTrialsTestImages2_2:
                exec('{} = thisTrialsTestImages2_2[paramName]'.format(paramName))
        
        for thisTrialsTestImages2_2 in trialsTestImages2_2:
            currentLoop = trialsTestImages2_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_2.rgb)
            if thisTrialsTestImages2_2 != None:
                for paramName in thisTrialsTestImages2_2:
                    exec('{} = thisTrialsTestImages2_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTest6"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_17.keys = []
            key_resp_17.rt = []
            _key_resp_17_allKeys = []
            image_8.setImage(ImageFile)
            # keep track of which components have finished
            ImageTest6Components = [key_resp_17, image_8]
            for thisComponent in ImageTest6Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTest6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTest6"-------
            while continueRoutine:
                # get current time
                t = ImageTest6Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTest6Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_17* updates
                waitOnFlip = False
                if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_17.frameNStart = frameN  # exact frame index
                    key_resp_17.tStart = t  # local t and not account for scr refresh
                    key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
                    key_resp_17.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_17.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_17.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_17_allKeys.extend(theseKeys)
                    if len(_key_resp_17_allKeys):
                        key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                        key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_17.keys == str(AnimateInanimate)) or (key_resp_17.keys == AnimateInanimate):
                            key_resp_17.corr = 1
                        else:
                            key_resp_17.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_8* updates
                if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_8.frameNStart = frameN  # exact frame index
                    image_8.tStart = t  # local t and not account for scr refresh
                    image_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                    image_8.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTest6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTest6"-------
            for thisComponent in ImageTest6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_17.keys in ['', [], None]:  # No response was made
                key_resp_17.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_17.corr = 1;  # correct non-response
                else:
                   key_resp_17.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTestImages2_2 (TrialHandler)
            trialsTestImages2_2.addData('key_resp_17.keys',key_resp_17.keys)
            trialsTestImages2_2.addData('key_resp_17.corr', key_resp_17.corr)
            if key_resp_17.keys != None:  # we had a response
                trialsTestImages2_2.addData('key_resp_17.rt', key_resp_17.rt)
            trialsTestImages2_2.addData('key_resp_17.started', key_resp_17.tStartRefresh)
            trialsTestImages2_2.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
            trialsTestImages2_2.addData('image_8.started', image_8.tStartRefresh)
            trialsTestImages2_2.addData('image_8.stopped', image_8.tStopRefresh)
            # the Routine "ImageTest6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTestImages2_2.addData('text_2.started', text_2.tStartRefresh)
            trialsTestImages2_2.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTestImages2_2'
        
        
        # ------Prepare to start Routine "Rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        RestComponents = [text_5, key_resp_5]
        for thisComponent in RestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Rest"-------
        while continueRoutine:
            # get current time
            t = RestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part2.addData('text_5.started', text_5.tStartRefresh)
        part2.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        part2.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            part2.addData('key_resp_5.rt', key_resp_5.rt)
        part2.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        part2.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTestImages2_3 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests3_Reversed.xlsx', selection='0:2'),
            seed=None, name='trialsTestImages2_3')
        thisExp.addLoop(trialsTestImages2_3)  # add the loop to the experiment
        thisTrialsTestImages2_3 = trialsTestImages2_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_3.rgb)
        if thisTrialsTestImages2_3 != None:
            for paramName in thisTrialsTestImages2_3:
                exec('{} = thisTrialsTestImages2_3[paramName]'.format(paramName))
        
        for thisTrialsTestImages2_3 in trialsTestImages2_3:
            currentLoop = trialsTestImages2_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_3.rgb)
            if thisTrialsTestImages2_3 != None:
                for paramName in thisTrialsTestImages2_3:
                    exec('{} = thisTrialsTestImages2_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTest7"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_18.keys = []
            key_resp_18.rt = []
            _key_resp_18_allKeys = []
            image_9.setImage(ImageFile)
            # keep track of which components have finished
            ImageTest7Components = [key_resp_18, image_9]
            for thisComponent in ImageTest7Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTest7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTest7"-------
            while continueRoutine:
                # get current time
                t = ImageTest7Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTest7Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_18* updates
                waitOnFlip = False
                if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_18.frameNStart = frameN  # exact frame index
                    key_resp_18.tStart = t  # local t and not account for scr refresh
                    key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
                    key_resp_18.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_18.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_18.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_18_allKeys.extend(theseKeys)
                    if len(_key_resp_18_allKeys):
                        key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                        key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_18.keys == str(AnimateInanimate)) or (key_resp_18.keys == AnimateInanimate):
                            key_resp_18.corr = 1
                        else:
                            key_resp_18.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_9* updates
                if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_9.frameNStart = frameN  # exact frame index
                    image_9.tStart = t  # local t and not account for scr refresh
                    image_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                    image_9.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTest7Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTest7"-------
            for thisComponent in ImageTest7Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_18.keys in ['', [], None]:  # No response was made
                key_resp_18.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_18.corr = 1;  # correct non-response
                else:
                   key_resp_18.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTestImages2_3 (TrialHandler)
            trialsTestImages2_3.addData('key_resp_18.keys',key_resp_18.keys)
            trialsTestImages2_3.addData('key_resp_18.corr', key_resp_18.corr)
            if key_resp_18.keys != None:  # we had a response
                trialsTestImages2_3.addData('key_resp_18.rt', key_resp_18.rt)
            trialsTestImages2_3.addData('key_resp_18.started', key_resp_18.tStartRefresh)
            trialsTestImages2_3.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
            trialsTestImages2_3.addData('image_9.started', image_9.tStartRefresh)
            trialsTestImages2_3.addData('image_9.stopped', image_9.tStopRefresh)
            # the Routine "ImageTest7" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTestImages2_3.addData('text_2.started', text_2.tStartRefresh)
            trialsTestImages2_3.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTestImages2_3'
        
        
        # ------Prepare to start Routine "Rest"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        RestComponents = [text_5, key_resp_5]
        for thisComponent in RestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Rest"-------
        while continueRoutine:
            # get current time
            t = RestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        part2.addData('text_5.started', text_5.tStartRefresh)
        part2.addData('text_5.stopped', text_5.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        part2.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            part2.addData('key_resp_5.rt', key_resp_5.rt)
        part2.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        part2.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTestImages2_4 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ImageTests4_Reversed.xlsx', selection='0:2'),
            seed=None, name='trialsTestImages2_4')
        thisExp.addLoop(trialsTestImages2_4)  # add the loop to the experiment
        thisTrialsTestImages2_4 = trialsTestImages2_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_4.rgb)
        if thisTrialsTestImages2_4 != None:
            for paramName in thisTrialsTestImages2_4:
                exec('{} = thisTrialsTestImages2_4[paramName]'.format(paramName))
        
        for thisTrialsTestImages2_4 in trialsTestImages2_4:
            currentLoop = trialsTestImages2_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestImages2_4.rgb)
            if thisTrialsTestImages2_4 != None:
                for paramName in thisTrialsTestImages2_4:
                    exec('{} = thisTrialsTestImages2_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ImageTest8"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_19.keys = []
            key_resp_19.rt = []
            _key_resp_19_allKeys = []
            image_10.setImage(ImageFile)
            # keep track of which components have finished
            ImageTest8Components = [key_resp_19, image_10]
            for thisComponent in ImageTest8Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ImageTest8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ImageTest8"-------
            while continueRoutine:
                # get current time
                t = ImageTest8Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ImageTest8Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_19* updates
                waitOnFlip = False
                if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_19.frameNStart = frameN  # exact frame index
                    key_resp_19.tStart = t  # local t and not account for scr refresh
                    key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
                    key_resp_19.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_19.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_19.getKeys(keyList=['1', '2'], waitRelease=False)
                    _key_resp_19_allKeys.extend(theseKeys)
                    if len(_key_resp_19_allKeys):
                        key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                        key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_19.keys == str(AnimateInanimate)) or (key_resp_19.keys == AnimateInanimate):
                            key_resp_19.corr = 1
                        else:
                            key_resp_19.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *image_10* updates
                if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_10.frameNStart = frameN  # exact frame index
                    image_10.tStart = t  # local t and not account for scr refresh
                    image_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                    image_10.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ImageTest8Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ImageTest8"-------
            for thisComponent in ImageTest8Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_19.keys in ['', [], None]:  # No response was made
                key_resp_19.keys = None
                # was no response the correct answer?!
                if str(AnimateInanimate).lower() == 'none':
                   key_resp_19.corr = 1;  # correct non-response
                else:
                   key_resp_19.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsTestImages2_4 (TrialHandler)
            trialsTestImages2_4.addData('key_resp_19.keys',key_resp_19.keys)
            trialsTestImages2_4.addData('key_resp_19.corr', key_resp_19.corr)
            if key_resp_19.keys != None:  # we had a response
                trialsTestImages2_4.addData('key_resp_19.rt', key_resp_19.rt)
            trialsTestImages2_4.addData('key_resp_19.started', key_resp_19.tStartRefresh)
            trialsTestImages2_4.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
            trialsTestImages2_4.addData('image_10.started', image_10.tStartRefresh)
            trialsTestImages2_4.addData('image_10.stopped', image_10.tStopRefresh)
            # the Routine "ImageTest8" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank500"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank500Components = [text_2]
            for thisComponent in Blank500Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Blank500"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank500Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank500"-------
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsTestImages2_4.addData('text_2.started', text_2.tStartRefresh)
            trialsTestImages2_4.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsTestImages2_4'
        
        thisExp.nextEntry()
        
    # completed nRepsTask2 repeats of 'part2'
    
# completed 1.0 repeats of 'controlTaskOrder'


# ------Prepare to start Routine "End_Experiment"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
End_ExperimentComponents = [key_resp_20, text_3]
for thisComponent in End_ExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End_ExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End_Experiment"-------
while continueRoutine:
    # get current time
    t = End_ExperimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End_ExperimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_ExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End_Experiment"-------
for thisComponent in End_ExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "End_Experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
