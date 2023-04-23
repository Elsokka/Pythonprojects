#  >>>>>> Variables : Contenedor de objetos(Espacio en memotia)

num_1 = 3  
num_2 = 4
nombre = "Facundo" 

# Tipos de datos : Enteros, Flotantes, Strings y Booleanos con estos tipos de datos podemos hacer operaciones.

num_2 = 4           #Nums
nombre = "Facundo"  #String
is_man = True       #Boleano

#Nums a detalle

num_2 = 4     #Entero
num_2 = 12.12 #Float

#String a detalles
#Los string se pueden imprimir de esta forma

print(f"Hola, mi nombre es {nombre}")


#Boleanos a detalle

is_man = True 
is_man = not True #Cambia la condición boleana

# Convertir los tipos de datos

num_1 = int(input("Escribe un numero :")) #Conviertiendo un string a entero
nombre = str(num_1)                       # Convirtiendo entero a string
print(nombre)


#---------------------------------------------------------------------------

# >>>>>>>> Operadores logicos


# %   : El restante de la operacion
# and : para comparar si y solo si dos valores son verdaderos da true
# or  : Para comparar si uno de los dos valores es verdadero da true 
# not : para invertir el valor booleano.
# ==  : Compara dos valores y te dice si son iguales o no.
# !=  : Compara dos valores y te dice sin son diferentes o no.
# >   : Compara si es mayor que otro valor.
# <   : Compara si es menor que otro valor.
# >=  : igual o mayor que el valor a comparar.
# <=  : igual o menor que el valor a comparar.
# in  : Ayuda verificar si un texto esta dentro de una cadena de caracteres
#pass : Sirve para saltar esa linea de codigo
#Triples comillas:  deja escribir una cada mas larga de caractares

#Operadores aritmeticos

# + = suma 
# - = resta 
# * = multiplicación
# ** = Exponeciación
# / = Divide


#-------------------------------------------------------------------------------

# >>>>>>>>> Condicionales 



opcion = int(input("Elige una opcion (1, 2, 3 ): "))

if opcion == 1:
    conversacion("Elegiste opcion 1")
elif opcion == 2:
    conversacion("Elegiste opcion 2")
elif opcion== 3:
    conversacion("Elegiste opcion 2")
else:
    print("El valor ingresado no corresponde a un numero valido")


#------------------------------------------------------------------------------


# >>>>>> Cadenas de caracteres


#Metodos: es una funcion especial, que existe para un tipo de dato en particular. 
#Por ejemplo, si queremos que el texto ingresado se transforme en mayusculas.
#Se ejecuta el metodo sobre la variables

nombre = "Felipe"

numero_letras = len(nombre) # Numero de caracteres del string 

nombre.upper()  # Ejecutando el metodo que hace el texto en Mayus

nombre.lower()  # Ejecutando el metodo que hace el texto en Minus

nombre.count('e')  # Cuenta las veces en que e esta en el texto

nombre.capitalize()  # Ejecutando la primera letra en mayusculas

nombre.startswith('F')  # Trae la respuesta de si el texto empieza con 

nombre.endswith('F')  # Trae la respuesta de si el texto termina con 

nombre.replace(" ", "") #Reemplaza los texto 


#----------------------------------------------------------------

# >>>>>>>> INDICES

# Permite acceder a cierto caracter en una cadena dada
# Van desde 0 e escriben entre corchetes al lado de la variable 
# y son apuntadores numericos a cada caracter.

nombre[1] # Apunta al caracter "1" de la variable
nombre[-1] #Empieza a contar en reversa

# >>>>>>>> SLICES

#Funcionan para hacer rebanadas de caracteres

nombre[1:4] # Te trae "omb" de la palabra nombre
nombre[:4] # Te trae "nomb" de la palabra nombre
nombre[2:] # Te trae "ombre" de la palabra nombre
nombre[:4:2] # Te trae "ob" de la palabra nombre por que va de 2 en 2
nombre[::-1] # Te trae "nombre" en reversa



#----------------------------------------------------------------

# >>>>>> LISTAS 

# >>>>> Almacenar varios valores en una variable

nums =[1,3,4,5,6,56,89]

# Para acceder a un objeto de mi lista debo seleccionarlo

nums =[1,3,4,5,6,56,89]

objeto = nums[2]

#metodos de las listas 

nums =[1,3,4,5,6,56,89]

nums.append(3) # agrega el objeto a lista
nums.insert(0, 4) #Inserta el dato 4 en el index 0 
nums.pop(4) # Elimina el objeto que esta en el indice 4
nums.clear() #Limpia toda la lista
nums.extend() #Une una lista con otra
nums.count() #Cuenta el numero de veces que aparece un dato en la lista
nums.index() # dice el indice en donde esta el dato a buscar
nums.remove() # Elimina el primer registro cuyo valor coincide con el que le indicamos 
nums.reverse() #Le da la vuelta a la lista 
nums.sort() # Ordena la lista de menor a mayor

#Remplazar un dato de la listas

nums[0] = 3 # Reemplaza el primer dato por 3


# Para recorrer la lista

nums = [1,2,3,4,5]

for elemento in nums: 
    print(elemento)


# Podemos de igual forma operar con listas

nums = [1,2,3,4,5]

nums_2 = [4,3,6,2,4]

lista_final = nums + nums_2

lista_finalpor5 = nums * 5


#Puedo usar los slices en las listas

nums =[1,3,4,5,6,56,89]

nums[1:4] # Trae solo los elementos en ese rango de la lista


# >>>> Tuplas 


# Objetos estaticos

mi_tupla = (2, 3, 21, 43, 53)


#Se aplican los mismo metodos de listas 



# >>>>>> Diccionarios : Una estructura de llaves y valores


#Accedemos a los elementos del diccionario a traves de la llave

mi_diccionario = {
    "Brasil" : 108_989_873,
    "Colombia" : 1_000_000,
    "Argentina" : 123_827_232,
}
print(mi_diccionario["llave 1"]) # Nos permite ir a mi diccionario, y abrr lo que esta en la llave 1


# Actualiza datos 

mi_diccionario['Brasil'] = "Peru" #Cambia la llave de Brail por peru 

mi_diccionario["Colombia"] += 10000 # Agrega 1000 a value

del mi_diccionario["Colombia"] # elimina el key y value 

mi_diccionario.pop("Colombia") # Elima el key y value 

# .items() > Trae los items en una lista de tuplas 

#  .keys()  > Retorna la clave de nuestro elemento

#  .values() > Retorna una lista de elementos (valores del diccionario)

#  .items()  > Devuelve lista de tuplas (primero la clave y luego el valor)

#  .clear()  > Elimina todos los items del diccionario

#  .pop(“n”) > Elimina el elemento ingresado


#Tambien puedo recorrer datos con for e n los diccionario

for pais in mi_diccionario.keys():
    print(pais) #Imrime la llaves del dic


for pais in mi_diccionario.values():
    print(pais) #Imrime los valoeres de la llaves del dic


for pais, poblacion in mi_diccionario.items():
    print(f"{pais} tiene la poblacion de {poblacion}") #Imprime los valores de la llaves del dic y las llaves



# ---------------------------------------------------------------

# >>>>>>> BUCLES

#Nos permite repetir un bloque de codigo de manera costante bajo unos parametro

# >>>> While

while True: #Mientras la condición se cumpla se va a ejecutar al el ciclo 
    print("Esto es un cilo infinito")
    break

# Ciclo que se ejecuta con una dos partes fundamentales
# Limite y una variable
# La pieza de codigo se ejecuta hasta que se llega al limite

def init():
    LIMIT = 100
    contador = 0
    potencia_2 = 2**contador # Inicialización 
    while potencia_2 < LIMIT:
        print(f" 2 elevado a la {contador} es igual a: {potencia_2}")
        contador = contador + 1
        potencia_2 = 2**contador



# >>>>>> FOR


for contador in range(1000):
    print(contador)

#Para el contador varia en el rango, es una variable
# Range = Rango de la variable rango(0:100)


# >>> Interrumpir un ciclo : Modificar el funcionamiento del bucle

# continue: Se salta el reto del codigo y empieza desde el principio

for contador in range(1000): #Ejemplo 1
        if contador % 2 != 0:
            continue 
        print(contador)



# Break : Finalizar un bloque de codigo

for i in range(10000):   #Ejemplo 2
        print(i)
        if i == 5778:
            break


# ---------------------------------------------------------------


# >>>>>> Funciones : Definimos una funciones que se repite y luego la invocamos.


def imprimir_mensaje():
    print("Mensaje especial: ")
    print("Estoy aprendiendo a usar funciones !")

imprimir_mensaje()

# Estas pueden tener parametros
# La funcion se ejecuta teniendo en cuenta el parametro
# El valor que le damos, asi como el impacto que tiene dentro de la funcion

def conversacion(mensaje):
    print("Hola")
    print(mensaje)


# Si queremos aprovechar el resultado de ejecutar la funcion debemos utilizar el objeto "return"

def suma(a, b):
    print("Se suman dos numeros")
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)

#Esto lo que hace es ejecutar la funcion con los parametros dados, guardar el valor producto de la ejecucion de la funcion y guardarlo en otro objeto 
#Se pueden agregar parametros por defecto 


def find_volume(length = 1,width = 1, depth = 1):
    return length * width * depth, width # nos retorna una tupla de valores 

result = find_volume(2,2,2) # si solo quioer enviar un valor (width = 1)

print(result)

# ---------------------------------------------------------------



# Conjuntos : Relacionada a la teoria de cojuntos que agrupa elementos que tiene algo en comun 

# Se pueden modificas
# No tiene orden
# No permite duplicados

set_countries = {"COL","PER", "MX","BR"}

print(set_countries)

# Generar un cojunto a partir de un string

set_from_string = set("Hola")
print(set_from_string)

#Generar un cojunto a partir de tuplas

set_from_tuplas = set(("abc", "def"))

#Generar un cojunto a partir de una lista

num = [1,2,3,4,5,1,2,3,4]

set_from_list = set(nums)

print(set_from_list)

nums_list = list(set_from_list)

print(nums_list)

# Como modificar conjuntos 


set_countries = {"COL","PER", "MX","BR"}

# Cantidad de elementos
size = len(set_countries)

#Saber si un elemento existe 

print("COL" in set_countries) # da una respuesta de True o false


#Adicionar elementos

set_countries.add("AR")

#Actualizar elementos 

set_countries.update({"UR", "ECU"})

# Remover elementos

set_countries.remove("COL")

set_countries.discard("boli") #Permite tratar de eliminar si no existe

# Elimina absoluatemnte todo 

set_countries.clear()

#Operaciones de conjuntos

set_countries = {"COL","PER", "MX","BR"}

set_countries_2 = {"PER", "AR", "UR"}

#Union 

set_c = set_countries.union(set_countries_2)

print(set_c)


#Interseccion

set_c = set_countries.intersection(set_countries_2)
print(set_c)

# diferencia

set_c = set_countries.difference(set_countries_2)
print(set_c)

#diferencia simetrica: Union sin los elemtos en comun

set_c = set_countries.symmetric_difference(set_countries_2)
print(set_c)



#------------------------------------------

#List comprehensión 

# Aprender a generar lista con un sintxys mas corta y facil de leer

my_list_2 = [element * 2 for element in range(1,11)] #Por cada elemento del iterable, vamos agregar un elemento a lalista 

print(my_list_2)

#Para mas detalles busca el archiv de lost_comprehension.py 



