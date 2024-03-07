def evenFirst(arr):
    n = len(arr) - 1
    i = j = 0
    while (i <= n):
        if (arr[i] % 2 == 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
