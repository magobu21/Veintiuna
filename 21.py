##### JUEGO DE 21 #####
#MAURICIO GONZALEZ
#CLASE DE INFORMATICA

###librerias
import random

###Funcion barajar = Prepara la baraja, la revuelve y reparte juego inicial
def barajar():
    baraja=[]
    valor=["02","03","04","05","06","07","08","09","10"," J"," Q"," K","A"]
    palo=["P", "C", "T", "D"]
    for i in valor:
        for j in palo:
            carta = "{}{}".format(i,j)
            baraja.append(carta)
    random.shuffle(baraja) 
    return baraja

###funcion contar = Determina el valor en puntos de cada carta
def contar (val):
    if val[0]=='A':
        return 11
    elif val[0]== ' ':
        return 10
    else:
        return int(val[0:2])

###Funcion repartir carta = entrega una carta y devuelve la sumatoria en [0] . En [1] marca si hay un AS
def repartircarta(J,B,n):
    if len(J)==0:
        J.append(contar(B[n]))
        w=(B[n])
        if w[0]=='A':
            J.append(1)
        else:
            J.append(0)    
        J.append(B[n])
    else:
        J[0] = (J[0] + contar(B[n]))
        w=(B[n])
        if w[0]=='A':
            J[1] = 1
        J.append(B[n])
    
    if J[0]>21 and J[1]==1:
        J[0]= J[0]-10
        J[1]=0
    return J


##VARIABLES GLOBALES
n = 1
J1=[]
J2=[]

###MAIN
print ("\n ")
print ("\n ")
print ("\n ")
print ("\nJUEGO DE 21")
BAR = barajar()                                     #se crea la baraja y se revuelve
#print(BAR)

while (1>0):
    J1 = repartircarta(J1,BAR,n)                    #reparte carta a jugador 1
    if len(J2) < 4:
        J2 = repartircarta(J2,BAR,n+1)              #le reparte dos cartas a la casa

    n +=2
    print ("\nTUS JUEGO ES... ", J1)
    #print ("\nEL JUEGO DE LA CASA ES... ", J2)
    if J1[0] > 21:
            print ("\nTE PASASTE DE 21... PERDISTE")
            break

    if len(J1) > 3:                                 #ofrece cartas cuando ya se tienen dos en la mano
        print ("\n Oprima cualquier tecla para recibir otra carta, o ""p"" para plantarse...")
        if input()=="p":
            print ("LAS CARTAS DE LA CASA SON... ", J2)
            if (J1[0] > J2[0]):
                print ("\nHAS GANADO")
                break
            else: 
                print ("\nHAS PERDIDO")
                break

