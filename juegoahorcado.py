import random

palabras = [
    "casa", "perro", "gato", "calle", "libro", 
    "llave", "azul", "lunes", "leche", "sol", 
    "mesa", "flor", "pared", "tren", "raton", 
    "lapiz", "plato", "mar", "camino", "pelota"
]

palabraRandom=palabras[random.randint(0,19)]
listaPalabra=[]
for i in range(0,len(palabraRandom)):
    listaPalabra.append("_")

print("¡EMPECEMOS A JUGAR!\nTienes sólo 6 oportunidades.")
print("")

oportunidades=6
gano=False

while(oportunidades!=0):
    print("")
    palabraFinal=""
    print("OPORTUNIDADES:",oportunidades)
    for i in listaPalabra:
        print(i,end=' ')
    print("")
    letra=input("Ingresa una letra: ").lower()
    letraPos=[]
    estaLetra=False
    for i in range(0,len(palabraRandom)):
        if palabraRandom[i]==letra:
            letraPos.append(i)
            estaLetra=True
    if estaLetra==True:
        print("FELICIDADES, ENCONTRASTE UNA LETRA.")
        for i in range(0,len(letraPos)):
            listaPalabra[letraPos[i]]=letra
    else:
        print("TE EQUIVOCASTE, PERDISTE UNA OPORTUNIDAD")
        oportunidades-=1
    for i in listaPalabra:
        palabraFinal+=i
    if palabraRandom==palabraFinal:
        gano=True
        break

print("")
if gano==True:
    print("FELICIDADES, GANASTE EL JUEGO.")
else:
    print(f"Lo siento, perdiste, juega de nuevo... La palabra era {palabraRandom}")
