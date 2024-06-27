from Intro import *
from Clean import *
from Menu import *
from Nivel1 import preguntasNivel1 as pn1, OpcionesNivel1 as on1, OpcionesCorrectas1 as oc1

    #***Desarrollo de nivel***
def jugar_nivel(preguntas, opciones, respuestas_correctas, nivel):
    print(f"\033[1;33mEmpezamos por el nivel {nivel}\033[0;m")
    time.sleep(3)
    puntos = 0

    for i in range(len(preguntas)):
        print(f"\nPregunta {i + 1}: {preguntas[i]}")
        for opcion in opciones[i]:
            print(opcion)

        while True:
            try:
                res = int(input("Ingrese una respuesta (1 - 4): "))
                if res < 0 or res > 4:
                    print("\033[1;31;41mDebe ingresar un número entre 1 y 4\033[0;m")
                    continue
                break
            except ValueError:
                print("\033[1;31;41mDebe ingresar un número de 1 al 4\033[0;m")

        if res == respuestas_correctas[i]:
            print("\033[1;32m¡Felicidades! Respuesta correcta. Sumas 100 puntos\033[0;m")
            puntos += 100
        else:
            print("\033[1;31mLo siento, no es correcta la respuesta.\033[0;m")

        # Mostrar puntaje después de cada pregunta
        print(f"Puntaje actual: {puntos}")

        # Preguntar si desea continuar jugando o volver al menú
        if i < len(preguntas) - 1:
            continuar = input("\nPresione Enter para la siguiente pregunta, o 'm' para volver al menú pero perdera los puntos: ").lower()
            if continuar == 'm':
                puntos = 0
                return puntos
            
        limpieza_pantalla()

    return puntos

def jugar_juego():

    #***Ingresar clave para jugar***
    clave = "manchester"

    while (True):
        clave_unica = input("Ingrese clave: ")
        if clave_unica == "manchester":
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorecta")
    limpieza_pantalla()

    puntaje = 0
    inicio()
    limpieza_pantalla()
    while True:
        mostrar_menu_niveles()
        nivel = elegir_nivel(puntaje)
        limpieza_pantalla()
    #***Jugar nivel seleccionado***
        if nivel == 0:
            break
        elif nivel == 1:
            puntaje += jugar_nivel(pn1,on1,oc1,"1")
# elif nivel == 2:
#     Puntaje = jugar_nivel(pn2,on2,oc2,"2")
# elif nivel == 3:
#     Puntaje = jugar_nivel(pn3,on3,oc3,"3")
# elif nivel == 4:
#     Puntaje = jugar_nivel(pn4,on4,oc4,"4")
        

    print(f"\n¡Felicidades! Has completado el juego con un puntaje total de {puntaje} puntos.")

jugar_juego()