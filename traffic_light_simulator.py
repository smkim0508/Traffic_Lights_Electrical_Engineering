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

#P = pedestrian count, 0 1 (no pedestrian, pedestrian waiting)
#C = car on light road count, (0, 1) = (no car, car waiting)

#H = heavy light traffic signal, (0, 1, 2) = (green, yellow, red)
#L = light light traffic signal, (0, 1, 2) = (green, yellow, red)

P = 0
C = 0
H = 0
L = 2

ICD_P = 0
ICD_C = 0

def no_p_no_c():
    if (H == 2 and L == 0):
        L = 1
        # wait 2 second
        L = 2
        # wait 1 second
        H = 0
    else:
        H = 0
        L = 2
    P = 0
    C = 0

def no_p_yes_c():

def yes_p_no_c():

def yes_p_yes_c():

async def check_ICD():
    if (ICD_P == 1):
        # wait 30 seconds
        ICD_P = 0

    if (ICD_C == 1):
        # wait 30 seconds
        ICD_C = 0

while (True):
    if (P == 0 and C == 0):
        no_p_no_c()
    if (P == 0 and C == 1):
        no_p_yes_c()
    if (P == 1 and C == 0):
        yes_p_no_c()
    if (P == 1 and C == 1):
        yes_p_yes_c()
    check_ICD()
    
    
    
