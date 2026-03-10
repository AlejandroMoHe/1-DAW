from Cuenta import Cuenta


class CuentaAhorro(Cuenta):
    def __init__(self, titular: str, numero_cuenta: str, saldo: float, interes_anual: float):
        super().__init__(titular, numero_cuenta, saldo)
        self.interes_anual = interes_anual
    

    def aplicar_intereses(self):
        self.saldo += (self.saldo*(self.interes_anual / 100))
    
    
    def __str__(self):
        return f"Cuenta Ahorro | Titular: {self.titular} | Nº: {self.numero_cuenta} | Saldo: {self.saldo}€ | Interés: {self.interes_anual}%"