# code18-4
# Prewitt operator
import ulab as np
Gx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
Gy = Gx.transpose()
print("Gx={}\nGy={}".format(Gx,Gy))
print("size: Gx={} Gy={}".format( Gx.size(), Gy.size()))
print("shape: Gx={} Gy={}".format( Gx.shape(), Gy.shape() ))
GxFlat = Gx.flatten()
GyFlat = Gy.flatten()
print("GxFlat={}\nGyFlat={}".format( GxFlat, GyFlat ))
print("size: GxFlat={} GyFlat={}".format( GxFlat.size(), GyFlat.size()))
print("shape: GxFlat={} GyFlat={}".format( GxFlat.shape(), GyFlat.shape()))
