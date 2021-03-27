from principal import *
from configuracion import *

import random
import math

def lectura(listaPalabras,listaDefiniciones): #cargar en las listaPalabras las palabras y en listaDefiniciones las definiciones
    f = open("diccionario.txt", "r")
    d = f.readlines()
    agregar_palabra = ""
    agregar_definicion = ""
    largo = len(d)
    for k in range(largo):
        cont = 0
        for palabra in d[k]:
            if cont == 0:
                if palabra != ":":
                    agregar_palabra += palabra
            if palabra == ":":
                cont = 1
            if cont == 1:
                if palabra != ":":
                    agregar_definicion += palabra
        listaPalabras.append(agregar_palabra)
        listaDefiniciones.append(agregar_definicion)
        agregar_palabra = ""
        agregar_definicion = ""
    f.close
    pass

def eligeLaPalabra(listaPalabras,cadenaDe2Letras): #elige de la lista de palabras una que contiene estas letras
    cont = 0
    seguir = True
    while seguir:
        if listaPalabras[cont] != 0:
            for k in range(len(listaPalabras[cont])):
                if cadenaDe2Letras[0] in listaPalabras[cont]:
                    if cadenaDe2Letras[1] in listaPalabras[cont]:
                        x = listaPalabras[cont]
                        seguir = False
        cont += 1
    return x
def damePosicion(palabra,listaPalabras): #devuelve la posicion de un elemento en una lista de elementos
    largo = len(listaPalabras)
    for k in range(largo-1):
        if listaPalabras[k] == palabra:
            x = k
    return x

def dameDefinicion(palabra,listaPalabras,listaDefiniciones): #devuelve la definicion de la palabra
    if esta(palabra,listaPalabras):
        largo = len(listaPalabras)
        for k in range(largo):
            if listaPalabras[k] == palabra:
                x = k
    return listaDefiniciones[x]

def azar(listaPalabras): #elige 2 letras al azar
    cont = 0
    letras = ""
    seguir = True
    while seguir:
        num = random.randint(0,len(listaPalabras) - 1) #toma un numero al azar
        palabraAzar = listaPalabras[num] #toma una palabra al azar de la listaPalabras
        if palabraAzar != 0:
            seguir = False
    continuar = True
    while continuar:
        x = palabraAzar[random.randint(0,len(palabraAzar) - 1)]
        if x not in letras:
            letras = letras + x
            if len(letras) == 2:
                continuar = False
    return letras

def puntuar(candidata,palabra): #suma puntos si es correcta, suma puntos distintos para vocales, consonantes faciles, consonantes dificiles y longitud.
    puntos = 0
    if candidata == palabra:
        vocales = "aeiou"  #cada vocal otorga un punto
        consonantesDificil = "j,k,q,w,x,y,z"  #cada consonante dificil otorga 5 puntos
        for letras in palabra:
            if letras in vocales:
                puntos = puntos + 1
            elif letras in consonantesDificil:
                puntos = puntos + 5
            else:
                puntos = puntos + 2 #cada consonante otorga 2 puntos
    elif candidata == "1":
        puntos = puntos - 10
    return puntos


def esCorrecta(candidata, palabra): # Devuelve verdadero si acierta falso en caso contrario
    if candidata == palabra:
        resultado = True
    else:
        resultado = False
    return resultado

def esta(palabra, listaPalabras):
    seguir = True
    cont = 0
    veces = 0
    while seguir:
        if palabra == listaPalabras[cont]:
            veces += 1
            valor = True
            seguir = False
        cont +=1
        if cont > (len(listaPalabras) - 1):
            seguir = False
    if veces == 0:
        valor = False
    return valor

def evitarRepeticion(palabra,listaPalabras,listaDefiniciones):
    for k in range(len(listaPalabras)):
        if listaPalabras[k] == palabra:
            listaPalabras[k] = 0
            listaDefiniciones[k] = 0