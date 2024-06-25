#Menu de niveles
#Versión 1.0
import time

def mostrar_menu():
    print("\033[1;37;40m"+"Bienvenido al juego!")
    print("Por favor, elige un nivel:")
    print("1. Nivel fácil")
    print("2. Nivel medio")
    print("3. Nivel difícil")
    print("4. Nivel experto")
    print("0. Salir"+'\033[0;m')

def elegir_nivel(opcion):
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except:
            print("\033[1;31;41m"+"Debe ingresar un número del 0 al 4"+'\033[0;m')
            time.sleep(3)
            continue
    
        if opcion == '1':
            print("Has elegido el nivel fácil. Comenzando juego...")
        elif opcion == '2':
            print("Has elegido el nivel medio. Comenzando juego...")
        elif opcion == '3':
            print("Has elegido el nivel difícil. Comenzando juego...")
        elif opcion == '4':
            print("Has elegido el nivel experto. Comenzando juego...")
        elif opcion == '0':
            print("Saliendo del juego...")
            break

