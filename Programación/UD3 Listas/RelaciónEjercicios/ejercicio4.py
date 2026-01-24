def dimension(m: list[list[int]]) -> list[int]:
    if len(m) == 0:
        return [0, 0]
    else:
        return [len(m), len(m[0])]

