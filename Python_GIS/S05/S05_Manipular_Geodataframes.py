#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 20:05:14 2022

@author: felipearrospide
"""

# En esta sesión aprenderemos a manipular un archivo vectorial mediante
# el uso de geopandas. Veremos como filtrar campos, realizar algunos cálculos
# y finalmente plotear variables de interés en un mapa

# Requisitos:
#    librería geopandas instalada
#    un archivo .shp, preferiblemente uno de líneas o polígonos

# primero importamos las librerias de utilidad
import os
import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt
import contextily as ctx

# 1 - Importamos el archivo shape a utilizar dandole la ruta exacta o relativa
path = os.path.join('..', 'shapes','PROVINCIA','PROVINCIAS_2020.shp')
gdf = gpd.read_file(path)

# imprimamos el sistema de coordenadas para verificar que sea uno UTM (proyectado)
print(gdf.crs)

# en caso de que no sea proyectado, podemos reproyectarlo a uno que nos convenga
# en este caso, usaré EPSG:32719 que es adecuado para Chile. 
gdf = gdf.to_crs('EPSG:32719')

# 2 - primeros pasos: conociendo el geodataframe

# lo primero que podemos hacer es saber el tamaño de nuestro dataframe, para
# ello, usamos el metodo shape. Esto nos dirá el número de filas y columnas
# que tiene

print(gdf.shape)

# también podemos darle una rápida vista al dataframe al ejecutar el metodo
# .head(N)
# donde N representa el numero de filas que queremos ver. Por defecto, es
# decir .head() imprime 5 filas y una cantidad limitada de columnas

print(gdf.head())
print(gdf.head(10))

# lamentablemente nuestro geodataframe es grande por lo que no podemos ver de
# forma simple nuestros campos. Lo que podemos hacer es imprimir todas las
# columnas o campos de nuestro geodataframe. Eso lo podemos lograr a través
# del método .columns, lo que nos dará un objeto del tipo "index"

print(gdf.columns)
print(type(gdf.columns))

# finalmente si aun asi son demasiados atributos, podemos hacer un objeto
# del tipo lista para guardar los nombres de las columnas

columnas = list(gdf.columns)

# importante notar que un geodataframe siempre tendra una columna llamada
# "geometry", que es la que guarda el objeto geometrico de nuestro shapefile
# estos objetos vienen de la libreria shapely, por lo que pueden ser un
# POINT, POLYGON, MULTIPOLYGON, STRING, MULTISTRING o una combinacion de todos
# ellos

# podemos verificarlo imprimiendo el tipo de elementos en la columna "geometry"

for x in gdf['geometry']:
    print(type(x))

# 3 - trabajando con una porción del geodataframe

# usualmente ocurre que queremos trabajar con solo una parte del geodataframe
# para ello debemos tener claro que parte del geodataframe queremos aislar
# de esta forma podemos crear una copia de una porcion especifica de este
# geodataframe para poder trabajarla


# en este caso en particular vamos a trabajar con aquellas provincias que 
# pertenezcan a la region de Coquimbo, para ello, podemos usar un filtro

# primero imprimamos el atributo REGION

# podemos hacerlo con punto 
print(gdf.REGION)

# o con la notacion de parentesis cuadrado
print(gdf['REGION'])

# definimos el filtro de esta forma
filtro = gdf['REGION'] == 'Coquimbo'

# y creamos una copia del geodataframe pero que solo tenga lo que queremos
# filtrar

gdf_filtrado = gdf[filtro].copy()

# podemos comprobar que tenemos un subconjunto al hacer un .head() o plotearlo

print(gdf_filtrado.head())
gdf_filtrado.plot(fc='none',ec='red')

# para terminar, obtengamos algunas mediciones, por ejemplo el perímetro de 
# cada provincia y la superficie de cada provincia

print(gdf_filtrado.length)

# los numeros que nos entrega, ¿como sabemos si son metros, kilometros, millas
# etc?
# la respuesta está en el sistema coordenado de referencia que estamos
# utilizando. En este caso, transformamos todo en un principio a UTM, y 
# UTM tiene la propiedad de estar expresado en metros, por lo que las unidades
# que estamos obteniendo son en metros

# obtengamos la superficie tambien

print(gdf_filtrado.area)

# en este caso la superficie es en metros cuadrados (m2), por el mismo 
# raciocinio anterior

# ahora, queremos guardar todo este avance, por lo que para lograrlo
# necesitamos guardar este nuevo geodataframe junto con los cálculos
# que hemos realizado

# podemos crear nuevos campos usando la misma notación de pandas

gdf_filtrado['perimetro (m)'] = gdf_filtrado.length
gdf_filtrado['superficie (m2)'] = gdf_filtrado.area

# finalmente guardamos este geodataframe como .shp

gdf_filtrado.to_file('provincias_coquimbo.shp')

# de esta manera el archivo queda grabado en el mismo directorio de donde 
# tengamos nuestro script




