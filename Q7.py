def print_numbers_reverse(n):
    if n == 1:
        print(1)
    else:
        print(n)
        print_numbers_reverse(n - 1)
N = 5
print(f"Printing numbers from {N} to 1:")
print_numbers_reverse(N)
