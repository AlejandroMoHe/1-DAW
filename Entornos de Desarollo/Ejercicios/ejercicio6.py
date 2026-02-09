class Notas:
    def __init__(self, alumno: str, nota: int):
        self.alumno = alumno
        self.nota = nota

    def __str__(self) -> str:
        return self.alumno

class B:
    def __init__(self, a1: str, a2: list):
        self.a1 = a1
        self.a2 = a2

    def m1(self) -> bool:
        for p in self.a2:
            if p[1] < 5:
                return False
        return True

    def m2(self) -> float:
        if len(self.a2) == 0:
            return 0
        s = 0
        for p in self.a2:
            s += p[1]
        return s / len(self.a2)

    def m3(self) -> list:
        r = []
        for p in self.a2:
            if p[1] < 5:
                r.append(p[0])
        return r

    def m4(self) -> int:
        c = 0
        for p in self.a2:
            if p[1] >= 5:
                c += p[0].a2
        return c

    def __str__(self) -> str:
        return self.a1
