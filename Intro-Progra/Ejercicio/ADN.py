


def contar_base(ADN,Base):
    cont=0
    cantidad=0
    length=len(ADN)
    while(cont<length):
        if(Base==ADN[cont]):
            cantidad+=1
        cont+=1
    return (cantidad)

ADN=input("ADN")
Base=input("Base")
msg= contar_base(ADN,Base)
print("El numero de",Base,"es",msg)
        

        
