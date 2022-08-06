
# Variables : Contenedor de objetos

num_1 = 3
num_2 = 4
nombre = "Facundo"

# Tipos de datos : Enteros, Flotantes, Strings y Booleanos
# Con estos tipos de datos podemos hacer operaciones.

#Cambiar de tipo de datos

num_1 = int(input("Escribe un numero :"))
nombre = str(num_1)
print(nombre)

# Operadores logicos

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

# Funciones : Definimos una funciones que se repite y luego la invocamos.


def imprimir_mensaje():
    print("Mensaje especial: ")
    print("Estoy aprendiendo a usar funciones !")

imprimir_mensaje()

# Estas pueden tener parametros
# La funcion se ejecuta teniendo en cuenta el parametro
# y el valor que le damos, asi como el impacto que tiene dentro de la funcion

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


# Si queremos aprovechar el resultado de ejecutar la función debemos utilizar 
# el objeto "return"

def suma(a, b):
    print("Se suman dos numeros")
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)

#Esto lo que hace es ejecutar la funcion con los parametros dados, guardar el valor 
#producto de la ejecucion de la funcion y guardarlo en otro objeto 


#Cadenas de caracteres

#Metodo: es una funcion especial, que existe para un tipo de dato en particular. 

#Por ejemplo, si queremos que el texto ingresado se transforme en mayúsculas.
#Se ejecuta el metodo sobre la variables

nombre.upper()  # Ejecutando el metodo que hace el texto en Mayus

nombre.capitalize()  # Ejecutando el metodo que hace el texto en Mayus

nombre.replace(" ", "")

#Se ejecuta el metodo sobre la variables


#INDICES

# Permite acceder a cierto caracter en una cadena dada
# Van desde 0 e escriben entre corchetes al lado de la variable 
# y son apuntadores numéricos a cada caracter.

nombre[1] # Apunta al caracter "O" de la variable

#SLICES

#Funcionan para hacer rebanadas de caracteres

nombre[1:4] # Te trae "omb" de la palabra nombre
nombre[:4] # Te trae "nomb" de la palabra nombre
nombre[2:] # Te trae "ombre" de la palabra nombre
nombre[:4:2] # Te trae "ob" de la palabra nombre por que va de 2 en 2
nombre[::-1] # Te trae "nombre" en reversa

# Bucles

#Nos permite repetir un bloque de codigo de manera costante bajo
#unos parametro

# >>>> While

# Ciclo que se ejecuta con una dos partes fundamentales
# Limite y una variable
# La pieza de codigo se ejecuta hasta que se llega al limite
