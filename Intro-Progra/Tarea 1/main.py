from Tarea_1 import *
import random

root = tk.Tk()
root.geometry('{}x{}'.format("550", "650"))
app = Application(master=root)
def reiniciar_carton():
    for i in range(0,5):
        for n in range (0,5):
            app.marcar_numero(i,n,False,1)
            app.marcar_numero(i,n,False,2)
def generar_carton():
    cont1=0
    cont2=0
    while cont1<=4 or cont2<=4:
        x=random.randint(1,20)
        y=random.randint(1,20)
        if app.agregar(x) and (cont1<=4):
             app.colocar_numero(cont1,0,x,1)
             cont1+=1
        if app.agregar(y)and cont2<=4:
            app.colocar_numero(cont2,0,y,2)
            cont2+=1     
    cont1=0
    cont2=0
    while cont1<=4 or cont2<=4:
        x=random.randint(21,40)
        y=random.randint(21,40)
        if app.agregar(x) and cont1<=4:
            app.colocar_numero(cont1,1,x,1)
            cont1+=1
        if app.agregar(y)and cont2<=4:
            app.colocar_numero(cont2,1,y,2)
            cont2+=1     
    cont1=0
    cont2=0
    while cont1<=4 or cont2<=4:
        x=random.randint(41,60)
        y=random.randint(41,60)
        if app.agregar(x) and cont1<=4:
            app.colocar_numero(cont1,2,x,1)
            cont1+=1
        if app.agregar(y)and cont2<=4:
            app.colocar_numero(cont2,2,y,2)
            cont2+=1    
    cont1=0
    cont2=0
    while cont1<=4 or cont2<=4:
        x=random.randint(61,80)
        y=random.randint(61,80)
        if app.agregar(x) and cont1<=4:
             app.colocar_numero(cont1,3,x,1)
             cont1+=1
        if app.agregar(y)and cont2<=4:
            app.colocar_numero(cont2,3,y,2)
            cont2+=1      
    cont1=0
    cont2=0
    while cont1<=4 or cont2<=4:
        x=random.randint(81,99)
        y=random.randint(81,99)
        if app.agregar(x) and cont1<=4:
            app.colocar_numero(cont1,4,x,1)
            cont1+=1
        if app.agregar(y) and cont2<=4:
            app.colocar_numero(cont2,4,y,2)
            cont2+=1
def probar_ganador_ent(ptos_jug1,ptos_jug2):
    cont1=0
    cont2=0
    for n in range (0,5):
        for i in range (0,5):
            if(app.esta_marcado(n,i,1)):
                cont1+=1
            if(app.esta_marcado(n,i,2)):
                cont2+=1
    if (cont1==25):
        ptos_jug1=3
    if (cont2==25):
        ptos_jug2=3
    return (ptos_jug1, ptos_jug2)
def probar_ganador_y(ptos_jug1,ptos_jug2):
    if (app.esta_marcado(0,0,1)) and (app.esta_marcado(1,1,1)) and (app.esta_marcado(2,2,1)) and (app.esta_marcado(3,2,1)) and (app.esta_marcado(4,2,1)) and (app.esta_marcado(1,3,1)) and (app.esta_marcado(0,4,1)):
        ptos_jug1=2                                                                                                                          
    if (app.esta_marcado(0,0,2)) and (app.esta_marcado(1,1,2)) and (app.esta_marcado(2,2,2)) and (app.esta_marcado(3,2,2)) and (app.esta_marcado(4,2,2)) and (app.esta_marcado(1,3,2)) and (app.esta_marcado(0,4,2)):                                                                                                                                                                                    
        ptos_jug2=2
    return(ptos_jug1,ptos_jug2)                                                                                                                                                                                       
           
def probar_ganador_diag(ptos_jug1,ptos_jug2):
    if (app.esta_marcado(0,0,1)) and (app.esta_marcado(1,1,1)) and (app.esta_marcado(2,2,1)) and (app.esta_marcado(3,3,1)) and (app.esta_marcado(4,4,1)):
        ptos_jug1=1
    if (app.esta_marcado(0,0,2)) and (app.esta_marcado(1,1,2)) and (app.esta_marcado(2,2,2)) and (app.esta_marcado(3,3,2)) and (app.esta_marcado(4,4,2)):                                                                                                                                                
        ptos_jug2=1
    return (ptos_jug1, ptos_jug2)

def probar_numero(bolita):
    if (bolita<=20):
        for n in range (0,5):
            if (bolita == app.obtener_numero(n,0,1)):
                app.marcar_numero(n,0,True,1)
            if (bolita == app.obtener_numero(n,0,2)):
                app.marcar_numero(n,0,True,2)
    elif(bolita<=40):
        for n in range (0,5):
            if (bolita == app.obtener_numero(n,1,1)):
                app.marcar_numero(n,1,True,1)
            if (bolita == app.obtener_numero(n,1,2)):
                app.marcar_numero(n,1,True,2)
    elif(bolita<=60):
        for n in range (0,5):
            if (bolita == app.obtener_numero(n,2,1)):
                app.marcar_numero(n,2,True,1)
            if (bolita == app.obtener_numero(n,2,2)):
                app.marcar_numero(n,2,True,2)
    elif(bolita<=80):
        for n in range (0,5):
            if (bolita == app.obtener_numero(n,3,1)):
                app.marcar_numero(n,3,True,1)
            if (bolita == app.obtener_numero(n,3,2)):
                app.marcar_numero(n,3,True,2)
    else:
        for n in range (0,5):
            if (bolita == app.obtener_numero(n,4,1)):
                app.marcar_numero(n,4,True,1)
            if (bolita == app.obtener_numero(n,4,2)):
                app.marcar_numero(n,4,True,2)

def turno():
    jug1=0
    jug2=0
    n=0
    jugar=1
    monto1=app.preguntar_monto(1)
    monto2=app.preguntar_monto(2)
    if(jug1==0) and (jug2==0):
        while n==0:
            bol= random.randint(0,99)
            if app.agregar(bol):   
                app.mostrar_mensaje(bol)
                probar_numero(bol)
                jug1 ,jug2 = probar_ganador_diag(jug1 , jug2)
                jug1 ,jug2 = probar_ganador_y(jug1, jug2)
                jug1 ,jug2 = probar_ganador_ent(jug1, jug2)

                if (jug1>jug2):
                    if(jug1==1):
                        app.mostrar_mensaje("Ganador Jugador 1 por diagonal")
                        print("Ganador Jugador 1 por diagonal")
                    elif(jug1==2):
                        app.mostrar_mensaje("Ganador Jugador 1 por Y")
                        print("Ganador Jugador 1 por diagonal")
                    elif(jug1==2):
                        app.mostrar_mensaje("Ganador Jugador 1 por Entero")
                        print("Ganador Jugador 1 por Entero")
                    app.mostrar_dinero(1,monto1+2*(app.obtener_apuesta()))
                    jugar=0
                elif (jug2>jug1):
                    if(jug2==1):
                        app.mostrar_mensaje("Ganador Jugador 2 por diagonal")
                        print("Ganador Jugador 2 por diagonal")
                    elif(jug2==2):
                        app.mostrar_mensaje("Ganador Jugador 2 por Y")
                        print("Ganador Jugador 2 por diagonal")
                    elif(jug2==2):
                        app.mostrar_mensaje("Ganador Jugador 1 por Entero")
                        print("Ganador Jugador 2 por Entero")
                    app.mostrar_dinero(2,monto2+2*(app.obtener_apuesta()))
                    jugar=0
                elif(jug1==jug2) and (jug1!=0):
                    app.mostrar_mensaje("Empate")
                    print("Empate")
                    app.mostrar_dinero(1,monto1+app.obtener_apuesta())
                    app.mostrar_dinero(2,monto2+app.obtener_apuesta())
                    jugar=0
                n=1
    
    if jugar==0:
        app.mostrar_ventana(False)
        seguir=int(input("Desea seguir jugando 1-Si 2-NO"))
        monto1=app.preguntar_monto(1)
        monto2=app.preguntar_monto(2)
        if monto1!=0 and monto2!=0:
            if (seguir==1):
                t=0
                apuesta=int(input("Cuanto desea apostar? "))
                while t==0:

                    if (apuesta>monto1) and (apuesta>monto2):
                        print("Los jugadores no tienen suficiente dinero")
                        apuesta=int(input("Cuanto desea apostar? "))
                    elif (apuesta>monto1):
                        print("El jugador 1 no tiene suficiete dinero")
                        apuesta=int(input("Cuanto desea apostar? "))
                    elif (apuesta>monto2):
                        print("El jugador 2 no tiene suficiete dinero")
                        apuesta=int(input("Cuanto desea apostar?"))
                    else:
                        app.mostrar_dinero(1,monto1-apuesta)
                        app.mostrar_dinero(2,monto2-apuesta)
                        t=1
                reiniciar_carton()
                app.reiniciar_contador()
                generar_carton()
                app.reiniciar_contador()
                app.mostrar_ventana(True)
            else:
                if(monto1>monto2):
                    print("Ganador jugador 1")
                    print("Fin del juego")
                    app.cerrar_ventana()
                if(monto1<monto2):
                    print("Ganador jugador 2")
                    print("Fin del juego")
                    app.cerrar_ventana()
        elif(monto1>monto2):
            print("Al jugador 2 no le queda dinero")
            print("Ganador jugador 1")
            print("Fin del juego")
            app.cerrar_ventana()
        elif(monto1<monto2):
            print("Al jugador 1 no le queda dinero")
            print("Ganador jugador 2")
            print("Fin del juego")
            app.cerrar_ventana()


            
app.mostrar_ventana(False)
print("Hola bienvenido al BINGO")
monto=int(input("Monto inicial?"))
apuesta=int(input("Cuanto desea apostar?"))
y=0
while y==0:
    if (apuesta>monto):
        print("No tienen suficiente dinero ingrese otra apuesta")
        apuesta=int(input("Cuanto desea apostar?"))
    else:
        app.poner_apuesta(apuesta)
        app.mostrar_dinero(1,monto-apuesta)
        app.mostrar_dinero(2,monto-apuesta)
        y=1
app.mostrar_ventana(True)
app.mostrar_mensaje("Hola pulsa siguente turno para comenzar")
app.reiniciar_contador()
generar_carton()
app.reiniciar_contador()
    # ESTO NO SE TOCA
app.button.config(command=turno)
app.mainloop()


