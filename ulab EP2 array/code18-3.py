# code18-3
import ulab as np
a = np.array([1,2,3],dtype=np.int8)
b = np.array([[1,0,-1],[1,0,-1],[1,0,-1]],dtype=np.float)
print("data:\na={}\nb={}".format(a,b))
print("shape: a={} b={}".format(a.shape(),b.shape()))
print("size: a={} b={}".format(a.size(),b.size()))
print("item's size: a={} b={}".format(a.itemsize(),b.itemsize()))
a.reshape((3,1))
print("data:a={} shape={}".format(a,a.shape()))
