def reverse_number(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        reversed_remaining = reverse_number(remaining_digits)
        return int(str(last_digit) + str(reversed_remaining))
number = 12345
print(f"The reverse of {number} is {reverse_number(number)}")
