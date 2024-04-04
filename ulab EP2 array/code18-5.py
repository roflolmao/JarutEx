#code18-5
import ulab as np
p0 = np.array([-1,1,1],dtype=np.float)
p1 = np.array([1,1,1],dtype=np.float)
p2 = np.array([1,-1,1],dtype=np.float)
p3 = np.array([-1,-1,1],dtype=np.float)

def matMul(p,M):
    x = p[0]*M[0][0]+p[0]*M[1][0]+p[0]*M[2][0]
    y = p[1]*M[0][1]+p[1]*M[1][1]+p[1]*M[2][1]
    z = p[2]*M[0][2]+p[2]*M[1][2]+p[2]*M[2][2]
    return (x,y,z)

def scale(p0,p1,p2,p3,Sx=1.0,Sy=1.0):
    Ms = np.array([[Sx,0.0,0.0],[0.0,Sy,0.0],[0.0,0.0,1.0]],dtype=np.float)
    return (matMul(p0,Ms), matMul(p1,Ms), matMul(p2,Ms), matMul(p3,Ms))

print(scale(p0,p1,p2,p3,2.0,2.0))
