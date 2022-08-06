# >>>>>>   Variables : Contenedor de objetos


num_1 = 3
num_2 = 4
nombre = "Facundo"

# Tipos de datos : Enteros, Flotantes, Strings y Booleanos con estos tipos de datos podemos hacer operaciones.

# >>>>>> Convertir los tipos de datos


num_1 = int(input("Escribe un numero :"))
nombre = str(num_1)
print(nombre)

# >>>>>>> Operadores logicos


# %   : El restante de la operacion
# and : para comparar si dos valores son verdaderos.
# or  : para comparar si dos valores son falsos.
# not : para invertir el valor booleano.
# ==  : Compara dos valores y te dice si son iguales o no.
# !=  : Compara dos valores y te dice sin son diferentes o no.
# >   : Compara si es mayor que otro valor.
# >   : Compara si es menor que otro valor.
# >=  : igual o mayor que el valor a comparar.
# <=  : igual o menor que el valor a comparar.
#pass : Sirve para saltar esa linea de codigo
#Triples comillas:  deja escribir una cada mas larga de caractares

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

opcion = int(input("Elige una opcion (1, 2, 3 ): "))

if opcion == 1:
    conversacion("Elegiste opcion 1")
elif opcion == 2:
    conversacion("Elegiste opcion 2")
elif opcion== 3:
    conversacion("Elegiste opcion 2")
else:
    print("El valor ingresado no corresponde a un numero valido")


# Si queremos aprovechar el resultado de ejecutar la funcion debemos utilizar el objeto "return"

def suma(a, b):
    print("Se suman dos numeros")
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)

#Esto lo que hace es ejecutar la funcion con los parametros dados, guardar el valor producto de la ejecucion de la funcion y guardarlo en otro objeto 


# >>>>>> Cadenas de caracteres


#Metodo: es una funcion especial, que existe para un tipo de dato en particular. 
#Por ejemplo, si queremos que el texto ingresado se transforme en mayusculas.
#Se ejecuta el metodo sobre la variables

nombre.upper()  # Ejecutando el metodo que hace el texto en Mayus

nombre.capitalize()  # Ejecutando el metodo que hace el texto en Mayus

nombre.replace(" ", "")

#Se ejecuta el metodo sobre la variables


#>>>>>>>> INDICES

# Permite acceder a cierto caracter en una cadena dada
# Van desde 0 e escriben entre corchetes al lado de la variable 
# y son apuntadores numericos a cada caracter.

nombre[1] # Apunta al caracter "O" de la variable

# >>>>>>>> SLICES

#Funcionan para hacer rebanadas de caracteres

nombre[1:4] # Te trae "omb" de la palabra nombre
nombre[:4] # Te trae "nomb" de la palabra nombre
nombre[2:] # Te trae "ombre" de la palabra nombre
nombre[:4:2] # Te trae "ob" de la palabra nombre por que va de 2 en 2
nombre[::-1] # Te trae "nombre" en reversa

# >>>>>>> BUCLES

#Nos permite repetir un bloque de codigo de manera costante bajo unos parametro

# >>>> While

# Ciclo que se ejecuta con una dos partes fundamentales
# Limite y una variable
# La pieza de codigo se ejecuta hasta que se llega al limite

def init():
    LIMIT = 100
    contador = 0
    potencia_2 = 2**contador
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

# >>>>> Almacenar varios valores en una variable

nums =[1,3,4,5,6,56,89]

# Para acceder a un objeto de mi lista debo seleccionarlo

objeto = nums[2]

#Puedo agregar y eliminar objetos

nums.append(3) # agrega el objeto a lista
nums.pop(4) # Elimina el objeto que esta en el indice 4

for elemento in nums: # Para recorrer la lista
    print(elemento)


# Podemos de igual forma operar con listas

nums_2 = [4,3,6,2,4]

lista_final = nums + nums_2

lista_finalpor5 = nums * 5

#Puedo usar los slices en las listas


nums[1:4] # Trae solo los elementos en ese rango de la lista

# Para covertir una lista en un string


# password = "".join(password)



# >>>> Tuplas 
# Objetos estaticos

mi_tupla = (2,3,21,43,53)


# >>>>>> Diccionarios : Una estructura de llaves y valores
#Accedemos a los elementos del diccionario a traves de la llave

mi_diccionario = {
    "Brasil" : 108_989_873,
    "Colombia" : 1_000_000,
    "Argentina" : 123_827_232,
}
print(mi_diccionario["llave 1"]) # Nos permite ir a mi diccionario, y abrr lo que esta en la llave 1

#Tambien puedo recorrer datos con for en los diccionario

for pais in mi_diccionario.keys():
    print(pais) #Imrime la llaves del dic


for pais in mi_diccionario.values():
    print(pais) #Imrime los valoeres de la llaves del dic


for pais, poblacion in mi_diccionario.items():
    print(f"{pais} tiene la poblacion de {poblacion}") #Imprime los valores de la llaves del dic y las llaves


#  .keys()  > Retorna la clave de nuestro elemento

#  .values() > Retorna una lista de elementos (valores del diccionario)

#  .items()  > Devuelve lista de tuplas (primero la clave y luego el valor)

#  .clear()  > Elimina todos los items del diccionario

#  .pop(“n”) > Elimina el elemento ingresado