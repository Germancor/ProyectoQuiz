from Intro import *
from Clean import *
from Nivel1 import preguntasNivel1 as pn1, OpcionesNivel1 as on1, OpcionesCorrectas1 as oc1

def jugarNivel1(puntos,nivel):
    print("\033[1;33m"+"Empezamos por el nivel " + f"{nivel}" + '\033[0;m')
    time.sleep(3)
    i = 0
    while i < 5:
        print(pn1[i])
        for opcion in on1[i]:
            print(opcion)

        try:
            res = int(input("Ingrese una respuesta (1 - 4): "))
        except:
            print("\033[1;31;41m"+"Debe ingresar un número de 1 al 4"+'\033[0;m')
            time.sleep(3)
            continue
        
        if res == oc1[i]:
            print("\033[1;32m"+"Felicidades respuesta correcta. Sumas 100 puntos"+'\033[0;m')
            puntos += 100
        else:
            print("\033[1;31m"+"Lo siento, no es correcta la respuesta."+'\033[0;m')


        i += 1

        input("Presione Enter para la siguiente pregunta...")
Puntaje = 0
cont = 0
nivel = 1

clave = "manchester"

while (True):
    clave_unica = input("Ingrese clave: ")
    if clave_unica == "manchester":
        print("Contraseña correcta")
        break
    else:
        print("Contrasñeña incorecta")

inicio()
limpieza_pantalla()
jugarNivel1(Puntaje,nivel)
