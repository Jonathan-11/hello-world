# Este es el repo del reto

import math

miVariable = input('Latitud: ')

digito1 = float(miVariable)
digito2 = math.radians(digito1)

print('Por lo tanto el coseno de la latitud es:', math.cos(digito2))

print('Si el radio medio de la tierra es de 6371 km entonces se va a multiplicar con el coseno de la latitud.')

cosenoLatitud = math.cos(digito2)
radioMedio = 6371

mult = radioMedio * math.cos(digito2)
print('El resultado es:', mult)

print('Ahora el resultado se multiplica por 2, ya que es parte de la ecuacion.')

n3 = 2

mult2 = n3 * mult
print('Y el resultado es:', mult2)

print('Ahora vamos a multiplicar por π (3.14).')

n4 = 3.14

mult3 = n4 * mult2
print('El resultado es:', mult3)

print('Ahora vamos a dividir el resultado entre 24, ya que son las horas de un dia entero.')

n5 = 24

div = mult3 / n5
print('El resultado final es:', div)

print('Por lo tanto los kilometros por hora que recorre la tierra son:', div)