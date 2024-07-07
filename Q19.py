def fibonacci(a, b, n):
    if(n == 0):
        return(a)
    elif(n == 1):
        return(b)
    elif(n == 2):
        return(a ^ b)
    return(fibonacci(a, b, n % 3))

T = int(input())
for i in range(T):
    a, b, n = [int(x) for x in input().split()]
    print(fibonacci(a, b, n))
