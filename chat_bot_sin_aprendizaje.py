# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:26:43 2023

@author: super
"""

import re

def probabilidad_de_mensaje(mensaje_usuario, palabras_reconocidas, respuesta_unica=False, palabras_requeridas=[]):
    probabilidad=0
    tiene_palabras_requeridas=True
    
    
    #cuenta la cantidad de palabras clave en el mensaje
    for palabra in mensaje_usuario:
        if palabra in palabras_reconocidas:
            probabilidad+=1
    
    #calcula el procentaje de dichas palabras en el mensaje
    porcentaje=float(probabilidad)/float(len(palabras_reconocidas))
    
    for palabra in palabras_requeridas:
        if palabra not in mensaje_usuario:
            tiene_palabras_requeridas=False
            break
        
    if tiene_palabras_requeridas or respuesta_unica:
        return int(porcentaje*100)
    else:
        return 0
    
def checar_mensajes(mensaje):
    lista_max_probabilidad={}
    
    def respuesta(bot_respuesta, lista_de_palabras, respuesta_unica=False, palabras_requeridas=[]):
        nonlocal lista_max_probabilidad
        lista_max_probabilidad[bot_respuesta]= probabilidad_de_mensaje(mensaje, lista_de_palabras, respuesta_unica, palabras_requeridas)
        
    
    #Respuestas--------------------------------------------------------------------------------------------
    respuesta('Hola', ['hola', 'hi'], respuesta_unica=True)
    respuesta('Muy bien, y tu?', ['como', 'estas'], palabras_requeridas=['como'])
    respuesta('De lo que tu quieras hablar', ['de', 'que', 'te', 'hablar', 'gustaria', 'quieres'], palabras_requeridas=['de','que','hablar'])

    mejor_candidato=max(lista_max_probabilidad, key=lista_max_probabilidad.get)
    #print(lista_max_probabilidad)
    
    return mejor_candidato

def obt_respuesta(entrada):
    separar_mensaje=re.split(r'\s+|[,;?!.-]\s*',entrada.lower())
    respuesta = checar_mensajes(separar_mensaje)
    return respuesta


#Probar el sistemas de respuesta
while True:
    print('Bot: ' + obt_respuesta(input('You: ')))