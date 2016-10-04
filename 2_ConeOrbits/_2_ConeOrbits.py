import math
from matplotlib import pyplot as plt


#PARAM_A = 1.1
#PARAM_E = 0.8

PARAM_A = 1
PARAM_E = 1

def CalcRFromAngle(phi):
    global PARAM_A
    global PARAM_E

    return PARAM_A * (1 - PARAM_E**2) / ( 1 + PARAM_E * math.cos(phi / 360 * 2 * math.pi))


def CreatePlot():
    phi = 0
    step = .95
    xCoord = []
    yCoord = []

    while phi <= 360:
        r = CalcRFromAngle(phi)
        x = r * math.cos(phi / 360 * 2 * math.pi)
        y = r * math.sin(phi / 360 * 2 * math.pi)
        
        xCoord.append(x)
        yCoord.append(y)

        phi += step

    plt.plot(xCoord, yCoord)
    plt.show()

if __name__ == '__main__':
    CreatePlot()
        