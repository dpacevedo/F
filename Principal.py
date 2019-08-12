import MenuInicio as MI

#Código principal

nombre_usuario= str(input("¡Bienvenide al juego! Ingrese su nombre de usuario:"))
partida= MI.MenuInicio(nombre_usuario)

#Comienza el juego

opcion = partida.imprimir_menu()
if opcion == 1:
    info = partida.nueva_partida()
    cant_legos = info[0]
    ancho = info[1]
    largo = info[2]
        
elif opcion == 2:
    partida.cargar_partida()
elif opcion == 3:
    partida.ranking_puntajes()
elif opcion == 4:
    partida.cerrar_programa(100) #cambiar puntaje


