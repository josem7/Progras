class simulacion:
    def __init__(self):
        self.equipo=[]
        self.personaje=[]
        self.consumibles=[]
        self.stats=[]
        self.pruebas=[]
    def agregar_equipo(self,equipo):
        self.equipo.append(equipo)
    def agregar_personaje(self,personaje):
        self.personaje.append(personaje)
    def agregar_consumibles(self,consumible):
        self.consumibles.append(consumible)
    def agregar_prueba(self,prueba):
        self.pruebas.append(prueba)
        
    def calcular_stats(self):
        y=self.personaje[0]
        vida=y.vida
        destreza=y.destreza
        resistencia=y.resistencia
        inteligencia=y.inteligencia
        suerte=y.suerte
        for i in self.equipo:
            x=i.atributo
            if x=="vida":
                vida=int(vida*i.bonificador)
            elif x=="destreza":
                destreza=int(destreza*i.bonificador)
            elif x=="resistencia":
                resistencia=int(resistencia*i.bonificador)
            elif x=="inteligencia":
                inteligencia=int(inteligencia*i.bonificador)
            elif x=="suerte":
                suerte=int(suerte*i.bonificador)
        for i in self.consumibles:
            x=i.stat
            if x=="vida":
                vida+=(i.cant)
            elif x=="destreza":
                destreza+=(i.cant)
            elif x=="resistencia":
                resistencia+=(i.cant)
            elif x=="inteligencia":
                inteligencia+=(i.cant)
            elif x=="suerte":
                suerte+=(i.cant)
        return(vida, destreza, resistencia, inteligencia, suerte)
    def dar_prueba(self,prueba,per,num):
        prueba=self.pruebas[num]
        perso=self.personaje[0]
        a,b,c,d,e=self.calcular_stats()
        x=prueba.debilidad
        if x=="destreza":
            debilidad=b
        elif x=="resistencia":
            debilidad=c
        elif x=="inteligencia":
            debilidad=d
        elif x=="suerte":
            debilidad=e
        vida_perdida=((b-prueba.destreza)+(c-prueba.resistencia)+(d-prueba.inteligencia)+(e-prueba.suerte))*(prueba.vida//debilidad)
        if vida_perdida>=0:
            return(0)
        else:
            return(vida_perdida)
    def reiniciar_consumibles(self):
        self.consumibles=[]
    def __str__(self):
        a,b,c,d,e=self.calcular_stats()
        msg="V: "+str(a)+" D: "+str(b)+" R: "+str(c)+" I: "+str(d)+" S: "+str(e)    
        return msg
    
class personaje:
    def __init__(self,nombre,vida,tiempo,destreza,resistencia,inteligencia,suerte):
        self.nombre=nombre
        self.vida=vida
        self.tiempo=tiempo
        self.destreza=destreza
        self.resistencia=resistencia
        self.inteligencia=inteligencia
        self.suerte=suerte
    def descontar_tiempo(self,tiempo):
        self.tiempo=tiempo
    def descontar_vida(self,vida):
        self.vida=vida

class prueba:
    def __init__ (self,nombre,vida,destreza,resistencia,inteligencia,suerte,debilidad):
        self.nombre=nombre
        self.vida=vida
        self.destreza=destreza
        self.resistencia=resistencia
        self.inteligencia=inteligencia
        self.suerte=suerte
        self.debilidad=debilidad
    def __str__(self):
        msg="V: "+str(self.vida)+" D: "+str(self.destreza)+" R: "+str(self.resistencia)+" I: "+str(self.inteligencia)+" S: "+str(self.suerte)
        return(msg)
class consumibles:
    def __init__ (self,nombre,stock,stat,cantidad,tiempo):
        self.nombre=nombre
        self.stock=stock
        self.stat=stat
        self.cant=cantidad
        self.tiempo=tiempo
    def quitar_stock(self):
        self.stock-=1
class equipamiento:
    def __init__(self,nombre,atributo,bonificador):
        self.nombre=nombre
        self.atributo=atributo
        self.bonificador=bonificador
consumibles_uti=[]
equip_uti=[]
guardar=[]
vidatotal_perdida=0
tiempo_total=0
n_archivo="base.txt"
archivo=open(n_archivo,"r")
x=archivo.readlines()
pers_inicial=x[0].strip().split(",")
elementos=x[1].strip().split(",")
cantconsu=int(elementos[0])
cantequip=int(elementos[1])
i=0
l_consumibles=[]
l_equip=[]
l_pruebas=[]
while i<cantconsu:
    y=x[i+2].strip().split(",")
    consumible=consumibles(y[0], int(y[1]), y[2], int(y[3]), int(y[4]))
    l_consumibles.append(consumible)
    i+=1
i=0
while i<cantequip:
    y=x[i+2+cantconsu].strip().split(",")
    equip=equipamiento(y[0], y[1], float(y[2]))
    l_equip.append(equip)
    i+=1
i=cantequip+2+cantconsu
while i<len(x):
    y=x[i].strip().split(",")
    pruebas=prueba(y[0], int(y[1]), int(y[2]), int(y[3]), int(y[4]), int(y[5]), y[6])
    l_pruebas.append(pruebas)
    i+=1
archivo.close()
print("¡Bienvenido a la simulación de pruebas!")
nombre_per=input("Por favor escribe el nombre de tu personaje: ")
print("Muy bien",nombre_per,"Te informo que posees:")
print(pers_inicial[0],"puntos de Vida base")
print(pers_inicial[1],"puntos de tiempo")
print(pers_inicial[2],"puntos para gastar en stats iniciales")
print("¿Como quieres repartir tus puntos?")
cont=True
tiempo=int(pers_inicial[1])
while cont:
    vida=int(pers_inicial[0])
    puntos=int(pers_inicial[2])
    vida1=int(input("Vida: "))
    vida+=vida1
    puntos-=vida1
    if puntos>0:
        destreza=int(input("Destreza: "))
        puntos-=destreza
    if puntos>0:
        resistencia=int(input("Resistencia: "))
        puntos-=resistencia
    if puntos>0:
        inteligencia=int(input("Inteligencia: "))
        puntos-=inteligencia
    if puntos>0:
        suerte=int(input("Suerte: "))
        puntos-=suerte
    else:
        print("Lo sentimos esa cantidad excede lo que tienes disponible.")
        print("Empezaremos de nuevo por si te equivocaste al repartir.")
    if puntos==0:
        cont=False
    elif puntos>0:
        print("¡Te sobraron puntos! Dadas tus malas matemáticas, te las asignaremos a Suerte (puede que la necesites).")
        suerte+=puntos
        puntos-=suerte
        cont=False
per=personaje(nombre_per,vida,tiempo,destreza,resistencia,inteligencia,suerte)
guardar.append(nombre_per)
stats1=str(vida)+","+str(destreza)+","+str(resistencia)+","+str(inteligencia)+","+str(suerte)+","+str(tiempo)
guardar.append(stats1)
sim=simulacion()
sim.agregar_personaje(per)
for i in l_pruebas:
    sim.agregar_prueba(i)
print("Tus stats iniciales son:")
print("Vida:",vida,"Destreza:", destreza, "Resistencia:", resistencia,"Inteligencia:",inteligencia,"Suerte:",suerte)
print("\n")
print("Aquí está el listado de todos los equipamientos que hay. elige un número para equiparlo")
print("En caso de que ya no quieras equiparte más ingresa -1","\n")
cont=True
n_equip=[]
conta=0
while cont:
    for i in range(0,len(l_equip)):
        cont1=True
        for j in n_equip:
            if i==j:
                cont1=False
        if cont1:
            print(str((i+1))+".-",l_equip[i].nombre,"Bonificador",l_equip[i].bonificador,"a",l_equip[i].atributo)                  
    equip=int(input())
    cont1=True
    if equip==-1:
        cont=False
    else:
        for i in n_equip:
            if i == (equip-1):
                print("Ya equipaste ese objeto")
                cont1=False
        if cont1:
            n_equip.append(equip-1)
            sim.agregar_equipo(l_equip[equip-1])
            equip_uti.append(l_equip[equip-1].nombre)
            conta+=1
    if conta==3:
        cont=False
cont_final=0
while cont_final<3:
    sim.reiniciar_consumibles()
    sim.calcular_stats()
    print("Stats actuales:",sim)
    print ("Tiempo disponible",tiempo)
    print("Aquí están los consumibles. selecciona el número del objeto que deseas")
    print("para comenzar la evaluacion ingresa -1","\n")
    cont=True
    n_consu=[]
    conta=0
    while cont:
        for i in range(0,len(l_consumibles)):
            if l_consumibles[i].stock>0:
                print(str((i+1))+".-","("+str(l_consumibles[i].stock)+")",l_consumibles[i].nombre,":",l_consumibles[i].tiempo,"de tiempo",l_consumibles[i].cant,"de",l_consumibles[i].stat)
        consu=int(input())
        cont1=True   
        if l_consumibles[consu-1].stock<=0:
            print("No te quedan disponibles")
        if consu==-1:
            cont=False
        if consu!=-1:
            tiempo-=l_consumibles[consu-1].tiempo
            if(tiempo>=0)and l_consumibles[consu-1].stock>0:
                l_consumibles[consu-1].quitar_stock()
                sim.agregar_consumibles(l_consumibles[consu-1])
                consumibles_uti.append(l_consumibles[consu-1].nombre)
                sim.calcular_stats()
                tiempo_total+=l_consumibles[consu-1].tiempo
                print("Stats actuales:",sim)
                print ("Tiempo disponible",tiempo)
            else:
                tiempo+=l_consumibles[consu-1].tiempo
    print("Stats actuales:",sim,"\n")
    per.descontar_tiempo(tiempo)
    print("¡Llegó la hora de la evaluacíon!")
    print("Preparate",per.nombre,"para enfrentar la Interrogacíon de",l_pruebas[cont_final].nombre,"(Música dramática)")
    print("Esta prueba posee",l_pruebas[cont_final],"y es debil contra la",l_pruebas[cont_final].debilidad,"¿Podrás superarla?","\n")
    print("2 semanas después","\n")
    vida_perdida=sim.dar_prueba(l_pruebas[cont_final],per,cont_final)
    vida+=vida_perdida
    vidatotal_perdida+=abs(vida_perdida)
    per.descontar_vida(vida)
    if vida>0:
        if vida_perdida<0:
            print("¡Si lo lograste! pero perdiste",abs(vida_perdida),"puntos de vida")
        elif vida_perdida==0:
            print("Lo lograste y la pasaste con un 7 no pierdes vida")
    else:
        print("Perdiste",abs(vida_perdida),"puntos de vida")
        print("No te queda vida por lo que repruebas el ramo")
        cont_final=3
    cont_final+=1
sim.reiniciar_consumibles()
a,b,c,d,e=sim.calcular_stats()
stats_finales=str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(tiempo)
guardar.append(stats_finales)
n_pruebas=l_pruebas[0].nombre+","+l_pruebas[1].nombre+","+l_pruebas[2].nombre
guardar.append(vidatotal_perdida)
guardar.append(n_pruebas)
for i in l_consumibles :
    cont=0
    for j in consumibles_uti:
        if i.nombre==j:
            cont+=1
    if cont>0:
        msg1=i.nombre+","+str(cont)
        guardar.append(msg1)
for i in equip_uti:
    guardar.append(i)
guardar.append(tiempo_total)
if cont_final==3:
    print("Felicitaciones aprobaste todo")
    G=int(input("Deseas guardar la partida (1)Si (2)No"))
    if G==1:
        nombre_archivo=input("Como deseas que se llame el archivo")
        archivo=open(nombre_archivo,"w")
        for i in guardar:
            print(i, file=archivo)
        archivo.close()
