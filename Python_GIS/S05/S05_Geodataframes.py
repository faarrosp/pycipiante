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