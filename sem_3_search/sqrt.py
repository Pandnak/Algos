def find_sqrt(num):
    l = 0
    r = num
    while l <= r:
        m = (l + r) // 2
        if (m**2 > num):
            r = m - 1
        elif (m**2 < num):
            l = m + 1
        else:
            return m
    return r
