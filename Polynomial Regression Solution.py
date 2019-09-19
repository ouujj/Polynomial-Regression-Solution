import math
#import matplotlib.pyplot as plt

X = [float(x) for x in input("Enter set x value split by ',': ").split(',')]
Y = [float(y) for y in input("Enter set y value split by ',': ").split(',')]
degree = int(input("Enter degree: "))
A=[]
def polyRegSol():
    
    sumxn=[] #[n,sum x, sum x^2 ,sum x^3 ...... sum x^2n ]
    sumxn.append(len(X))
    sumxn.append(sum(X))

   
       
       
    
    i=2
    while(i<=degree*2):
        sumxn.append(sum([x**i for x in X]))
        i+=1
    #print(sumxn)
    print()
    #print("XtX :")   
    XTX=[[] for i in range((degree+1))]
    for i in range((degree+1)):
        for j in range((degree+1)):
            XTX[i].append(sumxn[j+i])
        #print(XTX[i])

        
    #print("XtY :")
    XTY=[]
    XTY.append(sum(Y))
    i=1
    while(i<=degree):
        XTY.append(sum([(X[j]**i)*Y[j] for j in range(len(X))]))
        i+=1
    #print(XTY)
    print("Polynomial Matrix:")
    for i in range(degree+1):
       A.append("A"+str(i))
       print(XTX[i],"  ",A[i],"  ",XTY[i])
       



























   
if(len(X)!=len(Y)):
    print("Data set not equar!!!")
else:
    polyRegSol()
