# Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.


invitados= int(input('Cantidad de Invitados: '))
asientos= int(input('Asientos disponibles: '))


if asientos > invitados:
    print(f'La cantidad de asientos disponible es {asientos}, y los invitados son {invitados}, alcanza la cantidad de asientos y sobran {asientos - invitados}')
elif asientos < invitados:
    print(f'La cantidad de asientos disponible es {asientos}, y los invitados son {invitados}, no alcanzan los asientos para todos los invitados')
else:
    print('Hay la cantidad de asientos justa para todos los invitados')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.


while True:

    edad=int(input('\nIngresa tu edad: '))
    genero= input('Ingresa tu género: ').lower()
    nombre= input('Ingresa tu nombre: ').capitalize()

    opciones_fem= ['mujer', 'dama', 'princesa', 'reina', 'femina', 'femenina', 'femenino', 'niña', 'jovencita', 'vieja', 'anciana']
    opciones_masc= ['hombre', 'macho', 'principe', 'niño', 'joven', 'viejo', 'rey', 'masculino', 'anciana']

    if genero  in opciones_fem:
        genero= 'femenino'
    elif genero in opciones_masc:
        genero= 'masculino'
    else:
        print(f'\n{nombre}, el genero ingresado "{genero}" es invalido')
        continue

    if edad < 1 or edad > 120:
        print(f'\n{nombre}, la edad ingresada "{edad}" esta fuera del rango permitido')
        continue
    # elif genero != 'femenino' or genero != 'masculino':
    #     print(f'{nombre}, el genero ingresado "{genero}" es invalido')
    #     continue

    
    if (genero == 'femenino' and edad >= 60) or (genero == 'masculino' and edad >= 65):
        print(f'\n{nombre} ya esta en edad de jubilarse')
        break
    else:
        print(f'\n{nombre} no esta en edad de jubilarse todavia')
        break



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.


meses= ['enero', 'febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

resultados= []
for idx,mes in enumerate(meses, 1):
    resultados.append((idx,mes))

entrada= int(input('Ingresa un numero de mes: '))

if entrada < 1 or entrada > 12:
    print(f'el numero {entrada} no es valido como numero de mes')
else:
    print(f'el numero {entrada} corresponde a la posicion {entrada} en el calendario, que es el mes {meses[entrada-1]}')
    print(resultados[entrada - 1])


#otra manera utilizando las variables entrada y meses
if entrada not in range(1,13):
    print('Valor invalido')
else:
    print(meses[entrada-1])
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.
# Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
# Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
# Se debe recuperar cuando al menos una de las dos notas es menor a 4.


parcial1=int(input('Nota primer parcial: '))
parcial2=int(input('Nota segundo parcial: '))

if (parcial1 < 0 or parcial1 > 10) or (parcial2 < 0 or parcial2 > 10):
    print(f'una de las notas esta fuera del rango de calificaciones, las calificaciones deben estar entre 0 y 10')

if parcial1 >= 7 and parcial2 >= 7:
    print(f'El alumno/a promocionado la materia')
elif parcial1 >= 4 and parcial2 >= 4:
    print(f'El alumno a aprobado la materia')
else:
    if parcial1 < 4 or parcial2 < 4:
        print('El alumno a reprobado, debe recuperar la materia')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.
# (Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)

valores= []
valores.append(int(input('Ingresa el primer numero: ')))
valores.append(int(input('Ingresa el segundo numero: ')))

valores.sort(reverse= True)



if valores[0] % valores[1] == 0:
    print(f'{valores[0]} es divisible por {valores[1]}')
else:
    print(f'{valores[0]} no es divisible por {valores[1]}')



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------




# Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico del libro es de $1000, más $35,10 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación debe ser especial, lo que incrementa el costo en $1200. Además, si el número de páginas sobrepasa las 600 se hace necesario otro procedimiento de encuadernación que incrementa el costo en $880. Desarrollar un programa que calcule el costo de un libro dado el número de páginas.


COSTO_BASICO= 1000
COSTO_POR_PAGINA= 35.10
COSTO_ENC_RUSTICA= 1200
COSTO_ENC_ESPECIAL= 880

paginas= int(input('N° de paginas: '))

if paginas > 300 and paginas <= 600:
    costo= COSTO_BASICO + (paginas*COSTO_POR_PAGINA) + COSTO_ENC_RUSTICA
    print(f'el precio total del libro es {costo}')
elif paginas > 600:
    costo = COSTO_BASICO + (paginas*COSTO_POR_PAGINA) + COSTO_ENC_RUSTICA + COSTO_ENC_ESPECIAL
    print(f'el precio total del libro es {costo}')
else:
    costo= COSTO_BASICO + (paginas*COSTO_POR_PAGINA)
    print(f'el precio total del libro es {costo}')





#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
# Tiene la siguiente tarifa:

# Viaje mínimo $50
# Si recorre entre 0 y 10km: $20/km
# Si recorre 10km o más: $15/km
# Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.



TARIFA_MIN= 50
HASTA_10= 20
DE_15_O_MAS= 15
distancia= float(input('Que distancia desea recorrer? '))

if distancia <= 0:
    print('la distancia debe ser mayor a 0')
elif distancia > 0 and distancia < 10:
    tarifa= TARIFA_MIN + (distancia * HASTA_10)
    print(f'Total a pagar: ${tarifa}')
elif distancia >= 10:
    tarifa= TARIFA_MIN + (distancia * DE_15_O_MAS)
    print(f'Total a pagar: ${tarifa}')




#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------




# La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

# Menor de $5500.0 el descuento es del 4.5%
# Entre $5500.0 y $10000.0 el descuento es del 8%
# Más de $10000.0 el descuento es del 10.5%
# Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.

importe_recibido= float(input('Ingrese un importe: $'))

MENOR_5500= 0.045
ENTRE_5500_Y_10000= 0.08
MAS_DE_10000= 0.105

if importe_recibido < 5500:
    print(f'el importe recibido es {importe_recibido}, al ser menor a $5500 el descuento que se le aplica es del {MENOR_5500*100}%.\nEl importe total es {importe_recibido + (importe_recibido*MENOR_5500)}')
elif importe_recibido >= 5500 and importe_recibido < 10000:
    print(f'el importe recibido es {importe_recibido}, al estar entre $5500 y $9999 el descuento que se le aplica es del {ENTRE_5500_Y_10000*100}%.\nEl importe total es {importe_recibido + (importe_recibido*ENTRE_5500_Y_10000)}')
else:
    print(f'el importe recibido es {importe_recibido}, al ser $10000 o mayor, el descuento que se le aplica es del {MAS_DE_10000*100}%.\nEl importe total es {importe_recibido + (importe_recibido*MAS_DE_10000)}')




#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------




# Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:

# Jubilación: 11%
# Obra Social: 3%
# Sindicato: 3%

# Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
# Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

# Descuentos:

# Jubilación - 999,99
# Obra Social - 999,99
# Sindicato - 999,99
# Sueldo Neto 999,99


sueldo_basico= float(input('Ingresar Sueldo Basico: $'))
antiguedad= int(input('Ingresar Antiguedad (en años): '))
estado_civil= input('Ingresar Estado Civil: ').capitalize()

JUBILACION= 0.11
OBRA_SOCIAL= 0.03
SINDICATO= 0.03


if estado_civil == 'Soltero':
    temp_civ= sueldo_basico + (sueldo_basico*0.05)*antiguedad
elif estado_civil == 'Casado':
    temp_civ= sueldo_basico + (sueldo_basico*0.07)*antiguedad


jubilacion=  (temp_civ*JUBILACION)
obra_social= (temp_civ*OBRA_SOCIAL)
sindicato= (temp_civ*SINDICATO)

total= temp_civ - jubilacion - obra_social - sindicato

print(f'Estado Civil: {estado_civil} Sueldo básico: $ {sueldo_basico} Antigüedad: {antiguedad} años\n\nDescuentos:\n\nJubilación - {jubilacion}\nObra Social - {obra_social}\nSindicato - {sindicato}\n-----------------------\nSueldo Neto: {total}')




#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------





# Existen dos reglas que identifican dos conjuntos de valores:

# a) El número es de un solo dígito.
# b) El número es impar.
# A partir de estas reglas, escribir un programa que permita ingresar un número entero.

# Debe asignar el valor que corresponda a las variables booleanas:

# esDeUnSoloDigito
# esImpar
# estaEnAmbos
# noEstaEnNinguno
# el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.


numero= int(input('Ingresar numero: '))

esDeUnSoloDigito= len(str(numero)) == 1
esImpar= (numero % 2) != 0
estaEnAmbos= esDeUnSoloDigito and esImpar 
noEstaEnNinguno= not (esDeUnSoloDigito and esImpar)

def traductor(a):
   if a:
      a= 'Verdadero'
   else:
      a= 'Falso'

   return a

print(f'es de un solo digito: {traductor(esDeUnSoloDigito)}\nes impar: {traductor(esImpar)}\nesta en ambos: {traductor(estaEnAmbos)}\nno esta en ninguno: {traductor(noEstaEnNinguno)}\n')





#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------






# Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').


#funcion
def operacion(a,b,operacion):
  lista= ['suma', 'resta', 'multiplicacion', 'division']
  operacion= operacion.lower()
  
  if operacion not in lista:
    return 'la operacion ingresada es invalida'

  if operacion == 'suma':
    return a+b
  elif operacion == 'resta':
    return a-b
  elif operacion == 'multiplicacion':
    return a*b
  else:
    if b== 0:
        return 'ERROR'
    return a//b


operacion(2,2,'suma')

#clase
class calcular:
    def __init__(self):
        self.numeros= input('ingresa la operacion')
    def suma(self):
        for x,num in enumerate(self.numeros):
            if num == '+':
                suma= int(self.numeros[x-1]) + int(self.numeros[x+1])
        return suma
    def resta(self):
        for x,num in enumerate(self.numeros):
            if num == '-':
               resta= int(self.numeros[x-1]) - int(self.numeros[x+1])
        return resta
    def multiplicacion(self):
        for x,num in enumerate(self.numeros):
            if num == '*':
               multiplicacion= int(self.numeros[x-1]) * int(self.numeros[x+1])
        return multiplicacion
    def division(self):
        for x,num in enumerate(self.numeros):
            if num == '/':
               division= int(self.numeros[x-1]) / int(self.numeros[x+1])
               return division

#objeto
calculadora= calcular()
calculadora.division()









