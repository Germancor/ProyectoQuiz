def inicio():
    # Logo del juego con asteriscos y colores ANSI
    logo = """
\033[1;33;40m  
//  #####   ##   ##   ####    #######             ####    ####    ######    ####      ####   #######  ##   ##
// ##   ##  ##   ##    ##     #   ##             ##  ##    ##     # ## #     ##      ##  ##   ##   #  ###  ##
// ##   ##  ##   ##    ##        ##             ##         ##       ##       ##     ##        ## #    #### ##
// ##   ##  ##   ##    ##       ##              ##         ##       ##       ##     ##        ####    ## ####
// ##   ##  ##   ##    ##      ##               ##         ##       ##       ##     ##        ## #    ##  ###
// ##  ###  ##   ##    ##     ##    #            ##  ##    ##       ##       ##      ##  ##   ##   #  ##   ##
//  #####    #####    ####    #######             ####    ####     ####     ####      ####   #######  ##   ##
//     ###

\033[1;37;40mBienvenido al Quiz de Fútbol!
==============================================
Instrucciones:
Responde correctamente tantas preguntas como puedas.
Cada respuesta correcta suma puntos.
Debe ingresar como respuesta numeros entre 1 - 4.
¡Diviértete y demuestra cuánto sabes!
"""+'\033[0;m'

    # Imprimir el logo
    print(logo)

    input("Presione enter para continuar...")