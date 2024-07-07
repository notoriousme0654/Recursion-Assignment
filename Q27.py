def binary_search_recursive(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, end)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
