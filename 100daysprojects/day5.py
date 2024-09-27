def init():
    
    #Clase de loops

    '''
    fruits = ["Apple","Peach","Pear"]
    for fruit in fruits:
        print(fruit)
    '''
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
    sum_score = 0

    for n in range(1,101):
        sum_score += n

    print(sum_score)

    #print("Welcome to the PyPassword Generator!\n")
    



if __name__ == '__main__':
    init()