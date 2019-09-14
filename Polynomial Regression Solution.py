import math
import matplotlib.pyplot as plt

X = [float(x) for x in input("Enter set x value split by ',': ").split(',')]
Y = [float(y) for y in input("Enter set y value split by ',': ").split(',')]
degree = float(input("Enter degree: "))*2
def polyRegSol():
    sumxn=[] #[n,sum x, sum x^2 ,sum x^3 ...... sum x^2n ]
    sumxn.append(len(X))
    sumxn.append(sum(X))
    sumy=(sum(Y))
    
    i=2
    while(i<=degree):
        sumxn.append(sum([i**x for x in X]))
        i+=1
        
    print(sumxn)   




















   
if(len(X)!=len(Y)):
    print("Data set not equar!!!")
else:
    polyRegSol()
