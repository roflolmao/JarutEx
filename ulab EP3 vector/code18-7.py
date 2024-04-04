# code18-7
import time
import ulab as np
import math

def scale(pX,pY,Sx=1.0,Sy=1.0):
    return ((pX*Sx, pY*Sy))

def rotate(pX,pY,angle):
    rad = math.radians(angle)
    xCos = pX*np.vector.cos(rad)
    ySin = pY*np.vector.sin(rad)
    xSin = pX*np.vector.sin(rad)
    yCos = pY*np.vector.cos(rad)
    newX = xCos - ySin
    newY = xSin + yCos
    return (newX, newY)

pX = np.array([-1,1,1,-1],dtype=np.float)
pY = np.array([1,1,-1,-1],dtype=np.float)
Sx = 2.0
Sy = 4.0
newP = scale(pX,pY,Sx,Sy)
newP2 = rotate(pX, pY, 45.0)
print("Vector X={}".format(pX))
print("Vector Y={}".format(pY))
print("Vector X*Sx={}".format(newP[0]))
print("Vector Y*Sy={}".format(newP[1]))
print("Vector X rot 45 degrees={}".format(newP2[0]))
print("Vector Y rot 45 degrees={}".format(newP2[1]))
