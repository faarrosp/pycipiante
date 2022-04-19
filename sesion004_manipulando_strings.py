# Sesion 004_manipulando_strings

'''
En esta sección aprenderemos a manipular strings, lo cual podría ser de
especial utilidad cuando queremos importar una base de datos o un archivo
Excel trabajado por alguien más y por cualquier razón debemos corregir o
manipular los registros que ahí existen para nuestros fines particulares.

Lo primero que aprenderemos es a cambiar un string a mayusculas o minusculas
'''

# en primer lugar imprimimos un string cualquiera
print("Mi nombre es Felipe")

# este texto tiene mayusculas en el inicio de la frase y en el nombre
# supongamos que queremos dejarlo todo en mayusculas
# para ello usamos el metodo .upper() justo después del string
print("Mi nombre es Felipe".upper())

# como aprendimos en sesiones pasadas, no es necesario usar el string
# completo, sino que podemos utilizar variables
frase = "Mi amigo se llama Andres"
print(frase)
print(frase.upper())

# en ocasiones queremos lograr el efecto inverso, es decir, pasar un texto
# que originalmente está en mayúsculas y lo necesitamos en minúsculas
# para ello utilizamos el método .lower() después del string o de la variable
articulo = "MANZANAS"
print(articulo)
print(articulo.lower())

# en otras ocasiones queremos que la palabra o las frases de una oración
# comiencen siempre por una mayúscula, como es el caso de títulos
# para ello usamos el método .title() después del string o variable
asunto = "reunion proyecto secreto"
print(asunto)
print(asunto.title())

# otra herramienta importante es el poder reemplazar un caracter o una frase
# completa. Por ejemplo, consideremos la siguiente frase:
frase = "Windows es el mejor sistema operativo"
print(frase)

# un fanatico de Macintosh como yo jamas podria considerar esta frase como
# cierta, por lo que voy a cambiar Windows por Macintosh
# voy a crear una nueva variable (aunque podria sobreescribir la anterior)
# si quisiera

frase_correcta = frase.replace("Windows", "Macintosh")
# aqui lo que hemos hecho es darle 2 argumentos (parametros) al método "replace"
# el primero es la palabra o string antiguo (Windows) y el segundo es la
# palabra o string nuevo (Macintosh)
print(frase_correcta)

# finalmente, hay ocasiones en que registros vienen con espacios en blanco
# por alguna casualidad, error involuntario o por un formato antiguo.
# por ejemplo:
registro = "   MANZANAS   "

# podemos eliminar estos espacios usando el metodo .lstrip() para espacios
# en la izquierda y .rstrip() para espacios en la derecha

print(registro)
print(registro.lstrip())
print(registro.rstrip())

# podemos combinar ambos efectos tambien
print(registro.lstrip().rstrip())
