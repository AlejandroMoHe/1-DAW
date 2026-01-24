def sin_repetidos(l: list[int])-> list[int]:
    l2 = []

    for e in l:
        if l2.count(e) == 0:
            l2.append(e)
    return l2

l = (4,5,8,8,6,6)

print(sin_repetidos(l))
