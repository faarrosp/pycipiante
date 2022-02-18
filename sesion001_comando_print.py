# Bienvenidos a esta primera sesion de programacion en Python

# Nuestra primera interaccion con la consola sera imprimir un mensaje
print('Hola a todos, mi nombre es Felipe')

# como podemos observar, el comando "print" toma colores especiales
# distintos a los parentesis y al mensaje mismo
# "print" es una "palabra protegida", porque Python las interpreta
# como comandos

# otras palabras protegidas son:

# print
# int
# if
# else
# with
# class 
# def
# import
# from

# etc... 

# para poder hacer comentarios (escribir libremente en un script)
# simplemente usamos el hash o "gato"

# intentemos imprimir otro mensaje

print("Tengo 32 años y naci en Santiago")

# imaginemos que queremos ahora imprimir en pantalla el mismo mensaje
# pero ahora con otra edad y otra ciudad, por ejemplo:

print('Tengo 28 años y naci en Curico')

# imaginemos que ahora tenemos un grupo de personas sobre los cuales
# queremos escribir sus nombres y edades:

# Felipe, 32
# Alan, 34
# Sebastian, 33

# queremos escribir algo asi como:
# Me llamo A y mi edad es B
# notamos que solo los nombres y las edades cambian, el resto del
# mensaje es exactamente el mismo

# para hacer esto menos tedioso, introducimos el uso de variables
# una variable permite asignar un objeto a un nombre (variable)
# inventado por nosotros, para luego hacer referencia a este

# esto permite ejecutar comandos más rápidamente y tener un código
# más limpio

# la sintaxis es la siguiente

# variable = objeto

# veamos un ejemplo

variable = "Mi nombre es Felipe y tengo 32 años"

# a la palabra "variable" le hemos asignado el objeto
# "Mi nombre es Felipe y tengo 32 años"

# ahora podemos simplemente imprimir la frase haciendo referencia
# a la variable

print(variable)

# si bien hemos separado la tarea en 2 lineas, por un poco mas de
# texto, el codigo queda mas claro, mas funcional y simple de
# entender

# ahora quisieramos reemplazar los nombres y edades en el mensaje

# partamos con aprender que el comando "print" permite multiples
# argumentos, los cuales se separan con coma ","

print("Mi nombre es Felipe", "y tengo 32 años")

# notemos que ambas frases entre comillas se imprimieron con un
# espacio entre ellas, esto es una caracteristica del comando
# "print"

# ahora esto aun no tiene mucha utilidad, solo hemos separado
# el mensaje en 2. Como integramos el uso de variables?

# podemos separar lo que se repite de lo que no. creemos una
# variable llamada "nombre" y una variable llamada "edad"

nombre = "Felipe"
edad = 32

# estas variables las podemos integrar al comando "print"

print("Mi nombre es", nombre, "y tengo", edad, "años")

# podemos sobre-escribir las variables cuantas veces 
# queramos, aunque siempre hay que tener cuidado de si 
# efectivamente queremos sobre-escribir, o crear nuevas
# variables

nombre = "Alan"
edad = 34

# Para imprimir el mismo mensaje anterior pero con los datos
# de Alan, solo basta con haber modificado las variables
# y copiar la linea 96

print("Mi nombre es", nombre, "y tengo", edad, "años")

# si no queremos perder los valores guardados en las variables
# tenemos que crear nuevas

nombre2 = "Sebastian"
edad2 = "33"

# imprimamos los nombres de Alan y Sebastian

print("Mi nombre es", nombre, "y tengo", edad, "años")
print("Mi nombre es", nombre2, "y tengo", edad2, "años")

# perfecto

# tal vez no se vea muy util por ahora, pero mas adelante
# aprenderemos a crear listas y como recorrerlas para lograr
# resultados muy sorprendentes

# por ejemplo: copia el siguiente codigo desde la linea 134
# hasta la linea 139 y ejecutalo

nombres = ['Alan', 'Felipe', 'Sebastian']
edades = [34, 32, 33]

for nom, ed in zip(nombres, edades):
	print(f"Mi nombre es {nom} y tengo {ed} años")



# con lo que sabemos hasta ahora, nuestro trabajo habria sido:

nombre1 = "Alan"
nombre2 = "Felipe"
nombre3 = "Sebastian"

edad1 = 34
edad2 = 32
edad3 = 33

print("Mi nombre es", nombre1, "y tengo", edad1, "años")
print("Mi nombre es", nombre2, "y tengo", edad2, "años")
print("Mi nombre es", nombre3, "y tengo", edad3, "años")

# el trabajo de 9 lineas lo hicimos en 4!!!


###### TAREA/DESAFIO

# 1. Alexa, Siri y Cortana son inteligencias artificiales que
# estan programadas para saludarte cordialmente y entregarte 
# datos utiles como la temperatura, condicion del cielo,
# valor del dolar, euro y UF.

# Utilizando lo aprendido, genera el mensaje de bienvenida
# usando el comando "print" y sabiendo que el usuario se llama
# Juan, hay 25 grados, no hay nubes y el dolar subio a 850
# pesos

# 2. Juan no vive solo, vive con su esposa Elsa, su hija Dolores
# y su hijo Jose. Genera el saludo que harían estas inteligencias
# con cada uno de ellos sabiendo que Elsa quiere saber que
# ropa ponerse para salir,Dolores viaja pronto a Estados Unidos
# y Jose esta evaluando un credito hipotecario. 
# Averigua en internet los valores de 
# temperatura, dolar, UF, etc.

# Usa la menor cantidad de comandos posibles para que tu codigo
# sea limpio y facil de entender.
