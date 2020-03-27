nprimo=0
n=0
x=int(input("N-esimo primo: "))
while(n<7919):
    n+=1
    div=0
    cont=0
    while(cont<=n):
        cont=cont+1
        if(n%cont==0):
            div=div+1
    if(div==2):
        nprimo+=1
        if(x==nprimo):
            print(n)
            print("programa Acabado")

    
