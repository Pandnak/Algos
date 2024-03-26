def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while (left < right):
        if (s[left] != s[right]):
            return False
        left += 1
        right -= 1

    return True

def is_palindrome_with_stack(s) :
    stack = []
    for char in s :
        stack.append(char)
    for char in s:
        if char != stack[-1] :
            return False
        stack = stack[:-1]

    return True
