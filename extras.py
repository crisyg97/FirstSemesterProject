import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    elif key == K_1:
       return("1")
    else:
        return("")


def dibujar(screen, candidata, longitud, definicion, letras, puntos, segundos,palabra):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGRANDE= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea de abajo
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #para mostrar los segundos, en rojo si quedan menos de 15
    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    #para mostrar las letras que surgieron al azar
    ren3 = defaultFontGRANDE.render(letras[0]+"  "+letras[1], 1, COLOR_TIEMPO_FINAL)

    #poscicones de las letras en la palabra
    posicionDeLetras = []
    for k in range(len(palabra)-1):
        if palabra[k] == letras[0] or palabra[k] == letras[1]:
            posicionDeLetras.append(k)

    for i in range(longitud): #muestra los _
        screen.blit(defaultFont.render("_", 1, COLOR_LETRAS), (200+TAMANNO_LETRA*2*i,350))

    #ayuda al jugador mostrando las letras al azar
    if segundos < 15:
        for i in range(longitud):
            if posicionDeLetras[0] == i:
                screen.blit(defaultFont.render(palabra[posicionDeLetras[0]], 1, COLOR_LETRAS), (200+TAMANNO_LETRA*2*i,350))
            elif posicionDeLetras[1] == i:
                screen.blit(defaultFont.render(palabra[posicionDeLetras[1]], 1, COLOR_LETRAS), (200+TAMANNO_LETRA*2*i,350))

    #muestra las letras que escribe el jugador, las ubica sobre los _
    for i in range(len(candidata)):
        screen.blit(defaultFont.render(candidata[i], 1, COLOR_LETRAS), (200+TAMANNO_LETRA*2*i,350))

    #para mostrar la definicion
    x=40
    y=60
    for letra in definicion:
        if letra == " ":
            if (x > ANCHO - 100):
                x = 40
                y = y + TAMANNO_LETRA
            elif (x > ANCHO - 200):
                x = 40
                y = y + TAMANNO_LETRA
        screen.blit(defaultFont.render(letra, 1, COLOR_LETRAS), (x,y))
        x = x + TAMANNO_LETRA

    screen.blit(ren1, (680, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (ANCHO/2-TAMANNO_LETRA, 550)) #muestra las letras que salieron al azar