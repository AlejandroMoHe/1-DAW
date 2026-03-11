class Cuenta:
    
    MANTENIMIENTO = 5

    def __init__(self, titular: str, numero_cuenta: str, saldo: float):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    

    def __eq__(self, other):
        if isinstance(other, Cuenta):
            return self.numero_cuenta == other.numero_cuenta
        return False
    

    def __hash__(self):
        return hash(self.numero_cuenta)


    def ingresar(self, cantidad: float):
        self.saldo += cantidad


    def retirar(self, cantidad: float) -> bool:
        if self.saldo <= cantidad:
            self.saldo - cantidad
            return True
        else:
            return False


    def cobrar_comision(self):
        self.saldo -= Cuenta.MANTENIMIENTO


    def __str__(self):
        return f"Cuenta | Titular: {self.titular} | Nº: {self.numero_cuenta} | Saldo: {self.saldo}€"