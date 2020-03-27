figura=input("¿cuadrado o rectangulo?")
if figura=="cuadrado" :
    lado=float(input("¿lado?"))
    area=lado*lado
elif(figura=="rectangulo"):
    base=float(input("¿base?"))
    altura=float(input("¿altura?"))
    area=base*altura
else:
    area=("saco wea, cuadrado o rectangulo")
print("El area es:",area)
