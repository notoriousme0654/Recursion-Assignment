def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
a = 2
b = 5
print(f"{a} raised to the power {b} is {power(a, b)}")
