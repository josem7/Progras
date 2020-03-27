x=1
cont=0
nmax=0
nmin=9
suma=0
while x==1:
    cont=cont+1
    msg="nota estudiante " + str(cont)
    nota=float(input(msg))
    suma=suma+nota
    if nota>nmax:
        nmax=nota
    if nota<nmin:
        nmin=nota
    x=int(input("0-Salir 1-Continuar"))
print("promedio",suma/cont)
print("nmax",nmax)
print("nmin",nmin)
