# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import rasterio
import os
from matplotlib import pyplot as plt

from rasterio.plot import show

path = os.path.join('DEM', 'REGION_BIOBIO.jp2')

with rasterio.open(path, 'r') as dem:
    print('Nombre del archivo:', dem.name)
    print('Numero de bandas:', dem.count)
    print('Ancho del DEM:', dem.width)
    print('Alto del DEM:', dem.height)
    {i: dtype for i, dtype in zip(dem.indexes, dem.dtypes)}
    print('Frontera o extension del DEM:\n', dem.bounds)
    print('Sistema de referencia:', dem.crs)

    # Ahora grafiquemos nuestro DEM

    # Opcion 1: usar imshow--> muestra el plot con extents en indice matricial
    # plt.imshow(dem.read(1), cmap='viridis')
    # plt.show()
    # plt.close('all')
    # Opcion 2: usar rasterio.plot.show
    show(dem)
