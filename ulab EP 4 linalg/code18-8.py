#code18-8
import ulab as np
import time

print('inv of 2 by 2 matrix:')
m = np.array([[2, 1], [3, 5]])
t0 = time.ticks_us()
np.linalg.inv(m)
print("{} usec".format(time.ticks_us()-t0))

print('inv of 4 by 4 matrix:')
m = np.array([[7, 2, 1, 4], [5, 5, 4, 4], [0, 2, 8, 3], [8, 0, 3, 1]])
t0 = time.ticks_us()
np.linalg.inv(m)
print("{} usec".format(time.ticks_us()-t0))

print('inv of 8 by 8 matrix:')
m = np.array([[ 1, 2, 3, 4, 5, 6, 7, 8],
              [ 9,10,11,12,13,14,15,16],
              [21,18,19, 0,21,22, 0,10],
              [33, 0, 1, 0,29, 0,31,10],
              [49,34,35,36,37,38,39,10],
              [ 1, 1, 0,44,45, 0,47,10],
              [49, 0,51,52,53,54, 0,10],
              [ 1,58,59, 0,61, 0,63,10]])
t0 = time.ticks_us()
np.linalg.inv(m)
print("{} usec".format(time.ticks_us()-t0))
