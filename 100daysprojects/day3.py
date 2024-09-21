def init():
    
    """
    #Ejercicio de practica de If/Else 1
    number = int(input("Give me your number:\n"))
    
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odds Number")
    
    """
    print("Welcome to Python Pizza Delivery.")
    size = input("What size Pizza do you want? S for Small, M for Medium, L for Large:\n")
    pepperoni = input("Do you want Pepperoni on your Pizza? Y to Yes, N to No:\n")
    extra_chesee = input("Do you want extra Chesee on your Pizza? Y to Yes, N to No:\n")
    pizza_bill = 0

    if size == "S":
        pizza_bill = 15
        if pepperoni == "Y":
            pizza_bill += 2

    elif size == "M":
        pizza_bill = 20
        if pepperoni == "Y":
            pizza_bill += 3
    else:
        pizza_bill = 25
        if pepperoni == "Y":
            pizza_bill += 2
    
    if extra_chesee == "Y":
        pizza_bill += 1
    
    print(f"Your total Pizza bill is ${pizza_bill}")

   
   
   # print("Welcome to Treasure Island \nYour mission is to find the treasure.")


if __name__ == '__main__':
    init()