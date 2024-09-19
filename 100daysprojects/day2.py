def init():
    print("Welcome to Tip Calculator :D")
    total_bill = int(input("What was the total bill ? \n$"))
    #print(total_bill) to see the result 
    total_tip = int(input("How much tip would you like to give ? $10, $12, $15\n$"))
    guest = int(input("How many people to split the bil? \n"))
    bill_splited = (total_bill + total_tip) / guest
    print(f"Each person should pay: ${bill_splited}")






if __name__ == '__main__':
    init()