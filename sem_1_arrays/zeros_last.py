def zeros_to_end(arr):
    i = 0
    j = len(arr) - 1
    while (i <= j):
        if (arr[i] == 0):
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        i += 1
