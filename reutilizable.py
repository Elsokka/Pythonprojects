#Dictionarios

mi_diccionario = {
    "Brasil" : 108_989_873,
    "Colombia" : 1_000_000,
    "Argentina" : 123_827_232,
}
print(mi_diccionario["Colombia"])

#Prueba de como ZIP

text = "Hola, soy Felipe"

unique = {c: c.upper() for c in text if c in "aeiou"}

print(unique)