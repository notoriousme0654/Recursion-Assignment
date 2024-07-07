def sum_of_first_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_first_n(n - 1)
N = 5
print(f"The sum of the first {N} natural numbers is {sum_of_first_n(N)}")
