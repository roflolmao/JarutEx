# code18-13
import ulab as np

M = np.array(range(12), dtype=np.int8)
N = np.linspace(12,1,12,dtype=np.int8)

print("M == N ? {}".format(np.compare.equal(M, N)))
print("M != N ? {}".format(np.compare.not_equal(M, N)))
print("minimum(M,N) = {}".format(np.compare.minimum(M,N)))
print("maximum(M,N) = {}".format(np.compare.maximum(M,N)))
print("clip(M,5,10) = {}".format(np.compare.clip(M,5,10)))
print("clip(M,N,10) = {}".format(np.compare.clip(M,N,10)))
