def runner():

    n = int(input())
    arr = map(int, input().split()) #runner-up score : El segundo mas rapido 
    runner_up = arr[2]
    print(runner_up)

if __name__ == "__main__":
    runner()