class CuentaBancaria:

    INTERES = 0.10

    def __init__(self, titular: str, iban: str, saldo: float) -> float:
        self.titular = titular
        self.iban = iban
        self.saldo = saldo

    def añadir_interes(self):
        return self.saldo * (1 + CuentaBancaria.INTERES)
    
if __name__ == "__main__":

    cuenta1 = CuentaBancaria("Juan", "ES18918989218968", 60.22)
    cuenta2 = CuentaBancaria("Maria", "ES17498951789463", 30)

    print("==== SIN MODIFICAR ====")
    print(cuenta1.añadir_interes())
    print(cuenta2.añadir_interes())
    print()
    
    CuentaBancaria.INTERES = 0.50

    print("==== MODIFICADOS ====")
    print(cuenta1.añadir_interes())
    print(cuenta2.añadir_interes())

