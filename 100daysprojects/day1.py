# DAY 1

def init():
    print("Binvenido a este programa sencillo de generador de nombre de bandas \nPodrás generar tu banda respobdiendo la siguiente pregunta")
    name = input("¿Cual es tu ciudad de nacimiento?\n")
    pet = input("¿Cual es tu animal favorito?\n")
    print("Tu banda se llamará " + pet + " " +  name)


if __name__ == '__main__':
    init()