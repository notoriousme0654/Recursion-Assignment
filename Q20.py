def count_zeros(n):    
    if n == 0:
        return 0
    else:
        last_digit = n % 10
        if last_digit == 0:
            return 1 + count_zeros(n // 10)
        else:
            return count_zeros(n // 10)
number = 1020304050
print(f"Number of zeros in {number} is {count_zeros(number)}")
