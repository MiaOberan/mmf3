import math
E=10**-10
for i in range(0,110,10):
    x=i*1.0 
    clan=1.0
    fact=1.0
    s1=1.0
    sk=1.0
    s2=1.0
    s3=1.0
    k=0  
    while(clan>E):
                k=k+1
                fact=fact*k
                sk=-sk*x/k
                clan=x**k/fact 
                    
                if (k%2==0):
                    s1=s1+clan
                else:
                    s1=s1-clan
                s2=s2+sk
                s3=s3+clan
                

    print(s1)
    print(s2)
    print(1/s3)
    print(math.e**(-x))
    print("  ")
