import random
import supportday4

def init():

    '''
    #Mini exercise
    friends_list = ["Felipe","Farid","Elias","Henry"]
    selected_friend = random.randint(0,3)
    print(friends_list[selected_friend])
    '''
    print("Welcome to Rock, Paper and Scissors")

    player_choise = int(input("Whay do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

    machine_choise = random.randint(0,3)
    print("You select:\n")
    if player_choise == 0:

        print(supportday4.rock)
        
    elif player_choise == 1:

        print(supportday4.paper)
    elif player_choise == 2:

        print(supportday4.scissors)
    
    else:
        print("That is not a valid choise")
     

    print("Machine select:\n")

    if machine_choise == 0:

        print(supportday4.rock)
        
    elif machine_choise == 1:

        print(supportday4.paper)
    else:

        print(supportday4.scissors)
    
    #Logica de juego 

    #Escoge Rock
    if player_choise == 0:

        if machine_choise == 2:
            print("You Win")
        if machine_choise == 1:
            print("You Lose")
        if machine_choise == 0:
            print("Play again!")
    
    #Escoge Paper
    if player_choise == 1:

        if machine_choise == 0:
            print("You Win")
        if machine_choise == 1:
            print("Play again!")
        if machine_choise == 2:
            print("You Lose")

    #Escoge Scissors
    if player_choise == 2:

        if machine_choise == 0:
            print("You Lose")
        if machine_choise == 1:
            print("You Win")
        if machine_choise == 2:
            print("Play again!")

if __name__ == '__main__':
    init()