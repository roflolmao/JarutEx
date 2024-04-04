#coce18-17 : fft
import ulab as np
# FFT
numData = 4
x = np.linspace(0,10,numData)
print("x",x)
y = np.vector.cos(x)
print("y",y)
z = np.zeros(len(x))
print("z",z)
a,b = np.fft.fft(x)
for i in range(numData):
    print("fft(x) = {}+{}i".format(a[i],b[i]))
c,d = np.fft.fft(x,z)
for i in range(numData):
    print("fft(x,z) = {}+{}i".format(c[i],d[i]))
#
xnew = np.fft.ifft(a,b)
print("ifft(a,b)",xnew)
x2new,znew = np.fft.ifft(c,d)
print("ifft(c,d) ->x",x2new)
print("    ->z",znew)
#
a,b = np.fft.fft(y)
s = np.fft.spectrogram(y)
print(np.vector.sqrt(a*a+b*b))
print(s)
