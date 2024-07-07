def product(x, y):
    if y == 0:
        return 0
    else:
        return x + product(x, y - 1)
x = 5
y = 4
print(f"The product of {x} and {y} is {product(x, y)}")
