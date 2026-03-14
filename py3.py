import math
a=float(input("enter the a value"))
b=float(input("enter the b value"))
c=float(input("enter the c value"))
d=(b*b)-(4*a*c)
if d>0:
   
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/ (2*a)

    print(f"the equation has two distinct roots that is {r1,r2}")
if d==0:
    r=-b/(2*a)
    print (f"the equation has exactly one root that is {r}")
if d<0:
    real=-b/2*a
    im=(math.sqrt(-d))/ (2*a)


    print(f"the equation has two complex roots that are {real,im}")    
        