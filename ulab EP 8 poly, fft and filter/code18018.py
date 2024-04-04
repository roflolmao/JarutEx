#coce18-18 : filter
import ulab as np

x = np.array([1,2,3,4,5])
y = np.array([1,10,100,1000])
print("x convolute with y = {}".format(np.filter.convolve(x,y)))
