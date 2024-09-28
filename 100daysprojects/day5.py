import random
def init():
    
    #Clase de loops

    #Practica 1 
    '''
    fruits = ["Apple","Peach","Pear"]
    for fruit in fruits:
        print(fruit)
    '''


    #practica2
    '''
    code_list = [2122721478,2122721476,2122721484,2122721483,2122721480,2122721481,2122721482]

    code_max = 0
    for code in code_list:
        if code >= code_max:
            code_max = code
        else:
            continue
    print(code_max)
    '''


    #Practica 3
    '''
    sum_score = 0

    for n in range(1,101):
        sum_score += n

    print(sum_score)
    '''

    #practica 4

    '''
    for n in range(1,101):
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
    '''

    #proyect day 5 

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    final_pasword = []

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Creo una lista con las letras

    for l in range(1,nr_letters + 1):

        if nr_letters != 0:

            final_pasword.append(random.choice(letters))
            nr_letters -= 1

    # agrego a la lista symbols 
    for s in range(1,nr_symbols + 1):

        if nr_symbols != 0:

            final_pasword.append(random.choice(symbols))
            nr_symbols -= 1


    #Agrego numeros a la lista 

    for n in range(1,nr_numbers + 1):

        if nr_numbers != 0:

            final_pasword.append(random.choice(numbers))
            nr_numbers -= 1

    #print(final_pasword)
    #Tengo una lista con todos los caracteres que necesito, los randonizo
    random.shuffle(final_pasword)
    #print(final_pasword)
    #Creo una nueva variable con los caracteres randonizados yvuelvo una lista a string 
    my_password = "".join(final_pasword)
    print(f"Your final password is: {my_password}")

        

if __name__ == '__main__':
    init()