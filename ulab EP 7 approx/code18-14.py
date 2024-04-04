# code18-14 (approx)
import ulab as np

x = np.array([3.6, 7.9, 5.6, 8.4, 7.7, 9.2], dtype=np.float)
xp = np.array([4, 4.5, 5.5, 7.5, 10.5], dtype=np.float)
fp = np.array([1,2,4,7,11],dtype=np.float)
print(np.approx.interp(x,xp,fp))
print(np.approx.interp(x,xp,fp,left=0.4))
print(np.approx.interp(x,xp,fp,right=11))
print("trapz(x)=",np.approx.trapz(x))
