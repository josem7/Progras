def comprobar1 (palabra,texto):
    x=len(palabra)-1
    msg1=False
    msg2=False
    palabrainv=""
    while x>=0:
        palabrainv+=palabra[x]
        x-=1
    if palabra in texto:
        msg1=True
    if palabrainv in texto:
        msg2=True
    print(palabrainv)
    return (msg1,msg2)
palabra=input("Palabra")
texto= input("Texto")
msg1,msg2=comprobar1(palabra,texto)
if msg1:
    print("Alerta")
if msg2:
    print("Alerta Inverso")
