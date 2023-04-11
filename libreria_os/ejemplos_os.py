# Paso 1: importar la libreria
import os

# metodo o funcion os.listdir()
lista_total = os.listdir()
lista_total = sorted(lista_total)

# filtrar de la lista_total solo los archivos .txt
lista_txt = []

for elemento in lista_total:
    if elemento.endswith(".txt"):
        lista_txt.append(elemento)

# otra forma de generar una lista filtrada
lista_txt_2 = [x for x in lista_total if x.endswith(".txt")]

print(lista_total)
print(lista_txt)
print(lista_txt_2)