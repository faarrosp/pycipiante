#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:13:43 2022

@author: felipearrospide
"""

import os # libreria para navegar por carpetas
import geopandas as gpd
from matplotlib import pyplot as plt

# 1er paso: determinar la ruta (path) del archivo .shp con el cual vamos
# a trabajar

path = os.path.join('..', 'shapes', 'PROVINCIA', 'PROVINCIAS_2020.shp')

# 2do paso: asignar una variable el geodataframe

geodataframe = gpd.read_file(path)

# 3er paso: explorar el geodataframe con algunos comandos

# imprimir el sistema de coordenadas
print(geodataframe.crs)

# explorar las primeras 5 filas del geodataframe
print(geodataframe.head())

# imprimir todas las columnas
print(geodataframe.columns)

# imprimir las filas
print(geodataframe.index)

for i in geodataframe.index:
    print(i)
    
indices = geodataframe.index
columnas = geodataframe.columns

# imprimir el tamaño de nuestro geodataframe
print(geodataframe.shape)

columnas = list(geodataframe.columns)

# imprimir los nombres de un campo en particular

# a) usando la notacion .
print(geodataframe.REGION)

regiones = list(geodataframe.REGION)

# b) usando la notacion de parentesis cuadrados []

print(geodataframe['REGION'])

regiones = list(geodataframe['REGION'])

# 4to filtrar un dataframe

filtro = geodataframe['REGION'] == 'Coquimbo'

geodataframe_filtrado = geodataframe[filtro].copy()

# 5to guardar el geodataframe filtrado

geodataframe_filtrado.to_file('provincias_Coquimbo.shp')



