def mean_array(arr):
    if not arr:
        return None  # Alternatively, raise an exception for an empty array case
    else:
        total_sum = sum_array(arr)  # Use the sum_array function from the previous explanation
        return total_sum / len(arr)
def sum_array(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])
array = [1, 2, 3, 4, 5]
print(f"The mean of the array {array} is {mean_array(array)}")
