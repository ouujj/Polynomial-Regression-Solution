import matplotlib.pyplot as plt
import warnings
import numpy as np
warnings.simplefilter('ignore', np.RankWarning)


X = np.array([float(x) for x in input("Enter set x value split by ',': ").split(',')])
Y =  np.array([float(y) for y in input("Enter set y value split by ',': ").split(',')])
degree = float(input("Enter degree: "))

A = np.polyfit(X, Y, degree)
eq= "("+str("%.3f"%A[0])+")"+" + "+"("+str("%.3f"%A[1])+")x"
for i in range(2,len(A)):
    eq += " + ("+str("%.3f"%A[i])+")x^"+str(i)


with warnings.catch_warnings():
    warnings.simplefilter('ignore', np.RankWarning)
    P = np.poly1d(A)

    
print("\nequation:")   
print(eq)


xp = np.linspace(min(X)-0.5, max(X)+0.5, 100)
_ = plt.plot(X, Y, '.', xp, P(xp), '-', xp, P(xp), '--')
plt.ylim(min(Y)-0.5,max(Y)+0.5)
plt.show()

    
    
