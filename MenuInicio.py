import math
import parametros
import os

class MenuInicio:
    def __init__(self, usuario):
        self.jugador = usuario     
    
    def imprimir_menu(self):
        print("¡Empecemos!")
        print("[1] Crear partida" + " " + " [2] Cargar partida" + " " + " [3] Ranking puntajes" + " " + " [4] Cerrar programa" + " ")
        opcion = input("Indique su opción: ")
        while opcion.isdigit()== False:
            opcion = input("Valor inválido, indique su opción: ")
        while int(opcion) not in range(1,5):
            opcion = int(input("Valor inválido, indique su opción: "))
        return int(opcion)
        
    def nueva_partida(self):
        ancho = input("Ingrese un número del 3 al 15 que indique el ancho de su tablero:") 
        while ancho.isdigit()== False:
            ancho = input("Valor inválido, ingrese un nuevo número: ")
        while not int(ancho) in range (3,16):
            print("Número inválido")
            ancho = int(input("Ingrese un número del 3 al 15 que indique el ancho de su tablero:"))

        largo = input("Ingrese un número del 3 al 15 que indique el largo de su tablero:")
        while largo.isdigit()== False:
            largo = input("Valor inválido, ingrese un nuevo número: ")
        while not int(largo) in range (3,16):
            print("Número inválido")
            largo = int(input("Ingrese un número del 3 al 15 que indique el largo de su tablero:"))

        cantidad_legos = math.ceil (ancho * largo * parametros.PROB_LEGO)
        lista1= [cantidad_legos,ancho,largo]
        return lista1

    def cargar_partida(self):
        #Verificación de la existencia del archivo
        #Añadir al readme que se debe cargar desde la carpeta T00
        path_1 = os.path.join( "partidas", str(self.jugador)+".txt")
        print(path_1)
        print(os.path.isfile(path_1))
        if  os.path.isfile(path_1) == False:  #debería ser while
            print("Esta partida no existe")

        else:
            print("Partida encontrada")
            #Volver al menú de inicio

    def ranking_puntajes(self):
        puntajes = open("puntajes.txt" , "r")
        lista_puntajes = puntajes.readlines()
        lista_puntajes.sort()
        i = 0
        while i < 10 :
            print(lista_puntajes[i])
            i += 1

    def cerrar_programa(self,puntaje):  
        print( str(self.jugador) + " " + "tu puntaje es: " + str(puntaje))  
        archivo_puntajes = open( '\Tareas\T00\puntajes.txt' , 'a')
        archivo_puntajes.write( str(puntaje) + "," + str(self.jugador) + '\n')
        archivo_puntajes.close()


a=MenuInicio("Dani")
a.cargar_partida()    
a.ranking_puntajes()        
