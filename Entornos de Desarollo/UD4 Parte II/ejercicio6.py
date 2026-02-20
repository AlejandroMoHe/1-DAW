def alumnos_comunes(a, b):
    res = []
    for x in a:
        if x in b and x not in res:
            res.append(x)
    return res