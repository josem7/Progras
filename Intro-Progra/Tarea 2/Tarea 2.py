def ganador_2(tablero):
    contg=0
    for i in range(5):
        for j in range (5):
            if tablero[i][j]=="G":
                contg+=1
    if contg<=10:
        return(True)
    else:
        return(False)
def ganador_1(tablero):
    contmov=0
    for i in range(5):
        for j in range (5):
            if tablero[i][j]=="C":
                cordy=i
                cordx=j
    for i in range(5):
        for j in range (5):
            if movimiento_valido1(cordx,cordy,i,j,tablero,2):
                contmov+=1
    if contmov==0:
        return(True)
    else:
        return(False)
def comer(tablero):
    for i in range(5):
        for j in range (5):
            if tablero[i][j]=="C":
                cordy=i
                cordx=j
    for i in range(5):
        for j in range (5):
            if movimiento_valido2(cordx,cordy,i,j,tablero,2):
                return(True)
    return(False)
    
def crear_tablero(tablero):
    msg="0 "
    print("  0 1 2 3 4")
    for i in range(4):
        msg+=tablero[0][i]
        msg+="-"
    msg+=tablero[0][4]
    print(msg)
    print("  |\|/|\|/|")
    msg="1 "
    for i in range(4):
        msg+=tablero[1][i]
        msg+="-"
    msg+=tablero[1][4]
    print(msg)
    print("  |/|\|/|\|")
    msg="2 "      
    for i in range(4):
        msg+=tablero[2][i]
        msg+="-"
    msg+=tablero[2][4]
    print(msg)
    print("  |\|/|\|/|")
    msg="3 "
    for i in range(4):
        msg+=tablero[3][i]
        msg+="-"
    msg+=tablero[3][4]
    print(msg)
    print("  |/|\|/|\|")
    msg="4 " 
    for i in range(4):
        msg+=tablero[4][i]
        msg+="-"
    msg+=tablero[4][4]
    print(msg)
def movimiento_valido2(xi,yi,xf,yf,tablero,jug):
    cond= False
    if xf>4 or yf>4 or xf<0 or yf<0:
        return(False)
    if xi>4 or yi>4 or xi<0 or yi<0:
        return(False)
    if abs(xi-xf)>=3 or abs(yi-yf)>=3:
        return(False)
    if tablero[yf][xf]!="N":
        return(False)
    if (yi==1 and xi==2) or (yi==2 and xi==1) or (yi==2 and xi==3) or (yi==3 and xi==2) or (yi==0 and xi==1) or (yi==0 and xi==3) or (yi==1 and xi==0) or(yi==1 and xi==4) or (yi==3 and xi==0) or (yi==3 and xi==4) or (yi==4 and xi==1) or (yi==4 and xi==3):
        if yi!=yf and xi!=xf:
            return(False)
    if jug==2:
        cond1=True
        if tablero[yi][xi]!="C":
            return(False)
        if abs(xi-xf)==2 and abs(yf-yi)==2:
            xp=int((xi+xf)/2)
            yp=int((yi+yf)/2)
            if tablero[yp][xp]!="G":
                return (False)
            else:
                return(True)
                cond1=False
        if abs(xi-xf)==2:
            xp=int((xi+xf)/2)
            if tablero[yi][xp]!="G" or yi!=yf:
                if cond1:
                    return(False)
            else:
                return(True)
        if abs(yi-yf)==2:
            yp=int((yi+yf)/2)
            if tablero[yp][xi]!="G" or xi!=xf:
                if cond1:
                    return (False)
            else:
                return(True)
    return(cond)
def movimiento_valido1(xi,yi,xf,yf,tablero,jug):
    cond= True
    if xf>4 or yf>4 or xf<0 or yf<0:
        return(False)
    if xi>4 or yi>4 or xi<0 or yi<0:
        return(False)
    if abs(xi-xf)>=3 or abs(yi-yf)>=3:
        return(False)
    if tablero[yf][xf]!="N":
        return(False)
    if (yi==1 and xi==2) or (yi==2 and xi==1) or (yi==2 and xi==3) or (yi==3 and xi==2) or (yi==0 and xi==1) or (yi==0 and xi==3) or (yi==1 and xi==0) or(yi==1 and xi==4) or (yi==3 and xi==0) or (yi==3 and xi==4) or (yi==4 and xi==1) or (yi==4 and xi==3):
        if yi!=yf and xi!=xf:
            return(False)
    if jug==2:
        cond1=True
        if tablero[yi][xi]!="C":
            return(False)
        if abs(xi-xf)==2 and abs(yf-yi)==2:
            xp=int((xi+xf)/2)
            yp=int((yi+yf)/2)
            if tablero[yp][xp]!="G":
                return (False)
            else:
                cond=False
        if abs(xi-xf)==2:
            xp=int((xi+xf)/2)
            if tablero[yi][xp]!="G" or yi!=yf:
                if cond1:
                    return(False)
        if abs(yi-yf)==2:
            yp=int((yi+yf)/2)
            if tablero[yp][xi]!="G" or xi!=xf:
                if cond1:
                    return (False)
    return(cond)

def movimiento_valido(xi,yi,xf,yf,tablero,jug):
    cond= True
    if xf>4 or yf>4 or xf<0 or yf<0:
        return(False)
    if xi>4 or yi>4 or xi<0 or yi<0:
        return(False)
    if abs(xi-xf)>=3 or abs(yi-yf)>=3:
        return(False)
    if tablero[yf][xf]!="N":
        return(False)
    if (yi==1 and xi==2) or (yi==2 and xi==1) or (yi==2 and xi==3) or (yi==3 and xi==2) or (yi==0 and xi==1) or (yi==0 and xi==3) or (yi==1 and xi==0) or(yi==1 and xi==4) or (yi==3 and xi==0) or (yi==3 and xi==4) or (yi==4 and xi==1) or (yi==4 and xi==3):
        if yi!=yf and xi!=xf:
            return(False)
    if jug==2:
        cond1=True
        if tablero[yi][xi]!="C":
            return(False)
        if abs(xi-xf)==2 and abs(yf-yi)==2:
            xp=int((xi+xf)/2)
            yp=int((yi+yf)/2)
            if tablero[yp][xp]!="G":
                return (False)
            else:
                tablero[yp][xp]="N"
                cond1=False
        if abs(xi-xf)==2:
            xp=int((xi+xf)/2)
            if tablero[yi][xp]!="G" or yi!=yf:
                if cond1:
                    return(False)
            else:
                tablero[yi][xp]="N"
        if abs(yi-yf)==2:
            yp=int((yi+yf)/2)
            if tablero[yp][xi]!="G" or xi!=xf:
                if cond1:
                    return (False)
            else:
                tablero[yp][xi]="N"
    if jug==1:
        if tablero[yi][xi]!="G":
            return(False)
        if  abs(xi-xf)>=2 or abs(yi-yf)>=2:
            return(False)
    return(cond)
def mov(xi,yi,xf,yf,tablero,jug):
    tablero[yi][xi]="N"
    if jug==1:
        tablero[yf][xf]="G"
    if jug==2:
        tablero[yf][xf]="C"
def separar_inp(ent):
    x=ent
    msg=[]
    cond=True
    cont=0
    for i in range(0,len(x)):
        if(x[i]!=","):
            num=x[i]
            msg.append(num)
        else:
            cont+=1
    if len(x)>7 or cont!=3:
        cond=False        
    return(msg,cond)
def separar_inp1(ent):
    x=ent
    msg1=""
    msg=[]
    cond=True
    cont=0
    for i in range(0,len(x)):
        if(x[i]!=","):
            msg1+=x[i]
        else:
            msg.append(msg1)
            msg1=""
        if i==len(x)-1:
            msg.append(msg1)
    return(msg)
def separar_inp2(ent):
    x=ent
    msg=[]
    cond=x[0]
    for i in range(0,len(x)):
        if(x[i]!=",") and(x[i]!="C") and (x[i]!="G") and x[i]!="\n":
            num=x[i]
            msg.append(num)
    return(msg,cond)

    
lista=[]
jug=1
k=int(input("Desea empezar una partida nueva(1) o cargar una partida(2)"))
cont= True
if k==1:
    tablero=[["G","G","G","G","G"],["G","G","G","G","G"],["G","N","C","N","G"],["N","N","N","N","N"],["N","N","N","N","N"]]
    print("¡Bienvenido al juego del coyote y las gallinas!")
    n_jug1=input("¡Perfecto! Dime el nombre del jugador que será las gallinas")
    n_jug2=input("¡Perfecto! Dime el nombre del jugador que será el coyote")
    nombres=(n_jug1+","+n_jug2+"\n")
    lista.append(nombres)
elif k==2:
    n_archivo=input("Cual es el nombre del archivo")
    archivo=open(n_archivo,"r")
    for linea in archivo.readlines(1):
        tablero=[["G","G","G","G","G"],["G","G","G","G","G"],["G","N","C","N","G"],["N","N","N","N","N"],["N","N","N","N","N"]]
        print("¡Bienvenido al juego del coyote y las gallinas!")
        ln=separar_inp1(linea)
        n_jug1=str(ln[0])
        n_jug2=str(ln[1])
        nombres=(n_jug1+","+n_jug2)
        lista.append(nombres)
    for i,linea in enumerate(archivo):
        inp=linea
        limp,x=separar_inp2(inp)
        xi=int(limp[0])
        yi=int(limp[1])
        xf=int(limp[2])
        yf=int(limp[3])
        if x=="G":
            jug=1
            print("Es tu turno",n_jug1,"¿Cual es tu movimiento?")
            print("¿o deseas guardar la partida y salir?(G)")
            print("¿O deseas simplemente salir?(S)")
            if movimiento_valido(xi,yi,xf,yf,tablero,jug):
                mov(xi,yi,xf,yf,tablero,jug)
                lista.append(inp)
                jug=2
                crear_tablero(tablero)
            if ganador_1(tablero):
                print("Ganador",n_jug1)
                cont=False
        elif x=="C":
            jug=2
            print("Es tu turno",n_jug2,"¿Cual es tu movimiento?")
            print("¿o deseas guardar la partida y salir?(G)")
            print("¿O deseas simplemente salir?(S)")
            if movimiento_valido(xi,yi,xf,yf,tablero,jug):
                mov(xi,yi,xf,yf,tablero,jug)
                lista.append(inp)
                jug=1
                crear_tablero(tablero)
            if abs(xi-xf)>1 or abs(yi-yf)>1:
                jug=2
            if ganador_2(tablero):
                print("Ganador",n_jug2)
                cont=False
           
    archivo.close
if cont==True:
    print("Comencemos!")
    crear_tablero(tablero)
while cont==True:
    
    cont1=True
    while jug==1 and cont==True:
        print("Es tu turno",n_jug1,"¿Cual es tu movimiento?")
        print("¿o deseas guardar la partida y salir?(G)")
        print("¿O deseas simplemente salir?(S)")
        inp=input()
        if inp=="G" or inp=="S":
            n_archivo1=input("Como quieres que se llame el archivo")
            archivo=open(n_archivo1,"w")
            for i in range(len(lista)):
                archivo.write(lista[i])
            archivo.close()
            cont=False
        else:
            limp,cond=separar_inp(inp)
            xi=int(limp[0])
            yi=int(limp[1])
            xf=int(limp[2])
            yf=int(limp[3])
            if movimiento_valido(xi,yi,xf,yf,tablero,jug)and cond:
                mov(xi,yi,xf,yf,tablero,jug)
                lista.append("G,"+inp+"\n")
                jug=2
                crear_tablero(tablero)
            else:
                print("Movimiento invalido")
            if ganador_1(tablero):
                cont=False
                print("Ganador",n_jug1)
                p=int(input("Desea guardar la partida Si(1) o No(2)"))
                if p==1:
                    n_archivo1=input("Como quieres que se llame el archivo")
                    archivo=open(n_archivo1,"w")
                    for i in range(len(lista)):
                        archivo.write(lista[i])
                    archivo.close()
    while jug==2 and cont==True:
        print("Es tu turno",n_jug2,"¿Cual es tu movimiento?")
        print("¿o deseas guardar la partida y salir?(G)")
        print("¿O deseas simplemente salir?(S)")
        inp=input()
        if inp=="G" or inp=="S":
            n_archivo1=input("Como quieres que se llame el archivo")
            archivo=open(n_archivo1,"w")
            for i in range(len(lista)):
                archivo.write(lista[i])
            archivo.close()
            cont=False
        else:
            limp,cond=separar_inp(inp)
            xi=int(limp[0])
            yi=int(limp[1])
            xf=int(limp[2])
            yf=int(limp[3])
            if comer(tablero) and abs(xi-xf)>1 or abs(yi-yf)>1:
                x=True
                while comer(tablero) and cont:
                    if movimiento_valido2(xi,yi,xf,yf,tablero,jug)and cond and movimiento_valido(xi,yi,xf,yf,tablero,jug):
                        mov(xi,yi,xf,yf,tablero,jug)
                        crear_tablero(tablero)
                        lista.append("C,"+inp+"\n")
                        x=False
                    else:
                        if x:
                            print("Movimiento invalido, debes comerte a la gallina")
                        print("Es tu turno",n_jug2,"¿Cual es tu movimiento?")
                        print("¿o deseas guardar la partida y salir?(G)")
                        print("¿O deseas simplemente salir?(S)")
                        inp=input()
                        if inp=="G" or inp=="S":
                            n_archivo1=input("Como quieres que se llame el archivo")
                            archivo=open(n_archivo1,"w")
                            for i in range(len(lista)):
                                archivo.write(lista[i])
                            archivo.close()
                            cont=False
                        else:
                            limp,cond=separar_inp(inp)
                            xi=int(limp[0])
                            yi=int(limp[1])
                            xf=int(limp[2])
                            yf=int(limp[3])
                            x=True
                jug=1
            elif movimiento_valido(xi,yi,xf,yf,tablero,jug) and cond:
                mov(xi,yi,xf,yf,tablero,jug)
                lista.append("C,"+inp+"\n")
                jug=1
                crear_tablero(tablero)
            else:
                print("Movimiento invalido")
            if ganador_2(tablero):
                cont=False
                print("Ganador",n_jug2)
                p=int(input("Desea guardar la partida Si(1) o No(2)"))
                if p ==1:
                    n_archivo1=input("Como quieres que se llame el archivo")
                    archivo=open(n_archivo1,"w")
                    for i in range(len(lista)):
                        archivo.write(lista[i])
                    archivo.close()
print("Chao")
