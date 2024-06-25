#Menu de niveles
#Versión 2.0
import time

def mostrar_menu_niveles():
    print("\033[1;37;40m"+"\n======= MENÚ DE NIVELES =======")
    print("Por favor, elige un nivel:")
    print("1. Nivel fácil ")
    print("2. Nivel medio (Requiere más de 700 puntos)")
    print("3. Nivel difícil (Requiere más de 1400 puntos)")
    print("4. Nivel experto (Requiere más de 2100 puntos)")
    print("0. Salir"+'\033[0;m')

def elegir_nivel(puntos):
    while True:
        try:
            opcion = int(input("\nIngrese el número del nivel que desea jugar (0 para salir): "))
            if opcion == 0:
                print("Saliendo del juego...")
                break
        except:
            print("\033[1;31;41m"+"Debe ingresar un número del 0 al 4"+'\033[0;m')
            time.sleep(3)
            continue
            
        if puntos < 700 and opcion != 1:
                print("\033[1;31;41m¡No tienes suficientes puntos para desbloquear este nivel!\033[0;m")
                continue
        elif puntos < 1400 and opcion > 2:
                print("\033[1;31;41m¡No tienes suficientes puntos para desbloquear este nivel!\033[0;m")
                continue
        elif puntos < 2100 and opcion > 3:
                print("\033[1;31;41m¡No tienes suficientes puntos para desbloquear este nivel!\033[0;m")
                continue
        
        if opcion == 1:
            print("Has elegido el nivel fácil. Comenzando juego...")
        elif opcion == 2:
            print("Has elegido el nivel medio. Comenzando juego...")
        elif opcion == 3:
            print("Has elegido el nivel difícil. Comenzando juego...")
        elif opcion == 4:
            print("Has elegido el nivel experto. Comenzando juego...")
        
    return opcion