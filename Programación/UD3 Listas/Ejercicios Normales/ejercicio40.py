import statistics

def convertir_lista_str2int(l: list[str]) -> list[int]:
    l2 = []
    for e in l:
        l2.append(int(e))
    return l2


num = input("Inserta numeros separados por ; --> ")

numeros = convertir_lista_str2int(num.split(";"))

print(f"El número menor es: {min(numeros)}")
print(f"El número mayor es: {max(numeros)}")
print(f"La suma es: {sum(numeros)}")
print(f"La media es: {statistics.mean(numeros)}")

