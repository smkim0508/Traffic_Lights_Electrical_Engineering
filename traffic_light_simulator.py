# Variable definitions 
# PH = Pedestrian waiting
# PL = No pedestrian waiting

# CH = Cars waiting on light road
# CL = No cars waiting on light road

# HG = Heavy light green
# HY = Heavy light yellow
# HR = Heavy light red

# LG = Light light green
# LY = Light light yellow
# LR = Light light red

# P = pedestrian count, 0 1 (no pedestrian, pedestrian waiting)
# C = car on light road count, (0, 1) = (no car, car waiting)

# H = heavy light traffic signal, (0, 1, 2) = (green, yellow, red)
# L = light light traffic signal, (0, 1, 2) = (green, yellow, red)

# ICD = Internal Cooldown; the time between each function call is permitted

import time 
import asyncio

# global variables

P = 0
C = 0
H = 0
L = 2

ICD_P = 0
ICD_C = 0

def no_p_no_c():
    if (H == 2 and L == 0):
        L = 1
        time.sleep(2) 
        L = 2
        time.sleep(1)
        H = 0
    else:
        H = 0
        L = 2
    P = 0
    C = 0

def no_p_yes_c():
    while ICD_C: time.sleep(0.1)
    time.sleep(30)
    H = 1
    time.sleep(2)
    H = 2
    time.sleep(1)
    L = 0
    time.sleep(30) # cars passing
    P = 0
    C = 0
    ICD_C = 1

def yes_p_no_c():
    while ICD_P: time.sleep(0.1)
    time.sleep(15)
    H = 1
    time.sleep(2)
    H = 2
    time.sleep(1)
    L = 0
    time.sleep(30) # pedestrians crossing
    P = 0
    C = 0
    ICD_P = 1

def yes_p_yes_c():
    while (ICD_P or ICD_C): time.sleep(0.1)
    time.sleep(15)
    H = 1
    time.sleep(2)
    H = 2
    time.sleep(1)
    L = 0
    time.sleep(30) # pedestrians crossing
    P = 0
    C = 0
    ICD_P = 1
    ICD_C = 1

async def check_ICD():
    if (ICD_P == 1):
        time.sleep(30)
        ICD_P = 0

    if (ICD_C == 1):
        time.sleep(30)
        ICD_C = 0

while (True):
    if (P == 0 and C == 0):
        no_p_no_c()
    elif (P == 0 and C == 1):
        no_p_yes_c()
    elif (P == 1 and C == 0):
        yes_p_no_c()
    elif (P == 1 and C == 1):
        yes_p_yes_c()
    check_ICD()
    
    
    
