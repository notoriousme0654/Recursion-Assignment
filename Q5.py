def decimal_to_binary(n):
    if n == 0:
        return '0'
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
decimal_number = 23
binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_representation}")
