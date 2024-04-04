# code18-15 (approx)
import ulab as np

def f(x):
    return x*x*x-1

print("bisect of x^3-1 = {}".format(np.approx.bisect(f,0,4)))
print("bisect of x^3-1 = {} (maxiter=10)".format(np.approx.bisect(f,0,4,maxiter=10)))
print("bisect of x^3-1 = {} (xtol=0.1)".format(np.approx.bisect(f,0,4),xtol=0.1))
print("fmin of x^3-1 = {}".format(np.approx.fmin(f,1.0)))
print("fmin of x^3-1 = {} (xatol=0.1)".format(np.approx.fmin(f,1.0,xatol=0.1)))
print("newton of x^3-1 = {}".format(np.approx.newton(f,3.0,tol=0.001,rtol=0.01)))
