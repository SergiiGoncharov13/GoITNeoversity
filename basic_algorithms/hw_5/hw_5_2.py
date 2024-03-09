def binary_search(sorted_array, target):
    low, high = 0, len(sorted_array) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_array[mid]
        iterations += 1

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            return iterations, mid_value

    if low < len(sorted_array):
        upper_bound = sorted_array[low]
    else:
        upper_bound = None

    return iterations, upper_bound



if __name__ == '__main__':
    # Тестування функції
    arr = [1.1, 1.3, 2.5, 3.8, 4.6]
    print(binary_search(arr, 3.5))
    print(binary_search(arr, 4))
    print(binary_search(arr, 6.0))
    print(binary_search(arr, 2.5))
    print(binary_search(arr, 0)) 