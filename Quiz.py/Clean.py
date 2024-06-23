#Limpieza de pantalla

import platform
import os
import time

def limpieza_pantalla():
    time.sleep(5)
    if platform.system() == 'nt':
        os.system('cls')
    

#Llamado de funcion
limpieza_pantalla()