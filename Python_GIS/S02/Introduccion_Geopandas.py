#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 14:03:24 2022

@author: felipearrospide
"""

import geopandas as gpd
from matplotlib import pyplot as plt

# geopandas trabaja con archivos .shp, .shx, .geojson

regiones = gpd.read_file('REGIONES_2020.shp')


fig = plt.figure()
ax = fig.add_subplot(111)
regiones.plot(ax=ax, fc='none',ec='black')
plt.title('Regiones de Chile')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
plt.show()
