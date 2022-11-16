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

#necessary libraries & modules

import time 
import asyncio

from threading import Thread

# global variables

P = 0
C = 0
H = 0
L = 2

ICD_P = 0
ICD_C = 0

ICD_checker_P = 0
ICD_checker_C = 0

time1 = 5
time2 = 5

def no_p_no_c():
    # global variable declarations
    global H
    global L
    global P
    global C
    
    global ICD_P
    global ICD_C

    print("case 1")

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
    # global variable declarations
    global H
    global L
    global P
    global C
    
    global ICD_C

    global time1
    global time2

    print("case 2")

    while ICD_C:
        time.sleep(0.1)
        print("ICD for Car")

    print("buffer time")
    time.sleep(time2)
    print("heavy road yellow")
    H = 1
    time.sleep(2)
    print("heavy road red")
    H = 2
    time.sleep(1)
    print("light road green")
    L = 0
    print("cars passing")
    time.sleep(time2) # cars passing
    P = 0
    C = 0
    ICD_C = 1

def yes_p_no_c():
    # global variable declarations
    global H
    global L
    global P
    global C
    
    global ICD_P

    global time1
    global time2

    print("case 3")

    while ICD_P:
        time.sleep(0.1)
        print("ICD for Pedestrian")

    print("buffer time")
    time.sleep(time1)
    print("heavy road yellow")
    H = 1
    time.sleep(2)
    print("heavy road red")
    H = 2
    time.sleep(1)
    print("light road green")
    L = 0
    print("pedestrian crossing")
    time.sleep(time2) # pedestrians crossing
    P = 0
    C = 0
    ICD_P = 1

def yes_p_yes_c():
    # global variable declarations
    global H
    global L
    global P
    global C
    
    global ICD_P
    global ICD_C

    global time1
    global time2

    print("case 4")

    while (ICD_P or ICD_C):
        time.sleep(0.1)
        print("ICD")
        
    print("buffer time")
    time.sleep(time1)
    print("heavy road yellow")
    H = 1
    time.sleep(2)
    print("heavy road red")
    H = 2
    time.sleep(1)
    print("light road green")
    L = 0
    time.sleep(time2) # pedestrians crossing
    P = 0
    C = 0
    ICD_P = 1
    ICD_C = 1

def check_ICD_P():
    # global variable declarations
    global ICD_P
    global ICD_checker_P

    global time2

    if (ICD_P == 1 and ICD_checker_P == 0):

        ICD_checker_P = 1
        time.sleep(time2)

        ICD_P = 0
        ICD_checker_P = 0

def check_ICD_C():
    # global variable declarations
    global ICD_C
    global ICD_checker_C

    global time2
    
    if (ICD_C == 1 and ICD_checker_C == 0):

        ICD_checker_C = 1
        time.sleep(time2)

        ICD_C = 0
        ICD_checker_C = 0

if __name__ == '__main__':

    while (True):
        # threading functions declaration
    
        check_P = Thread(target = check_ICD_P)
        check_C = Thread(target = check_ICD_C)

        # x = Thread(target = no_p_no_c)
        # y = Thread(target = no_p_yes_c)
        # w = Thread(target = yes_p_no_c)
        # z = Thread(target = yes_p_yes_c)
        
        P = int(input("enter P"))
        if (P != 0 and P != 1):
            print("please enter a P value of either 0 or 1")
        C = int(input("enter C"))
        if (C != 0 and C != 1):
            print("please enter a C value of either 0 or 1")

        # time.sleep(1)
        
        if (P == 0 and C == 0):
            # x.start()
            no_p_no_c()
        elif (P == 0 and C == 1):
            # y.start()
            no_p_yes_c()
        elif (P == 1 and C == 0):
            # w.start()
            yes_p_no_c()
        elif (P == 1 and C == 1):
            # z.start()
            yes_p_yes_c()
            
        check_P.start()
        check_C.start()

        print("P is: " + str(P))
        print("C is: " + str(C))
        print("H is: " + str(H))
        print("L is: " + str(L))

        print("ICD_P is: " + str(ICD_P))
        print("ICD_C is: " + str(ICD_C))

   
    
    
