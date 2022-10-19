import math
import numpy as np
import matplotlib.pyplot as plt
E=10**-10
for i in range(0,110,10):
    x=i*1.0
    clan=1.0
    fact=1.0
    suma1=1.0
    sumak=1.0
    suma2=1.0
    suma3=1.0
    k=0.0  
    while(clan>E):
                k=k+1
                fact=fact*k
                sumak=-sumak*x/k
                clan=x**k/fact 
                    
                if (k%2==0):
                    suma1=suma1+clan
                else:
                    suma1=suma1-clan
                suma2=suma2+sumak
                suma3=suma3+clan
                if x==20:
                    print("Za x = 20 svi članovi preko reda su: ",suma1)
    print('x je:',x)
    print('Suma1:',suma1)
    print('Suma2:',suma2)
    print('Suma3:',1/suma3)
    print('e na x:',math.e**(-x))
