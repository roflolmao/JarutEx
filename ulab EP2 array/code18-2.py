# code18-2
import ulab as np
a = np.array([-1,0,1],dtype=np.float)
b = np.array([1,2,3])
c = np.array([-1,0,1],dtype=np.int8)
print("type of a is {}.".format(type(a)))
print("value of a is {}.".format(a))
print("len() of a is {}.".format(len(a)))
print("abs() of a is {}.".format(abs(a)))
print("value of a*3 is {}.".format(a*3))
print("value of a/2 is {}.".format(a/2))
print("value of b is {}.".format(b))
print("value of c is {}.".format(c))
print("a == [1,2,3] ? {}".format(a==b))
print("a == int([-1,0,1]) ? {}".format(a==c))
print("a+b = {}".format(a+b))
print("a-c = {}".format(a-c))
