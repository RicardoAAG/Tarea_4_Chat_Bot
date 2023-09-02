# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 22:40:50 2023

@author: super
"""

import json
from difflib import get_close_matches

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def guardar_base_de_datos(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data,file,indent=2)
        
def encontrar_mejor_candidato(usuario_pregunta: str, preguntas: list[str]) -> str or None:
    coincidencias : list = get_close_matches(usuario_pregunta, preguntas, n=1, cutoff=0.6)
    return coincidencias[0] if coincidencias else None

def obtener_respuesta_de_pregunta(pregunta:str, base_de_datos:dict) -> str or None:
    for q in base_de_datos["preguntas"]:
        if q["pregunta"] == pregunta:
            return q["respuesta"]
        
def chat_bot():
    base_de_datos: dict = cargar_base_de_datos('base_de_datos_chat_bot_aprendizaje.json')
    
    while True:
        usuario_entrada: str = input('Tu: ')
        
        if usuario_entrada.lower() == 'salir':
            break
        
        mejor_candidato: str|None = encontrar_mejor_candidato(usuario_entrada, [q["pregunta"] for q in base_de_datos["preguntas"]])
        
        if mejor_candidato:
            respuesta: str = obtener_respuesta_de_pregunta(mejor_candidato, base_de_datos)
            print(f'Bot: {respuesta}')
        else:
            print('Bot: No se la respuesta, ¿Puedes enseñarme?')
            nueva_respuesta: str = input('Escribe la pregunta o "saltar" para saltar: ')
            
            if nueva_respuesta.lower() != 'saltar':
                base_de_datos["preguntas"].append({"pregunta": usuario_entrada, "respuesta": nueva_respuesta})
                guardar_base_de_datos('base_de_datos_chat_bot_aprendizaje.json' , base_de_datos)
                print('Bot: Gracias :3, aprendí una nueva respuesta')
                

if __name__ == '__main__':
    print('Bienvenido al Chat Bot, escribe "salir" para salir')
    chat_bot()