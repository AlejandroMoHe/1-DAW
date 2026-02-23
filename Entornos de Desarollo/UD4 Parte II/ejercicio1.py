def contiene(lista: list, num: int) -> bool:
    for n in lista:
        if n == num:
            return True
    return False