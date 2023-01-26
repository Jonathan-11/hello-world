import math

def calculate_earth_speed_from_latitude_and_longitude():
    latitude = input('Latitud: ')
    radiant = float(latitude)
    cosine_of_latitude = math.radians(radiant)

    # Si el radio medio de la tierra es de 6371 km entonces se va a multiplicar con el coseno de la latitud
    # Ahora el resultado se multiplica por 2, ya que es parte de la ecuacion
    # Ahora vamos a multiplicar por π (3.14)
    # Ahora vamos a dividir el resultado entre 24, ya que son las horas de un dia entero

    calculation_result = 6371 * math.cos(cosine_of_latitude) * 2 * 3.14 / 24
    print('Por lo tanto los kilometros por hora que recorre la tierra son:', calculation_result)

def main():
    calculate_earth_speed_from_latitude_and_longitude()

main()
