def reverseArray(arr, left, right):
    while(left < right):
        arr[right], arr[left] = arr[left], arr[right]
        left += 1
        right -= 1

def sol(arr, k):
    n = len(arr)

    reverseArray(arr, 0, n - 1)
    reverseArray(arr, 0, n - k - 1)
    reverseArray(arr, n - k, n - 1)
