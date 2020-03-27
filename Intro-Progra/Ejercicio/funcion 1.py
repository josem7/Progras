import math
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
def cuadratica (a,b,c):
    x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    x2=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
    return(x1,x2)
x1,x2= cuadratica(a,b,c)
print("las soluciones son",x1,"y",x2)
