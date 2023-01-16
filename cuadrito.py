import pygame, sys
from Juego import *
from time import sleep
from random import randint

file=open(r"C:\Users\Gabri\OneDrive\Documentos\Universidad\E. de datos\Arboles\laberinto_1.in")
filas, columnas = map(int, file.readline().split())
matriz = file.readlines()

pygame.init()
ancho_pantalla, alto_pantalla = 500, 400
tam_pantalla = (ancho_pantalla, alto_pantalla)
pantalla = pygame.display.set_mode(tam_pantalla, 0, 32)

color_piso= 252, 252 , 252
color_pared= 0, 0, 0
color_salida= 250, 12 ,12
color_meta = 12, 210, 34
verde_pensamiento = 10, 100, 30
color_recorrido = 120, 120, 34
color_rastro= 60, 70, 80


def dummy():
    recorrido=[(2,1)]
    return recorrido

recorrido=dummy()
n=10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(filas):
        for j in range(columnas):
            ancho, alto = ancho_pantalla/columnas,alto_pantalla/filas
            esq_izquierda, esq_superior = i*ancho, j*alto
            posicion=(esq_izquierda, esq_superior, ancho, alto)

            if matriz[i][j]=="1":
                color=color_piso
            elif matriz[i][j]=="0":
                color=color_pared
            elif matriz[i][j]=="A":
                color=color_salida
            elif matriz[i][j]=="B":
                color = color_meta
            pygame.draw.rect(pantalla, color, posicion)
        sleep(.1)
        pygame.display.update()


    for x in range(n):
        i, j = recorrido[x]
        color=color_rastro
        esq_izquierda, esq_superior = j*ancho, i*alto
        posicion=(esq_izquierda, esq_superior)
        

    i, j = recorrido[n]
    color=color_recorrido
    esq_izquierda, esq_superior = j*ancho, i*alto
    posicion=(esq_izquierda, esq_superior)
    pygame.draw.rect(pantalla,color,posicion)
    n=(n+1)%5


