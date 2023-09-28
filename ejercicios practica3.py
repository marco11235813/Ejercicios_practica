# Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso.

lista= list(range(1,6))
print(lista)
print(lista[::-1])


#-------------------------------------------------------------------------------------



# Escribir un programa que permita ingresar un número entero n. 
# Debe mostrar los primeros 10 múltiplos de n.
print('\n-------------------------------------------------------------\n')
import random
numero= input('Ingresa un numero: ')


print(f" TABLA DEL {numero}")
for x in range(1,11):
    print(f'{x} x {numero} = {x * int(numero)}')



#-------------------------------------------------------------------------------------


# Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176
print('\n-------------------------------------------------------------\n')
lista= []
for x in range(42,177):
    lista.append(x)
print(sum(lista))




#-------------------------------------------------------------------------------------



# Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:
# La suma de los numeros pares entre a y b.
# El producto de los numeros impares entre a y b.

print('\n-------------------------------------------------------------\n')
import numpy as np
a= int(input('Ingresa el primer numero: '))
b= int(input('Ingresa el segundo numero: '))

pares= []
impares= []
for x in range(a,(b+1)):
    if x == 0:
        continue
    else:
        if x%2 == 0:
            pares.append(x)
        elif x%2 == 1:
            impares.append(x)

print(sum(pares))
print(np.prod(impares))

# otra solucion, utilizando las variables y ciclos ya creados
producto= 0
for idx, x in enumerate(impares):
    if idx == 0:
        producto += x
    else:
        producto *= x
print(producto)

#-------------------------------------------------------------------------------------


# Escribir un programa que lea números enteros hasta que se ingrese un 0, 
# y muestre el máximo.


print('\n-------------------------------------------------------------\n')
import random
maximo= float('-inf')
minimo= float('inf')
numero= random.randint(-10,20)
while numero != 0:
    numero= random.randint(-10,20)
    print(numero)
    if numero > maximo:
        maximo= numero
    elif numero < minimo:
        minimo= numero
    else:
        continue

print(f'El numero maximo es: {maximo}')
print(f'El numero minimo es: {minimo}')




#-------------------------------------------------------------------------------------


# Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

try:
    numero= random.randint(0,20)
    lista= []
    while numero != 0:
        numero= random.randint(0,20)
        lista.append(numero)
    print(lista)
    promedio= sum(lista)/ len(lista)
    print(f'Promedio: {promedio}')
except ZeroDivisionError:
    print('Justo salio como primer numero 0 jajaja.... mala suerte ;)')



#-------------------------------------------------------------------------------------

# Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.


lista= []
while sum(lista) < 101:
    numero= random.randint(0,20)
    lista.append(numero)
    print(numero)
print(f'Cantidad de numeros ingresados para superar el valor 100: {len(lista)} numeros')



#-------------------------------------------------------------------------------------

# Escribir un programa que permita leer dos números 
# A y B (enteros positivos). Calcular el producto A * B por sumas 
# sucesivas e imprimir el resultado.


print('\n-------------------------------------------------------------\n')
a= abs(int(input('Primer numero: ')))
b= abs(int(input('Segundo numero: ')))

sucesivas= f' + {a}'*(b-1)
print(f'\n{a} x {b} = {a}{sucesivas} = {a*b}')





#-------------------------------------------------------------------------------------

# Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.

a= abs(int(input('Primer numero: ')))
b= abs(int(input('Segundo numero: ')))

sucesivas= f' * {a}'*(b-1)
print(f'\n{a} ** {b} = {a}{sucesivas} = {a**b}')


#-------------------------------------------------------------------------------------

# Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.


cant= int(input('Ingresa un numero: '))
contador= 0
lista= []
while contador <= cant:
    numero= random.randint(0,80)
    lista.append(numero)
    contador += 1
maximo= max(lista)
print(lista)
print(f'Valor maximo: {max(lista)}')
print(f'Posicion en la lista del valor maximo: {lista.index(maximo)}')
#-------------------------------------------------------------------------------------

# Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
# La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

nota = int(input("Nota: "))
nota_valida= list(range(1,11))

while nota not in nota_valida:
    print(nota)
    nota = int(input("Nota: "))



#-------------------------------------------------------------------------------------

# Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.



print("\nOperaciones:\n\n+ --> Suma\n- --> Resta\n* --> Multiplicación\n/ --> División\nF --> Exit\n")
opciones= ['+', '-', '*', '/', 'F']

while True:
    operacion= input('Ingresa la operacion que deseas realizar: ')

    if operacion == 'F' or operacion == 'f':
        break

    a= int(input('Ingresa el primer numero: '))
    b= int(input('Ingresa el segundo numero: '))

    if operacion not in opciones:
        print('operacion invalida')
    else:
        if operacion == '+':
            print(a+b)
            continue
        elif operacion == '-':
            print(a-b)
            continue
        elif operacion == '*':
            print(a*b)
            continue
        elif operacion == '/':
            if b == 0:
                print('no se puede diividir por 0')
                break
            else:
                print(a/b)
                continue
    
    
#-------------------------------------------------------------------------------------

# Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.

vocales= ['a','e','i','o','u']
while True:
    while True:
        letra= input('Ingresa una vocal: ')
        if letra not in vocales:
            print('Letra incorrecta')
            continue
        else:
            print('\nGanaste!')
            break
    opcion= input('Desea continuar? S/N?').lower()
    if opcion == 's':
        continue
    elif opcion == 'n':
        break
    else:
        print('opcion invalida')
        continue



#-------------------------------------------------------------------------------------

# Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
# La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
# Las notas 1 y 3 no usan nunca.
# La nota 0 se reserva para los ausentes.
# Las notas válidas pueden ser un 2 o un valor entre 4 y 10.


nota = int(input("Nota: "))
nota_valida= list(range(2,11))
nota_valida.pop(1)
while nota not in nota_valida:
    nota = int(input("Nota: "))



# otra solucion posible

nota = int(input("Nota: "))

#while nota not in (2,4,5,6,7,8,9,10):

nota_valida = tuple(range(4,11))
nota_valida += (2,)

while nota not in nota_valida:

    nota = int(input("Nota: "))


