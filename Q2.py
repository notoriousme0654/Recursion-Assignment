def product_of_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) * product_of_digits(n // 10)
number = 12345
print(f"Product of digits of {number} is {product_of_digits(number)}")
