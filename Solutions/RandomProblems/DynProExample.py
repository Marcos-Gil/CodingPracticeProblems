from timeit import default_timer as timer

def fib(num):
    if num == 1 or num == 2:
        result = 1
    else:
        result = fib(num - 1) + fib(num - 2)
    return result

def fibDP(num, memo):
    if memo[num] != None:
        return memo[num]
    if num == 1 or num == 2:
        result = 1
    else:
        result = fibDP(num - 1, memo) + fibDP(num - 2, memo)
    memo[num] = result

    return result

def fib_bottom_up(num):
    if num == 1 or num == 2:
        return 1

    bottomUp = [None] * (num + 1)
    bottomUp[1] = 1
    bottomUp[2] = 1

    for i in range(3, num + 1):
        bottomUp[i] = bottomUp[i-1] + bottomUp[i-2]

    return bottomUp[num]

def main():
    memo = [None] * 41
    start = timer()
    resultOne = fib(40)
    end = timer()
    print(end-start,"time")
    start = timer()
    resultTwo = fibDP(40,memo)
    end = timer()
    print(end-start,"time")
    start = timer()
    resultThree = fib_bottom_up(40)
    end = timer()
    print(end-start,"time")
    print(resultOne)
    print(resultTwo)
    print(resultThree)

main()
