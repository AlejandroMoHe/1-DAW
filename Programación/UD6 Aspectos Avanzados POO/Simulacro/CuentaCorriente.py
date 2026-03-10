from Cuenta import Cuenta


class CuentaCorriente(Cuenta):
    def __init__(self, titular: str, numero_cuenta: str, saldo: float, limite_descubierto: float) -> None:
        super().__init__(titular, numero_cuenta, saldo)
        self.limite_descubierto = limite_descubierto

    
    def puede_retirar(self, cantidad: float) -> bool:
        return cantidad < self.limite_descubierto
    
    def retirar(self, cantidad: float) -> None:
        descubierto = self.limite_descubierto * -1

        if self.saldo <= cantidad and cantidad < descubierto:
            self.saldo - cantidad

    def __str__(self):
        return f"Cuenta Corriente | Titular: {self.titular} | Nº: {self.numero_cuenta} | Saldo: {self.saldo}€ | Descubierto: {self.limite_descubierto}€"