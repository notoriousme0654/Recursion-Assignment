def print_numbers(n):
    if n == 1:
        print(1)
    else:
        print_numbers(n - 1)
        print(n)
N = 5
print(f"Printing numbers from 1 to {N}:")
print_numbers(N)
