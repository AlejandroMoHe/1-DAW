from datetime import datetime

def tiempo_pasado(nacimiento: datetime) -> int:
   hoy = datetime.now()
   # Calcular la diferencia de años teniendo en cuenta si ya pasó el cumpleaños este año
   edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
   return edad