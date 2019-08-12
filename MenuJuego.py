import math
import parametros
import random
import tablero as tab

class MenuJuego:
    def __init__(self, usuario):
        self.jugador = usuario     
    
    def imprimir_menu_juego(self):
        print("¡Juguemos!")
        print("[1] Descubrir baldosa" + " " + " [2] Guardar partida" + " " + " [3] Salir de la partida")
    
    def creacion_tablero(self,cantidad_legos,ancho,largo):
        #ancho hacia el lado y largo hacia abajo
        tablero = []
        for i in range (0, largo):
            tablero.append([])
            for j in range(0, ancho):
                tablero[i].append(" ")
        
        legos=0
        while legos < cantidad_legos:
            i=random.randint(0, largo-1)
            j= random.randint(0, ancho-1)
            if tablero[i][j]!="L":
                tablero[i][j]="L"
                legos += 1
            else:
                legos += 0
        tab.print_tablero(tablero)

a=MenuJuego("Dani")
a.creacion_tablero(10,11,5)
a.imprimir_menu_juego()