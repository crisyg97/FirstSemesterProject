#! /usr/bin/env python
import os, random, sys, math
import pygame
from pygame.mixer_music import *
from pygame.locals import *
from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Diccionar.io")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        listaPalabras=[]
        listaDefiniciones=[]

        lectura(listaPalabras,listaDefiniciones)   #carga en las listas las palabras y las definiciones
        letras=azar(listaPalabras)
        palabra=eligeLaPalabra(listaPalabras,letras)    #elige de la lista de palabras las que contiene dos letra elegidas al azar
        definicion=dameDefinicion(palabra,listaPalabras,listaDefiniciones)  #busca la definicion de la palabra elegida

        while segundos > fps/1000:

        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:

            	fps = 3
            #Busscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        if candidata=="1":# si escribe 1 significa que no sabe de que palabra se trata
                            evitarRepeticion(palabra,listaPalabras,listaDefiniciones)
                            puntos += puntuar(candidata, palabra)
                            letras=azar(listaPalabras)
                            palabra = eligeLaPalabra(listaPalabras, letras)
                            #falta evitar repeticiones de la misma palabra
                        else:
                            if esCorrecta(candidata,palabra):
                                evitarRepeticion(palabra,listaPalabras,listaDefiniciones)
                                puntos += puntuar(candidata, palabra)
                                letras=azar(listaPalabras)
                                palabra = eligeLaPalabra(listaPalabras, letras)
                                #falta evitar repeticiones de la misma palabra
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo
            longitud=len(palabra)  #busca la longitud de la nueva palabra
            definicion=dameDefinicion(palabra,listaPalabras,listaDefiniciones) #busca la definicion por si la letra cambio

            dibujar(screen, candidata, longitud, definicion, letras, puntos, segundos,palabra)
            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
