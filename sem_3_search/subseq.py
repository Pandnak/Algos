def is_IN(A, B):
    a, b = 0, 0
    while (b != len(B)):
        if (B[b] == A[a]):
            a += 1
            if (a == len(A)):
                return True
        else:
            if (a != 0):
                b -= 1
            a = 0
        b += 1
    return False

# Алгорим с лекции
def isSubsequence(a, b):
    q = []
    for el in a:
        q.append(el)

    for el in b:
        if q[0] == el:
            q = q[1:]

    return len(q) == 0

# Алгорим с лекции модифицированный
def isSubsequenceMod(a, b):
    q = []
    for el in a:
        q.append(el)
    copy = q
    for el in b:
        if q[0] == el:
            q = q[1:]
        elif len(q) != len(copy):
            q = copy

    return len(q) == 0
