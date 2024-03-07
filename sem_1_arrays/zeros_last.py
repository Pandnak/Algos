def zeros_to_end(arr):
    i = 0
    j = len(arr) - 1
    while (i < j):
        if (arr[i] == 0 and arr[j] != 0):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif (arr[i] == 0):
            j -= 1
        else:
            i += 1
    return arr
