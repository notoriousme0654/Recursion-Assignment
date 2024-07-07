def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_max = find_max(arr[:mid])
        right_max = find_max(arr[mid:])
        return max(left_max, right_max)

def find_min(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_min = find_min(arr[:mid]) 
        right_min = find_min(arr[mid:]) 
        return min(left_min, right_min)  

array = [3, 7, 2, 8, 1, 9, 4, 5, 6]
print(f"Array: {array}")
print(f"Maximum element: {find_max(array)}")
print(f"Minimum element: {find_min(array)}")
