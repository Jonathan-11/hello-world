# Este es el repo del reto

import math

miVariable = input('Latitud: ')
print('El coseno es:', miVariable)

digito1 = float(miVariable)
digito2 = math.radians(digito1)

print('Por lo tanto el coseno de la latitud es:', math.cos(digito2))

print('Si el radio medio de la tierra es de 6371 km entonces:')

n1 = float(input('Ingresa el radio medio de la tierra: '))
n2 = float(input('Ingresa el coseno de la latitud, solo tres decimales: '))

mult = n1 * n2
print('El resultado es:', mult)

print('Multiplica el resultado por 2, ya que es parte de la ecuacion')

n3 = float(input('Escribe el resultado de la operación: '))
n4 = float(input('Escribe 2: '))

mult2 = n3 * n4
print('El resultado es:', mult2)

print('Ahora vamos a multiplicar por π')

n5 = float(input('Escribe el resultado de la multiplicación: '))
n6 = float(input('Escribe el valor de π (3.14): '))

mult3 = n5 * n6
print('El resultado es:', mult3)

print('Ahora vamos a dividir el resultado entre 24, ya que son las horas de un dia entero')

n7 = float(input('Escribe el resultado de la multiplicacion: '))
n8 = float(input('Escribe las horas de un dia entero: '))

div = n7 / n8
print('El resultado final es:', div)

print('Por lo tanto los kilometros por hora que recorre la tierra son:', div)