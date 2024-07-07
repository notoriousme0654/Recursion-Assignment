def recursive_bubble_sort(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursive_bubble_sort(arr, n - 1)
array = [64, 34, 25, 12, 22, 11, 90]
print("Original Array:", array)
recursive_bubble_sort(array, len(array))
print("Sorted Array:", array)
