#Clase de como funciona continue and break

def run():

    for contador in range(1000): #Ejemplo 1
        if contador % 2 != 0:
            continue 
        print(contador)


    for i in range(10000):   #Ejemplo 2
        print(i)
        if i == 5778:
            break
    
    texto =input("Escribe un texto: ")  #Ejmplo 3
    for i in texto:
        if i == "o":
            break
        print(i)


if __name__ == "__main__":
    run()
