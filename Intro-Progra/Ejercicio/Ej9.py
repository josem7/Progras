#!/bin/python3

import sys
def esPrimo(x):
    cont=1
    divis=0
    primo=False
    while cont<=x:
        if x%cont==0:
            divis+=1
        cont+=1
    if divis==2:
        primo=True
    return (primo)

def cod_digitos(x):
    length=len(str(x))
    dig=""
    i=0
    while (i<length):
        y=str(x)
        t=str(((int(y[i])*length))%10)
        dig+=t
        i+=1
    return(dig)
def cod_impares(x):
    length=len(str(x))
    dig=""
    i=0
    while (i<length):
        y=str(x)      
        if (i%2==0):
            t=(int(y[i])-1)%10
        else:
            t=(int(y[i])+1)%10
        dig+=str(t)
        i+=1
    imp=int(dig)*length
    return(imp)

def cod_primos(x):
    cont=1
    while(cont<x):
        esprimo=esPrimo(cont)
        if(x%cont==0) and (esprimo):
            primo=cont
        cont+=1
    y1=x/primo
    cont=1
    while(cont<y1):
        esprimo=esPrimo(cont)
        if(y1%cont==0) and (esprimo):
            primo2=cont
        cont+=1

    res=(y1*primo2)%1
    return(res)

def cod_binaria(x):
    return(x)
    

x = int(input())
x1 = cod_digitos(x)
x2 = cod_impares(x1)
x3 = cod_primos(x2)
x4 = cod_binaria(x3)
print(x1)
print(x2)
print(x3)
print(x4)
