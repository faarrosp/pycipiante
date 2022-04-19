#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 23:33:10 2022

@author: felipearrospide
"""

import geopandas as gpd
from matplotlib import pyplot as plt
import contextily as ctx

# geopandas trabaja con archivos .shp, .shx, .geojson
# vamos a trabajar con la libreria contextily
# https://contextily.readthedocs.io/en/latest/


regiones = gpd.read_file('../shapes/REGION/REGIONES_2020.shp')
regiones_proyectada = regiones.to_crs('EPSG:32719')

maule = regiones_proyectada[regiones_proyectada['REGION']=='Maule'].copy()

fig = plt.figure()
ax = fig.add_subplot(111)
maule.plot(ax=ax, fc='none', ec='yellow')
ctx.add_basemap(ax=ax,zoom=8,crs='EPSG:32719',
                source=ctx.providers.NASAGIBS.ViirsEarthAtNight2012)
plt.show()