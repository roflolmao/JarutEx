import numpy as np
import matplotlib.pyplot as plt

n = 24
x = np.arange(n)
y = np.array([29.5, 29.2, 29.0, 28.9, 28.6, 28.8, 28.5, 28.3, 29.0, 29.6, 30.8, 31.8, 31.7, 32.1, 32.5, 31.6, 30.5, 30.5, 30.2, 29.6, 29.5, 29.2, 28.1, 28.9])

sumX = np.sum(x)
sumY = np.sum(y)
sumXY = np.sum(x*y)
sumX2= np.sum(x*x)
sumY2 = np.sum(y*y)

print("SumX={}".format(sumX))
print("SumY={}".format(sumY))
print("SumXY={}".format(sumXY))
print("SumX2={}".format(sumX2))
print("SumY2={}".format(sumY2))

a = ((sumY*sumX2)-(sumX*sumXY))/((n*sumX2)-(sumX*sumX))
b = ((n*sumXY)-(sumX*sumY))/((n*sumX2)-(sumX*sumX))
print("Y = ({})+({}*x)+c".format(a,b))

z = a+(b*x)
print(z)

plt.suptitle('regression')
plt.ylabel('Temperature')
plt.xlabel('Hour')
plt.subplot(111)
plt.plot(y)
plt.subplot(111)
plt.plot(z)
plt.show()
