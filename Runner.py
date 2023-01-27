if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    runner = arr[n-1]
    runner_up = 0
    for i in arr:
        if i < runner:
            runner_up = i
    print(runner_up)