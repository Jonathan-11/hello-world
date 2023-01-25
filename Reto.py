import math



mi_variable = input('Latitud: ')
digit_1 = float(mi_variable)
digit_2 = math.radians(digit_1)

# Si el radio medio de la tierra es de 6371 km entonces se va a multiplicar con el coseno de la latitud.
multiplication = 6371 * math.cos(digit_2)

# Ahora el resultado se multiplica por 2, ya que es parte de la ecuacion.
multiplication_2 = 2 * multiplication

# Ahora vamos a multiplicar por π (3.14).')
multiplication_3 = 3.14 * multiplication_2

# Ahora vamos a dividir el resultado entre 24, ya que son las horas de un dia entero.
division = multiplication_3 / 24

print('Por lo tanto los kilometros por hora que recorre la tierra son:', division)