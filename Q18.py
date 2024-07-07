def GeekOnacci(args):
    A,B,C,N = list(map(int, args))
    N_th = A
    N_th2 = B
    N_th3 = C
    if N>3:
        for case in range(N-3):
            if case%3 == 0:
                N_th = N_th + N_th2 + N_th3
    
            elif case%3 == 1:
                N_th2 = N_th + N_th2 + N_th3
    
            else:
                N_th3 = N_th + N_th2 + N_th3
    if N%3 == 1:
        print(N_th)
    if N%3 == 2:
        print(N_th2)
    if N%3 == 0:
        print(N_th3)
n = int(stdin.readline())
for test_case in range(n):
    GeekOnacci(stdin.readline().strip().split(' '))
