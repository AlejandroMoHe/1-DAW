class Coche:

    def __init__(self, marca: str, modelo: str, año_fabricacion: int, peso: int, tipo_motor: str, potencia: int, automatico: bool, num_puertas: int, num_asientos: int, consumo: float, deposito: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.peso = peso
        self.tipo_motor = tipo_motor
        self.potencia = potencia
        self.automatico = automatico
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.consumo = consumo
        self.deposito = deposito

    def __str__(self) -> str:
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Año de Fabricación: {self.año_fabricacion}\n"
            f"Peso: {self.peso}\n"
            f"Tipo de Motor: {self.tipo_motor}\n"
            f"Potencia: {self.potencia}\n"
            f"Automático: {self.automatico}\n"
            f"Número de puertas: {self.num_puertas}\n"
            f"Número de asientos: {self.num_asientos}\n"
            f"Consumo: {self.consumo}\n"
            f"Depósito: {self.deposito}\n"
        )

    def autonomia(self) -> float:
        return self.deposito / self.consumo * 100