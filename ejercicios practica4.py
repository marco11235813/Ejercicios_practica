import random 


# Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
# La computadora debe mostrar el número máximo y el número mínimo.


maximo= float('-inf')
minimo= float('inf')
respaldo= []


a= random.randint(0,40)
respaldo.append(a)
while a != 0:
    a= random.randint(0,40)
    respaldo.append(a)
    if a > maximo:
        maximo= a
    if a == 0:
        break
    elif a < minimo:
        minimo= a
    
print(f'Numero máximo: {maximo}')
print(f'Numero minimo: {minimo}')
# print(respaldo)


print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) de cada jugador de un equipo de básquet La carga finalizará al ingresar cero. Calcular y mostrar la estatura promedio del equipo.


jugadores= []
contador= 0

while True:
    estatura= random.uniform(0.0, 3.0)
    contador += 1
    if contador == 12 or estatura == 0.0:
        break
    elif estatura < 1.60:
        contador -= 1
        continue
    else:
        jugadores.append(estatura)
print(f'Estatura promedio del equipo: {round((sum(jugadores)/len(jugadores)),2)}mts.')

#otra manera
'''
contador= 0
equipo= []

while True:
    estatura= float(input('Ingrese la estatura en mts.: '))

    if estatura == 0 or contador == 12:
        break
    else:
        equipo.append(estatura)
        contador += 1 
'''




print("-"*80)
#----------------------------------------------------------------------------------------------------------


# Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.


contador= 0
equipo_nombre= []
equipo_edad= []
mas_joven= float('inf')
while True:
    nombre= input('ingrese el nombre: ')
    if '*' in nombre or contador == 12:
        for x,y in zip(equipo_nombre, equipo_edad):
            if y == mas_joven:
                print(f'Jugador: {x}\nEdad: {y}')
        break
    else:
        edad= int(input('Ingrese la edad: '))
        if edad < mas_joven:
            mas_joven= edad

        equipo_nombre.append(nombre)
        equipo_edad.append(edad)
        contador += 1


print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"


USUARIO= ('admin')
PASSWORD= ('123456')
intentos= 0

while True:
    user= input('Ingrese su usuario: ')
    password= input('ingrese contraseña: ')

    if user != USUARIO or password != PASSWORD:
        intentos += 1
        if intentos == 3:
            print('Te quedaste sin intentos, vuelve a intentarlo mas tarde')
            break
        print('Usuario o contraseña incorrecta vuelva a intentarlo')
        continue
    else:
        break

print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa que permita para cada cliente que va al banco "Express".
# Cada cliente indica su número de documento y aguarda a ser atendido, cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.

dicc= {}
turnos= 0
llaves= []
valores= []
while True:
    turnos +=1
    if turnos > 3:
        break
    try: 
        dni= int(input('Ingrese su N° de documento sin puntos: '))
    except ValueError:
        print('Valor invalido')
        continue
    if dni == -1:
        break

    else:
        nombre= input('Ingrese su nombre: ')
        llaves.append(dni)
        valores.append(nombre)

        for idx in range(0, len(llaves)):
            dicc.update({llaves[idx]:valores[idx]})


print(llaves[0],',',dicc[llaves[0]])
print(llaves[-1],',',dicc[llaves[-1]])

print("-"*80)
#----------------------------------------------------------------------------------------------------------


# Escribir un programa que permita Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100)

menor_18= []
mayor_18= []



while True:
    edades= random.randint(1,1000)

    if edades == 999:
        break
    elif edades < 18:
        menor_18.append(edades)
    elif edades >= 18 and edades <= 100:
        mayor_18.append(edades)
    else:
        continue

promedio_menor_18= sum(menor_18) / len(menor_18)
promedio_mayor_18= sum(mayor_18) / len (mayor_18)
promedio_edades= (sum(mayor_18) + sum(menor_18)) / (len(mayor_18) + len (menor_18))

print(f'Edades menores a 18: {menor_18}')
print(f'Edades mayores a 18: {mayor_18}')
print(f'Promedio de edad de los menores: {promedio_menor_18}')
print(f'Promedio de edad de los adultos: {promedio_mayor_18}')
print(f'promedio de edad de la muestra: {promedio_edades}')

    


print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo
# Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
# Cantidad de alumnos que aprobaron (nota >= 4). Cantidad de alumnos que desaprobaron el examen (nota < 4). Porcentaje de alumnos que están aplazados (nota == 1)


dicc= {}
alumnos= []
calificaciones= []

for legajo in range(1000,1031):
    notas = []
    
    while len(notas) < 3:
        nota= random.randint(1,10)
        notas.append(nota)
        if len(notas) == 3:
            break
    alumnos.append(legajo)
    calificaciones.append(notas)
    for idx in range(0, len(alumnos)):
        dicc.update({alumnos[idx]:calificaciones[idx]})

for alumno, nota in zip(alumnos,calificaciones):
    if nota[-1] >=4:
        print(f'Alumno {alumno}: {nota[-1]}----> APROBADO')
        print(f'Promedio Final: {round(sum(nota)/len(nota),2)}\n')
    elif nota[-1] < 4:
        if nota[-1] != 1:
            print(f'Alumno {alumno}: {nota[-1]}----> DESAPROBADO')
            print(f'Promedio Final: {round(sum(nota)/len(nota),2)}\n')
        else:
            print(f'Alumno {alumno}: {nota[-1]}----> APLAZADO\n')

print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
# Aplica el precio base a la primera docena de unidades.
# Aplica un 10% de descuento a todas las unidades entre 13 y 100.
# Aplica un 25% de descuento a todas las unidades por encima de las 100.
# Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:
# 100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
# Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad.
# El fin de carga se determina ingresando -1 como cantidad solicitada.
# Al finalizar informar:
# a- Cantidad de ventas realizadas total.
# b- Cantidad de ventas que se aplicaron un 10% de descuento.
# c- Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos




# PRECIO_BASE= float(input('Ingrese el precio base: $'))
PRECIO_BASE= 100
descuento_10= (PRECIO_BASE/100)*10
descuento_25= (PRECIO_BASE/100)*25


total= 0
total_desc_10= 0
total_BASE= 0
contador= 0
while True:
    pedido= int(input('Ingrese la cantidad que requiera: '))
    if pedido == -1:
        break

    contador += 1


    if pedido <= 12:
        sin_descuento= PRECIO_BASE * pedido
        primer_desc= 0
        segundo_desc= 0
        total_BASE += pedido
    elif pedido > 12 and pedido <= 100:
        sin_descuento= PRECIO_BASE * 12
        primer_desc= descuento_10 * (pedido-12)
        segundo_desc= 0
        total_desc_10 += pedido-12
        total_BASE += 12
    else:
        sin_descuento= PRECIO_BASE * 12
        total_BASE += 12
        temp= 100-12
        primer_desc= descuento_10 * (temp) 
        segundo_desc= descuento_25 * (pedido - 100)
        total_desc_10 += temp
    

    total_neto= sin_descuento + primer_desc + segundo_desc
    precio_promedio= total_neto / pedido

    total += total_neto

    informe= f'Venta N° {contador}: TOTAL: ${total_neto}\nPRECIO PROMEDIO: ${precio_promedio}\n '
    print(informe)


print(f'TOTAL VENTA DEL DIA: ${total}')
print(f'CANTIDAD PRODUCTOS CON DESCUENTO DEL 10%: {total_desc_10}')
print(f'CANTIDAD PRODUCTOS SIN DESCUENTOS: {total_BASE}')
print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:

# C: cheque, 20% de recargo.
# E: efectivo, 10% de descuento.
# T: con tarjeta, 12% de recargo.
# Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.

# | Forma de Pago    | Total     |
# | ---------------- | --------- | 
# | Efectivo en Caja | $ xxxx.xx |
# | Tarjeta Crédito  | $ xxxx.xx |
# | Cheques          | $ xxxx.xx |
# | Total de Venta   | $ xxxx.xx |
# | Importe del IVA  | $ xxxx.xx 


dicc= {'Importe': [],
       'Forma_pago': [],
       'Total_venta': []}

efectivo= 0
cheque= 0
tarjeta= 0

while True:
    importe= input('Ingrese el importe de venta: $')
    if importe == 'f':
        break
    else:
        importe= float(importe)


    C= (importe/100)*20 ## de recargo
    E= (importe/100)*10 ## de descuento
    T= (importe/100)*12 ## de recargo 

    forma_pago= input('Ingresar la forma de pago C/E/T: ').lower()

    
    if forma_pago not in ['c','e','t']:
        print('Forma de pago no valida')
        continue
    else:
        dicc['Importe'].append(importe)
        if forma_pago == 'c':
            total_venta= importe + C
            dicc['Forma_pago'].append([forma_pago,C])
            cheque += total_venta
        elif forma_pago == 'e':
            total_venta= importe - E
            dicc['Forma_pago'].append([forma_pago,E])
            efectivo += total_venta
        else:
            total_venta= importe + T
            dicc['Forma_pago'].append([forma_pago,T])
            tarjeta += total_venta

    dicc['Total_venta'].append(total_venta)
    
total= sum(dicc['Total_venta'])
print(f'| Forma de pago     |Total       |')
print('|-------------------|------------')
print(f'| Efectivo en Caja  | $ {efectivo} ')
print(f'| Tarjeta Crédito   | $ {tarjeta}  ')
print(f'| Cheques           | $ {cheque}  ')
print(f'| Total de Venta    | $ {total}  ')
print(f'| Importe del IVA   | $ {(total / 100)*21}  ')


print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:
# Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
# Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
# Si el empleado posee estudios superiores: aumento del 5%
# Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. Se termina la carga cuando no se deseen ingresar más empleados.
# Determinar: a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo. b. Sueldo nuevo promedio de la empresa.



while True:
    sueldo= random.randint(1000,5000)
    antiguedad= random.randint(0,13)
    hijos= random.randint(0,7)
    estudios= input('Cuenta con estudios? S/N: ').lower()
    sueldo_total= 0
    if antiguedad >= 10:
        sueldo_total= sueldo + (sueldo*0.1)
    if hijos >= 2:
        sueldo_total += sueldo + (sueldo*0.1)
    elif hijos == 1:
        sueldo_total += sueldo + (sueldo*0.05)

    if estudios not in ['s', 'n']:
        print('valor no valido')
    elif estudios == 's':
        sueldo_total += sueldo + (sueldo*0.05)
    else:
        pass

    print(f'N° de empleado: {random.randint(0,1000)}\nSueldo Basico: ${sueldo}\nNuevo Sueldo: ${sueldo_total}\n')

    temp= input('Desea seguir cargando informacion de empleados? S/N: ').lower()
    if temp == 's':
        continue
    elif temp == 'n':
        break
    else:
        print('Valor invalido')
        continue




print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa que permita ingresar un número entero positivo y mostrar su factorial. El factorial de un número es el producto de todos los números enteros desde 1 hasta el número ingresado. Por ejemplo, el factorial de 5 es 1 * 2 * 3 * 4 * 5 = 120

def factorial(numero)->int:
  """ devuelve el factorial de un numero

  """
  
  if numero >1:
    numero=numero*factorial(numero-1)
  return numero

factorial()

print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.
# Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)
# Para considerarlo apto debe cumplir las siguientes condiciones:
# Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos.
# Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
# Que su promedio sea menor o igual a 18 minutos.
# Se pide:
# Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia. *Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el menor tiempo



def dia_entrenamiento():
    tiempo_prueba= random.randint(0,30)
    return tiempo_prueba

def registro():
    dias= 0
    marcas= []
    while dias < 10:
        dias += 1
        marca= dia_entrenamiento()
        marcas.append(marca)
        if marca > 20:
            print('No se cumplio con los requisitos')
            print(f'Marca de tiempo: {marca}')
            return
        else:
            continue

    for num in marcas:
        condicion= num <= 15
        if condicion in marcas:
            break
        elif condicion not in marcas:
            print('No se cumplio el requisito de marca minima')
            print(f'Marcas: {marcas}')
            return
        else:
            continue

    if (sum(marcas)/len(marcas)) > 18:
        print('No se cumplio con el requerimiento de promedio de tiempos')
    else:
        pass
        
    print(f'Promedio de tiempo: {sum(marcas)/len(marcas)}\nDia que se registro el tiempo minimo: {marcas.index(min(marcas))+1}')
    return


# def main():
#     return registro()

# main()
print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Escribir un programa para registrar y obtener información sobre los viajes diarios de un conductor de Uber.
# Cada vez que comienza un viaje se debe ingresar la distancia recorrida, indicando si el viaje fue corto (‘C’), mediano (‘M’), largo (‘L’) o si es el fin de los datos (‘Z’).
# El día finaliza cuando se llega a los 30 viajes o cuando se ingresa distancia ‘Z’ (fin de los datos).
# Por cada viaje se debe ingresar la siguiente información:
# Cantidad de pasajeros (mayor a 0 y menor a 4).
# Importe a cobrar, incluyendo la el costo básico ($180).
# Por cada pasajero de ese viaje se debe ingresar:
# Nombre.
# Edad (mayor a 18 y menor a 120 años).
# Se desea saber, para cada viaje, cuál es la persona más grande y su nombre.
# Al finalizar el día de trabajo, el programa debe informar:
# Cantidad de viajes por cada categoría (‘C’, ‘M’, ‘L’).
# Recaudación total.
# Valor promedio del viaje.
# Porcentaje de viajes cortos.
# Todos los datos ingresados deben ser validados.



def viaje(promp= 'Ingrese tipo de viaje C/M/L: ')->tuple|str|int:
    promp= input(promp).lower()
    if promp not in ['c', 'm', 'l','f']:
        print('Valor invalido')
    elif promp == 'f':
        print('Gracias por viajar con nuestra empresa!')
        return
    else:
        pass

    importe= 180

    if promp == 'c':
        importe += random.choice(range(10,50,5))
    elif promp == 'm':
        importe += random.choice(range(50,90,5))
    else:
        importe += random.choice(range(90,4000,5))
    mayor= pasajeros()
    return promp,importe, mayor

def pasajeros(pasajeros= random.randint(1,3))->dict:
    muestra= ['pepe','ernesto','julian','sofia','laura','esteban','macarena','luna','mauro','aylen','francisco']
    datos= []
    for x in range(pasajeros):
        nombre= random.choice(muestra)
        edad= random.randint(18,119)
        datos.append((nombre,edad))
        muestra.pop(muestra == nombre)
    datos.sort(key= lambda x: x[1])
    mayor= datos[-1]
    return mayor


def main():
    cant_viajes= random.randint(1,5)
    cantXcategoria= []
    recaudacion= 0
    viajesxdia= 0

    while viajesxdia != cant_viajes:
        a,b,c= viaje()
        

        cantXcategoria.append(a)
        recaudacion += b
        viajesxdia += 1
        if viajesxdia == cant_viajes:
            break
        else:
            continue

    C= cantXcategoria.count('c')
    M= cantXcategoria.count('m')
    L= cantXcategoria.count('l')
    valor_promedio= recaudacion / cant_viajes
    porc_viajes_C= round((C/len(cantXcategoria))*100,2)

    print(f'Cantidad de viajes por categoria:\nC: {C}\nM: {M}\nL: {L}\n\nRecaudacion Total: ${recaudacion}\n\nValor promedio del viaje: ${valor_promedio}\n\nPorcentaje de viajes cortos: {porc_viajes_C}%')
    return
# main()
print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
# Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
# Se desea conocer:
# Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
# El total en kg de alimento recibido.
# Promedio de alimento por tanda


def alimentar(promp= 'Cuanto alimento le vas a dar (en Kg.)?: ')->int|list:

    comidas= []

    while True:
        pregunta= input(promp)
        if pregunta.isdigit() == True:
            comida= int(pregunta)
            comidas.append(comida)
        else:
            print('Valor invalido')
            continue
        preguntar= input('El animal quiere mas comida? S/N: ').lower()

        if preguntar not in ['s','n']:
            while preguntar not in ['s','n']:
                print('Valor invalido')
                preguntar= input('El animal quiere mas comida? S/N: ').lower()
        else:
            if preguntar == 's':
                continue
            else:
                break

    return comidas

def main():

    alimentacion= alimentar()
    mas_abundante= max(alimentacion)

    print(f'La comida mas abundante fue la N°{alimentacion.index(mas_abundante)}, su cantidad fue {mas_abundante}Kg.')
    print(f'El total de alimento consumido fue: {sum(alimentacion)}Kg.')
    print(f'Promedio de alimento por tanda: {sum(alimentacion)/len(alimentacion)}Kg.')

    return





print("-"*80)
#----------------------------------------------------------------------------------------------------------

# Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.
# Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:
# Combo 1: Hamburguesa, papas fritas y gaseosa - $1550

# Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650

# Hamburguesa sola - $1300

# Hamburguesa con queso - $1400

# Gaseosa - $700

# Postre - $600

# Agregar aderezo - $100

# Terminar

# Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.
# El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.
# Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado"



def pedido(promp= 'Seleccione el N° de opcion/es que mas le guste/n:\n\n ')->int|tuple:

    opciones= ['Terminar','Combo 1: Hamburguesa, papas fritas y gaseosa - $1550','Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650','Hamburguesa sola - $1300','Hamburguesa con queso - $1400','Gaseosa - $700','Postre - $600','Agregar aderezo - $100']

    precios= [0,1550,1650, 1300,1400,700,600,100]

    while True:
        temp= input(promp)

        if temp.isdigit() != True:
            print('Valor invalido')
            continue
        elif int(temp) < 0 or int(temp) > 7:
            print('Opcion no valida')
            continue
        else:
            break
           
    return opciones[int(temp)], precios[int(temp)]

def ticket()-> str:
    subtotal= 0
    while True:

        temp= pedido()
        subtotal += temp[1]
        orden= input(f'Desea agregar otro pedido a su orden?\n(Su total hasta el momento es de ${subtotal})\nS/N: ').lower()

        if orden not in ['s','n']:
            while orden not in ['s','n']:
                print('Opcion invalida')
                orden= input('Desea agregar otro pedido a su orden? S/N: ').lower()
        elif orden == 's':
            continue
        else:
            break

    total= subtotal
    print(f'Importe a pagar: ${total}')

    return

def main():      ### la funcion main() debe mostrar y ejecutar lo que el programa hace, no COMO LO HACE...

    """ Establecemos la interfaz que se mostrará a los clientes,
        llamamos las funciones a ejecutar"""


    print('-'*15,'MENU','-'*15,'\n')
    print('1-Combo 1: Hamburguesa, papas fritas y gaseosa - $1550')
    print('2-Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650\n')
    print('3-Hamburguesa sola - $1300')
    print('4-Hamburguesa con queso - $1400\n')
    print('5-Gaseosa - $700\n')
    print('6-Postre - $600\n')
    print('7-Agregar aderezo - $100\n')
    print('0-Terminar\n')
    temp= ticket()

    return



print("-"*80)
#----------------------------------------------------------------------------------------------------------

#crea un diccionario en el cual las llaves sean numeros enteros
#y los valores sean sus cuadrados
#haz esto para n numeros.


def llaves(promp= 'Ingrese el inicio y final del rango de numeros que utilizará: ', cantidad= 'Ingrese la cantidad de llaves= '):

    while True:
        promp= input(promp)
        lista= [str(x) for x in range(10)] 
        lista.append(',')

        for x in promp:
            if x in lista:
                continue
            else:
                print('Valor invalido')
                print('Solo se permiten numeros para el rango')
                return
            
        temp= [int(x) for x in promp.split(',')]
        llaves= [x for x in range(temp[0],temp[1]+1)]

        break

    return llaves

def muestra():

    k= llaves()
    valores= [x**2 for x in k]
    dicc= dict(zip(k, valores))

    return dicc

def main():
    return muestra()
    

print("-"*80)
#----------------------------------------------------------------------------------------------------------

main()



