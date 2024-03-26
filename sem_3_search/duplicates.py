def del_dupl(s):
    q = s[0]
    for i in range(1, len(s)):
        if s[i] == q[-1]:
            q = q[:-1]
        else:
            q += s[i]
    return q
