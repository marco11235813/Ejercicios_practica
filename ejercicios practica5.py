# Ejercicios de Tipos de Datos Simples



# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

def imprimir()-> str:
    print('Hola Mundo')
    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

def almacenar_e_imprimir(promp= 'Ingrese el texto a imprimir: ')-> str:
    variable= input(promp)
    print(variable)

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

def imprimir_usuario(promp= 'Ingrese el nombre del usuario: ')-> str:
    variable= input(promp)
    print(f'¡Hola{variable}!')

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética: ((3+2)/(2*5))²

def operacion(*args)->int|float:
    operacion= args
    print('((3+2)/(2*5))² = ',operacion)

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

def sueldo(promp1= 'Coste x hora: ', promp2= 'Horas trabajadas: ')->int:

    xhora= float(input(promp1))
    horas_trab= int(input(promp2))
    sueldo= horas_trab * xhora

    print(f'Sueldo correspondiente: ${sueldo}')
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Escribir un programa que lea un entero positivo, n
# , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n
# . La suma de los 
#  primeros enteros positivos puede ser calculada de la siguiente forma: suma= (n*(n+1))/2

def sumatoria(promp= 'Introduce un numero entero positivo(desde 1 en adelante: )')->int|str:

    numero= int(input(promp))
    suma= (numero*(numero+1))/2

    return f'Sumatoria: {suma}'



#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

def masa_corporal(promp= 'Peso(en kg): ', promp2= 'Estatura (en mts.): ')-> str:

    peso= float(input(promp))
    altura= float(input(promp2))
    masa= peso * altura 

    return f'Tu indice de masa corporal es {round(masa,2)}'


#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

def division(n: int, m: int)->int|str|None:

    c= n/m
    r= n%m

    print(f'Dividendo: {n}\nDivisor: {m}\nCOciente: {c}\nResto: {r}')

    return 


#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

def capital(promp= 'Cuanto desea invertir? $')-> str:

    inversion= float(input(promp))
    int_anual= input('Cuanto interes anual tendra la inversion (en %)? ')
    anios= input('A cuantos años poner la inversion a generar interes? ')
    capital= inversion+(inversion*(int_anual/100))*anios

    return f'Capital obtenido: ${capital}'

#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


def pedido_peso(cant_payasos: int, cant_muñecas: int)-> int|str:
    """ 
        Esta funcion toma como argumentos la cantidad de muñecos y payasos vendidos
        en el ultimo pedido ingresado, devuelve el peso total del paquete en kilos.
    """


    payaso= 112/1000
    muñeca= 75/1000

    peso_total= (cant_payasos*payaso) + (cant_muñecas*muñeca)

    return f'El peso total del paquete en el ultimo pedido es de {peso_total} kg'


#----------------------------------------------------------------------------------------------------------
# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

def cuenta_ahorros(promp= 'Ingresar el monto a depositar en la cuenta de ahorros: $')-> str|tuple:

    deposito= int(input(promp))
    int_anual= 0.04

    primero= round(deposito+(deposito*int_anual),2)
    segundo= round(primero+(primero*int_anual),2)
    tercero= round(segundo(segundo*int_anual),2)

    return f'Ahorros totales en el 1er año: {primero}\nAhorros totales en el 2do año: {segundo}\nAhorros totales en el 3er año: {tercero}\n '



#----------------------------------------------------------------------------------------------------------
# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

def ventas_pan_viejo(promp= 'Cant de barras de pan viejo que se vendieron: ')->str:

    precio= 3.49
    pan_viejo= int(input(promp))
    porc_descuento= 0.60
    descuento= (pan_viejo*precio)*porc_descuento
    total= (pan_viejo*precio)-descuento

    return f'Precio habitual del pan: €{precio}\nDescuento realizado: €{descuento}\nTotal venta: €{total}'

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
# Ejercicios de Cadenas



# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

def repeticion_nombre()->str:

    nombre= input('Ingresa el nombre de usuario: ')
    numero= int(input('Ingresa el numero de repeticiones que realizaras: '))

    print(f'{nombre}\n'*numero)

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

def nombre_completo(promp= 'Ingrese su nombre completo: ')->str:

    completo= input(promp)

    print(f'en mayusculas: {completo.upper()}\nen minusculas: {completo.lower()}\ncon la primera letra de cada nombre/s apellido/s en mayuscula: {completo.title()}')

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

def contar_letras(promp= 'Ingrese el nombre: ')->str:

    nombre= input(promp)

    return  f'{nombre} tiene {len(nombre)} letras'



#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.


def numero_telefono()->int:
    print('Nomenclatura telefonica----------> prefijo-numero-extension\nEjemplo: ------------> +34-913724710-56\n\n')
    numero= input('Ingrese el numero completo: ')
    filtro= numero.split('-')
    
    print(f'Numero Telefonico: {int(filtro[1])}')
    return 


#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

def reverse_frase(promp= 'Ingrese una frase: ')->str:
    
    frase= input(promp)
    print(frase[::-1])

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.


def modificacion_frase(promp= 'Introduzca una frase: ')->str:

    frase= input(promp).lower()
    vocales= ['a','e','i','o','u']
    frase_modificada= []
    for letra in frase:
        if letra in vocales:
            letra= letra.upper()
        print(letra, end= '')

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def mail(promp= 'Escribe tu correo electronico: ')->str:

    mail= input(promp).split('@')
    nuevo_mail= mail[0]+'@'+'ceu.es'
    print(nuevo_mail)

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

def precio()->int|tuple:

    promp= round(float(input('Introduzca un precio(con decimales): €')),2)
    precio= str(promp).split('.')
    decimales= float('0.'+precio[1])
    euros= int(precio[0])

    return euros,decimales


#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def fecha()->str:

    promp= input('Ingresa la fecha separada por "/": ').split('/')
    dia= int(promp[0])
    mes= int(promp[1])
    año= int(promp[2])

    return f'{(dia):02}/{(mes):02}/{(año):4}'


#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

def compra():
    print('Lista de compras\n')
    cesta= input('Que productos pusiste en la cesta?---> ').split(',')

    for producto in cesta:
        print(producto)

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

def inventario(cartel= 'Ingrese los datos: ')->str:
    
    print(cartel, end= '\n\n')
    nombre= input('Ingrese el producto: ')
    precio= float(input('Ingrese el precio: '))
    cantidad= int(input('Ingrese la cantidad: '))
    
    print(f'Nombre del producto: {nombre}\nPrecio unitario: {precio:0>8.2f}\nCantidad: {cantidad:03}\n\nPrecio final: {(cantidad*precio):0>10.2f}')

    return


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# Ejercicios de Condicionales


# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def mayoria_edad()->str:

    edad= input('Ingrese su edad en años: ')

    if edad < 18:
        print('Es menor de edad')
    else:
        print('Es mayor de edad')

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def contraseña()->str|None:

    password= 'contraseña'
    promp= input('Ingrese su contraseña: ')

    if promp == password:
        print('Contraseña correcta')
    else:
        print('La contraseña ingresada es incorrecta')
        
    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


def division(numero1= 'Ingrese el primer numero', numero2= 'Ingrese el segundo numero')->str|int|float:

    while True:

        a= int(input(numero1))
        b= int(input(numero2))

        try:
            division= a/b
            print(division)
            break

        except ZeroDivisionError:
            print('No se puede dividir por 0')
            continue

    return
    
#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def par_impar(promp= 'Ingrese un numero: ')-> str:

    while True:
        numero= abs(int(input(promp)))

        if numero == 0:
            print('Ingresa un numero entero diferente de 0')
            continue

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


def tributar()->str:

    edad=int(input('Ingrese su edad en años: '))
    ingresos= float(input('Ingrese sus ingresos mensuales en €: €'))

    if edad > 16 or ingresos >= 1000:
        print('Debe tributar')
    else:
        print('No deber tributar')

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def clasificacion_grupos()-> str|tuple:

    grupo_a= []
    grupo_b= []
    lista= ["a",'b','c','d','e','f'               
        ,'g','h','i','j','k','l',            
        'm','n','ñ','o','p','q','r'
        ,'s','t','u','v','w','x','y','z']

    while True:

        alumno= ()
        nombre= input('Ingresar el nombre del alumno: ').lower()
        if nombre == 'logout':
            break
        sexo= input('Ingresar el sexo del alumno V/M: ').lower()
        alumno += nombre.title(),sexo.upper()

        if (nombre[0] in lista[:12] and sexo == 'm') | (nombre[0] in lista[13:] and sexo == 'v'):
            grupo_a.append(alumno)
        else:
            grupo_b.append(alumno)

    print(f'Grupo A: {grupo_a}\nGrupo B: {grupo_b}')

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def tipo_impositivo()-> str:

    lista= ['Renta	                      Tipo impositivo:',
            '1-Menos de 10000€                     5%',
            '2-Entre 10000€ y 20000€               15%',
            '3-Entre 20000€ y 35000€               20%',
            '4-Entre 35000€ y 60000€               30%',
            '5-Más de 60000€                       45%']
    for item in lista: 
        print(item)
    
    renta_anual= float(input('Ingrese su renta anual: $'))
    print('\nRango de tipo impositivo al que corresponde:\n')
    if renta_anual < 10000:
        print(lista[1])
    elif renta_anual > 10000 and renta_anual < 20000:
        print(lista[2]) 
    elif renta_anual > 20000 and renta_anual < 35000:
        print(lista[3])
    elif renta_anual > 35000 and renta_anual < 60000:
        print(lista[4])
    else:
        print(lista[5])    
        
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.


def bono()->str:

    puntuacion= {0.0: 'Inaceptable',
                 0.4: 'Aceptable',
                 0.6: 'Meritorio'}

    promp= float(input('Ingrese el nivel de puntuacion del empleado: '))
    llaves= list(puntuacion.keys())
    bono= 2400

    if promp == 0.0:
        print(f'Nivel de Puntuacion: {puntuacion[0.0]}\nBono: € {bono*llaves[0]}')
    elif promp == 0.4:
        print(f'Nivel de Puntuacion: {puntuacion[0.4]}\nBono: € {bono*llaves[1]}')
    else:
        print(f'Nivel de Puntuacion: {puntuacion[0.6]}\nBono: € {bono*llaves[2]}')

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


def precio_entrada()->str:

    edad= int(input('Ingrese la edad del cliente: '))

    if edad < 4:
        print('Precio de la entrada: Sin costo')
    elif edad >= 4 and edad <= 18:
        print(f'Precio de la entrada: € {5}')
    else:
        print(f'Precio de la entrada: € {10}')


    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

def pizza()->str:

    basicos= ['mozzarella', 'tomate']
    vegetarianos= ['pimientos', 'tofu']
    no_vegetarianos= ['peperoni', 'jamon','salmon']

    while True:
        pedido= input('Quiere pedir una pizza vegetariana? SI/NO:  ').lower()

        if pedido in ['si', 'no']:   
            if pedido == 'si':
                print(f'Su pedido es una pizza vegetariana----> Ingredientes: {basicos + vegetarianos}')
                break
            else:
                print(f'Su pedido es una pizza no vegetariana----> Ingredientes: {basicos + no_vegetarianos}')
                break
        else:
            print('Ingreso no valido')
            continue

    return


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# Ejercicios de Bucles



# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def palabra(promp= 'Ingrese una palabra: ')->str:

    contador= 0

    while contador < 10:
        contador += 1
        palabra= input(promp)
        print(palabra)


    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def edad(promp= 'Ingrese su edad en años: ')-> int|object|tuple:

    edad= int(input(promp))

    for x in range(1,edad+1):
        print(x)

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def impares()-> tuple|list|int:

    numero= abs(int(input('ingresa un numero entero positivo: ')))
    tupla= ()
    for x in range(numero+1):
        if x%2 == 1:
            print(x,end= ',')
            tupla += x,
        else:
            continue
    # print(tupla)
    return 

#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def reverse()->tuple|int|list:

    numero= abs(int(input('ingresa un numero entero positivo: ')))

    for x in range(numero,-1,-1):
        print(x,end= ',')

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


def capital_obtenido()->str:

    inversion= float(input('Ingrese la cantidad a invertir: $'))
    interes_anual= (int(input('interes anual')))/100
    anios= int(input('Ingrese a cuantos años es la inversion: '))

    capital_obtenido= inversion + ((inversion*interes_anual)*anios)
    print(f'Capitañ obtenido: ${capital_obtenido}')

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

def triangulo_rectangulo()-> str:

    numero= int(input('Ingrese un numero entero: '))

    for x in range(1,numero+1):
        print('*'*x)
        
    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablas(promp= 'Ingrese la tabla que desea ver: '):

    while True:
        tabla= int(input(promp))

        if tabla > 10:
            print('Solo puede ingresar una tabla del 1 al 10')
            continue
        else:
            print(f'Tabla del {tabla}:\n')
            for x in range (1,11):
                print(f'{tabla} x {x} = {tabla*x}')
        break
    
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

def triangulo_rectangulo2()-> list|int:

    numero= int(input('Ingrese un numero entero: '))
    repeticiones= int(input('Ingrese la extension de la base del triangulo: '))
    registro= ()
    condicion= 0
    while condicion <= repeticiones:

        condicion += 1

        if len(registro) == 0:
            registro += numero,
        else:
            temp= len(registro)
            for x in registro[::-1]:
                print(x, end= ' ')
                temp -= 1
                
                if temp == 0:
                    print('')
                
            registro += numero,

        numero += 2
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


def contraseña()->str|None:

    while True:
        password= 'contraseña'
        promp= input('Ingrese su contraseña: ')

        if promp == password:
            print('Contraseña correcta')
            break
        else:
            print('La contraseña ingresada es incorrecta')
            continue
            
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


def primo_o_no()->str|bool:

    numero= int(input('Ingrese un numero entero positivo: '))
    primo= True

    if numero <= 1:
        print('Valor invalido')
    else: 
        for x in range (2,numero):
            if numero%x == 0:
                primo= False
                break
            else:
                continue

    if primo == True:
        print('El numero es primo')
    else:
        print('El numero no es primo')


    return




#----------------------------------------------------------------------------------------------------------
# Ejercicio 11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def reverse_palabra(promp= 'Intoduce una palabra/frase: ')->str:

    palabra= input(promp)

    for letra in palabra[::-1]:
        print(letra)

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def contador_letras()-> int:

    frase= input('Introduce una frase o palabra: ')
    letra= input('introduce la letra a buscar: ')

    print(letra, '----->', frase.count(letra), 'veces')

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def eco()->str:

    while True:
        palabra= input('Introduce una palabra: ')

        if palabra.lower() == 'salir':
            break
        else:
            print(palabra)

    return



#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# Ejercicios de Listas y Tuplas



# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

def asignaturas()->list:

    asignaturas= input('Ingrese la materia: ')
    materias= []
    materias.append(asignaturas)

    while asignaturas.lower() != 'exit':
        asignaturas= input('Ingrese la materia: ')
        if asignaturas.lower() == 'exit':
            continue
        else:
            materias.append(asignaturas)

    return materias

#----------------------------------------------------------------------------------------------------------
# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

def asignaturas_cursadas()->list|str:

    asignaturas= input('Ingrese la materia: ')
    materias= []
    materias.append(asignaturas)

    while asignaturas.lower() != 'exit':
        asignaturas= input('Ingrese la materia: ')
        if asignaturas.lower() == 'exit':
            continue
        else:
            materias.append(asignaturas)

    for x in materias:
        print(f'Yo estudio {x}')
        
    return 

#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

def calificaciones()->str:

    materias= ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    
    for materia in materias:
        nota= int(input(f'Ingresa la nota que el alumno a sacado en {materia}: '))
        if nota <= 10 and nota >= 0:
            print(f'En {materia} has sacado {nota}')
        else:
            while nota > 10 or nota < 0:
                print('Valor invalido,el valor debe estar entre 0 y 10')
                nota= int(input(f'Ingresa la nota que el alumno a sacado en {materia}: '))
            print(f'En {materia} has sacado {nota}')

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

def loteria(promp= 'Ingrese un numero: '):

    print('Ingrese los numeros ganadores de la loteria:\n')
    billete= []

    while len(billete) < 6:
        numero= int(input(promp))
        billete.append(numero)

    billete.sort()
    print(f'Numeros ganadores: {billete}')

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

def lista_inversa()->int|tuple:

    lista= range(1,11)

    for x in lista[::-1]:
        print(x, end= ',')

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


def recursar_materias()->str:

    materias= ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    
    for materia in materias:
        nota= int(input(f'Ingresa la nota que el alumno a sacado en {materia}: '))
        if nota < 6 and nota >= 0:
            print(f'En {materia} has sacado {nota}')
            print('Debes recursarla')
        else:
            while nota > 10 or nota < 0:
                print('Valor invalido,el valor debe estar entre 0 y 10')
                nota= int(input(f'Ingresa la nota que el alumno a sacado en {materia}: '))
                if nota < 6 and nota >= 0:
                    print(f'En {materia} has sacado {nota}')
                    print('Debes recursarla')
                    break

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def sacar_letras()->list:

    lista= ["a",'b','c','d','e','f'               
        ,'g','h','i','j','k','l',            
        'm','n','ñ','o','p','q','r'
        ,'s','t','u','v','w','x','y','z']

    for idx,letra in enumerate(lista):
        if idx == 0:
            continue
        elif idx%3 == 0:
            lista.pop(idx)
            print(idx)
        else:
            continue
    print(lista)

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def palindromo()->str:

    palabra= input('Inserte una palabra o frase: ').lower()
    palabra= palabra.replace(' ', '')

    if palabra.strip() == palabra[::-1].strip():
        print('La palabra/frase es palindromo')
    else:
        print('La palabra/frase no es un palindromo')

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

def contador_vocales(promp= 'Ingrese una palabra: '):

    palabra= input(promp).lower()
    vocales= ['a','e','i','o','u']

    for vocal in vocales:
        if vocal in palabra:
            print(f'La vocal "{vocal}" se repite {palabra.count(vocal)} veces')
        elif vocal not in palabra:
            print(f'La vocal "{vocal}" no esta en {palabra}')
        else:
            continue
        
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

def precio_mayorymenor()->str|int:

    precios= [50,75,46,22,80,65,8]


    print(f'Precio mayor: {max(precios)}')
    print(f'Precio mayor: {min(precios)}')

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

def producto_escalar()-> int|float|str|None:

    vector1= (1,2,3)
    vector2= (-1,0,3)
    producto= 0
    for x,y in zip(vector1,vector2):
        temp= x*y
        producto += temp

    print(f'El producto escalar es: {producto}')

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 12
# Escribir un programa que almacene las matrices
 
# a= ([1 2 3]       b= ([-1 0
#      4 5 6])            0 1
#                         1 1])
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.



#----------------------------------------------------------------------------------------------------------
# Ejercicio 13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

def estadisticos(promp= 'Ingrese una serie de numeros separados por coma: ')->str:

    import numpy as np

    matriz= input(promp).split(',')
    matriz= [int(x) for x in matriz]

    print(f'Media de la muestra: {np.mean(matriz)}\nDesviacion Estandar de la muestra: {np.std(matriz)}')
    
    return

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# Ejercicios de Diccionarios



# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def divisa():

    divisas= {'Euro': '€',
              'Dollar': '$',
              'Yen': '¥'}
    
    promp= input('Ingresa una divisa').lower().title()

    if promp in divisas.keys():
        print(divisas[promp])
    else:
        print('Divisa invalida')

    
    return
#otra manera
def divisa2()->str|dict:

    nombres=['Euro','Dollar','Yen']
    simbolos= ['€','$','¥']

    divisas= dict(zip(nombres,simbolos))
    promp= input('Ingresa una divisa').lower().title()

    if promp in divisas.keys():
        print(divisas[promp])
    else:
        print('Divisa invalida')

    return

#----------------------------------------------------------------------------------------------------------       
# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def datos_personales()->str:

    dicc= {'nombre': input('Ingresa un nombre: ').title(),
            'edad': int(input('Ingresa la edad en años: ')),
            'direccion': input('Ingresa la direccion: '),
            'telefono': int(input('Ingresa su numero de telefono/celular: '))}


    print(f'{dicc["nombre"]} tiene {dicc["edad"]} años, vive en {dicc["direccion"]} y su numero de telefono es {dicc["telefono"]}')

    return
#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70


def verduleria()->str:

    verduras= {'Platano': 1.35,
               'Manzana': 0.80,
               'Pera': 0.85,
               'Naranja': 0.70}
    
    while True:
        pedido= input('Que va a comprar hoy?: ').title()
        peso= float(input('Cuanto va a llevar? (en kgs): '))

        if pedido in verduras.keys():
            print(f'El costo total de {pedido} es de ${verduras[pedido]*peso}')
            break
        else:
            print('No tenemos en stock el producto ingresado')
            promp= input('Desea realizar otro pedido? SI/NO: ')
            if promp == 'si':
                continue
            elif promp == 'no':
                break
            
    return
#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

def fecha()-> str:

    fecha= input('Ingresa la fecha separada por /: ').split('/')
    dicc= {'dia': fecha[0],
           'mes': fecha[1],
           'año': fecha[2]}
    
    print(f'{int(dicc["dia"]):02} de mes {int(dicc["mes"]):02} de {int(dicc["año"]):4}')

    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

def calificaciones2()->str:

    materias= ['Matematicas', 'Fisica','Quimica']
    print('Ingrese las calificaciones por materia:\n')
    total= 0
    for materia in materias:
        calificacion= int(input(f'{materia}: '))
        total += calificacion
        print(f'{materia}: {calificacion}')

    print(f'\nTotal de puntos: {total}')

    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def registro()->str:

    persona= {}
    condicion= True

    while condicion:
        ingreso= input('Ingresa los datos: ')

        if ':' in ingreso:
            ingreso= ingreso.split(':')
            persona.setdefault(ingreso[0],ingreso[1])
            print(persona)
        elif ingreso.lower() == 'exit':
            break
        else:
            print('Valor o sintaxis de carga invalida')
            continue

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste

def carrito():

    carrito= {}
    condicion= True
    total= 0
    while condicion:
        ingreso= input('Ingresa el producto y el precio: ')

        if ':' in ingreso:
            ingreso= ingreso.split(':')
            carrito.setdefault(ingreso[0],ingreso[1])
            total += float(ingreso[1])
        elif ingreso.lower() == 'exit':
            break
        else:
            print('Valor o sintaxis de carga invalida')
            continue
    for item in carrito.items():
        print(f'{item[0]}     ${item[1]}')
    print('-'*80)
    print(f'Total de coste: ${total}')
    
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

def traductor()->str|dict:

    dicc= {}
    stop= False

    while stop == False:
        pares= input('Introduce los pares palabra:valor separados por coma: ')

        if pares.lower() == 'exit':
            break
        else:
            pares= pares.split(',')

        for par in pares:
            par= par.split(':')
            dicc.setdefault(par[0].strip(),par[1].strip())


    frase= input('Ingresa la frase a traducir: ').split(' ')
    new_frase= False
    for palabra in frase:
        if palabra.lower() in dicc.keys():
            palabra_trad = dicc[palabra.lower()]
            if new_frase == False:
                print(palabra_trad.title(), end= ' ')
                new_frase= True
            else:
                print(palabra_trad, end= ' ')
        else:
            print(palabra, end= ' ')

    return 


#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

def gestor(promp= 'Ingrese el nombre de usuario: ')->str:


    usuario= input(promp)
    dicc= {}
    datos= {}
    print(f'Bienvenido {usuario}\n')
    total_pagado= 0
    total_adeudado= 0
    dicc.setdefault(usuario,datos)

    while True:

        gestion= input('Seleccione la gestion a realizar:\n\n1--Ingreso de factura\n2--Pago de factura\n\n')


        if gestion.lower() in ['terminar', 'exit', 'logout']:
            break
        elif int(gestion) == 1:
            ingreso= input('Ingrese el N° de factura seguido de su importe en $(separados por coma): ').split(',')
            if len(ingreso) != 2:
                print('Ingreso invalido')
                while len(ingreso) != 2:
                    ingreso= input('Ingrese el N° de factura seguido de su importe en $(separados por coma): ').split(',')
            datos.setdefault(ingreso[0],float(ingreso[1].strip()))
            total_adeudado += float(ingreso[1])
        elif int(gestion) == 2:
            print(f'Facturas registradas:\n{dicc[usuario]}')
            ingreso= input('Ingrese el N° de factura a pagar: ')
            print(f'\nMonto a pagar: {dicc[usuario][ingreso]}\n')
            total_pagado += dicc[usuario][ingreso]
            total_adeudado -= dicc[usuario][ingreso]
            dicc[usuario].pop(ingreso)
        else:
            print('Valor invalido. Ingrese un valor nuevamente')
            continue

        print(f'\nTotal pagado: ${total_pagado}\nTotal adeudado: {total_adeudado}\n')
        
    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.
db_clientes= {}

#nombre, direccion, telefono, correo, preferente
def gestor_db(promp= 'Ingrese el NIF de usuario: ')->str:

    llaves= ['Nombre', 'Direccion', 'Telefono', 'Correo', 'Preferente']
    print(f'Bienvenido al Sistema de Gestion de Usuarios\n')

    while True:

        datos= {}
        try:
            gestion= int(input('Seleccione la gestion a realizar:\n\n1--Añadir cliente\n2--Eliminar cliente\n3--Mostrar Cliente\n4--Listar todos los clientes\n5--Listar Clientes preferentes\n6--Terminar\n\n'))
        except ValueError:
            print('Tipo de valor invalido.\nIngrese entre las opciones numericas de la lista.\n')
            print('-'*100)
            continue

        if gestion == 6:
            print('Gracias por utilizar nuestro servicio')
            break
        elif gestion == 1:
            print(f'Gestion N°{gestion}\n')
            while True:
                try:
                    usuario= int(input(promp))
                    break
                except ValueError:
                    print('NIF invalido')
                    print('-'*100)
                    continue
            if usuario in db_clientes:
                print('El NIF de usuario ya existe')
                print('-'*100)
                continue
            else:
                pass

            for key in llaves:
                ingreso= input(f'{key}: ').strip()
                datos.setdefault(key,ingreso)
            db_clientes.setdefault(usuario,datos)

        elif gestion == 2:
            print(f'Gestion N°{gestion}\n')
            ingreso= input('Ingrese el NIF del Cliente: ')
            if ingreso in db_clientes.keys():
                confirmacion= input(f'Esta seguro que desea eliminar los datos de la cuenta {ingreso}? Si/NO: ').lower()
                if confirmacion in ['si','no']:
                    if confirmacion == 'si':
                        db_clientes.pop(ingreso)
                    else:
                        continue
            else:
                print('N° de NIF inexistente')
                print('-'*100)
                continue

        elif gestion == 3:
            print(f'Gestion N°{gestion}\n')
            ingreso= int(input('Ingrese el NIF del Cliente: '))
            if ingreso in db_clientes.keys():
                print(f'N° de NIF: {ingreso}---- Datos: {db_clientes[ingreso]}')
                print('-'*100)
            else:
                print('N° de NIF inexistente')
                print('-'*100)
                continue

        elif gestion == 4:
            print(f'Gestion N°{gestion}\n')
            for user in db_clientes.items():
                print(f'N° de NIF: {user[0]}-----Nombre: {user[1]["Nombre"]}')
            print('-'*100)
        elif gestion == 5:
            print(f'Gestion N°{gestion}\n')
            for user in db_clientes.items():
                if user[1]["Preferente"] == str(True):
                    print(f'N° de NIF: {user[0]}-----Nombre: {user[1]["Nombre"]}')
                else:
                    continue
                print('-'*100)
        else:
            print('Valor fuera de rango. Ingrese un valor nuevamente')
            continue

        
    return



#----------------------------------------------------------------------------------------------------------
# Ejercicio 11
# El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

# "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

# Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

# {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}


def formatear_datos()->dict:    

    datos= input('Ingrese los datos a formatear: ').replace(';', ',').replace('"', '')
    temp= datos.split('\\n')

    campos= temp[0].split(',')
    campos.pop(0)
    temp= [x.split(',') for x in temp][1::]
    nif= [x[0] for x in temp]
    dicc= {}

    for x in temp:
        x.pop(0)

    for index, x in enumerate(temp):
        valores= {}
        for idx,y in enumerate(campos):
            valores.setdefault(y,x[idx])
        dicc.setdefault(nif[index],valores)

    print(dicc)

    return


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


# Ejercicios de Funciones



# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludo()->str:
    print('!Hola amiga¡')
    return


#----------------------------------------------------------------------------------------------------------
# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludo2()->str:

    nombre= input('Ingresa un nombre: ')
    print(f'!Hola {nombre}¡')

    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(n)->int:

    n= abs(int(n))
    if n > 1:
        n= n*factorial(n-1)

    return n

#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def facturacion_con_IVA(importe:float, iva= 21)->str:

    iva= iva/100
    importe_iva= importe*iva
    total= importe+importe_iva

    print(f'Facturacion sin IVA: ${importe}\nImporte de IVA: ${importe_iva}\nFacturacion con IVA: ${total}')
    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math
def area_circulo(radio:float)->float:
    # podriamos utilizar el valor 3,14 para pi pero para un calculo mas exacto, preferi importar el modulo math la variable pi

    area= math.pi * (radio**2)

    return area

def volumen_cilindro(radio,altura)->float:

    volumen= area_circulo(radio)*altura

    return volumen
#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media(*args)->int|float:

    while True:
        try:
            if len(args) == 1 and type(args[0]) == list or type(args[0]) == tuple:
                media= sum(args[0])/len(args[0])
                break
            else:
                lista= list(args)
                media= sum(lista)/len(lista)
                break
        except TypeError:
            print('EL tipo de dato no se puede leer o transformar como lista.')
            return

    return media

#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def al_cuadrado(*args)->str|list:

    while True:
        try:
            if len(args) == 1 and type(args[0]) == list or type(args[0]) == tuple:
                cuadrado= [x**2 for x in args[0]]
                break
            else:
                lista= list(args)
                cuadrado= [x**2 for x in lista]
                break
        except TypeError:
            print('EL tipo de dato no se puede leer o transformar como lista.')
            return

    return cuadrado

#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.


## en este caso, para simplificar, usaremos el modulo numpy que cuenta con funcionalidades en estadisticos (varianza y desviacion estandar entre muchos otros)
import numpy as np
def estadisticos(*args):
    llaves= ['Media', 'Varianza', 'Desvio estandar']

    while True:
        try:
            if len(args) == 1 and type(args[0]) == list or type(args[0]) == tuple:
                mean= media(args)
                varianza= np.var(args)
                desvio= np.std(lista)
                estadisticos= dict(zip(llaves,[mean,varianza,desvio]))
                break
            else:
                lista= list(args)
                mean= media(lista)
                varianza= np.var(lista)
                desvio= np.std(lista)
                estadisticos= dict(zip(llaves,[mean,varianza,desvio]))
                break
        except TypeError:
            print('EL tipo de dato no se puede leer o transformar como lista.')
            return

    return estadisticos

#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def mcd_y_mcm(numero1,numero2)->str:

    """Funcion que toma 2 numeros y obtiene su Maximo Comun Divisor (mcd)
        y su Minimo Comun Multiplo (mcm)"""

    if numero1 < 1 or numero2 < 1:
        print('Valor invalido')
        return
    else:
        valores= [numero1,numero2]      #declaramos las variables que vamos a utilizar
        divisores_1= []
        divisores_2= []
        primos= []
        coincidencias= []
        mcd= 1
        mcm= 1

        for numero in valores:          #obtenemos nuestros numeros primos dentro del rango del maximo numero
            for x in range(2,numero+1):
                primo= True
                for y in range(2,x):
                    if x == y:
                        break
                    elif x%y == 0:
                        primo= False
                        break
                if x in primos:
                    continue
                elif primo == True:
                    primos.append(x)


        for idx,numero in enumerate(valores):       # agregamos los factores primos a cada lista correspondiente
            while numero > 1:
                for x in primos:
                    while numero%x == 0:
                        numero /= x
                        if idx == 0:
                            divisores_1.append(x)
                        else:
                            divisores_2.append(x)

        
        factores_primos= list(set(divisores_1)) + list(set(divisores_2))        ## Obtenemos los factores primos comunes entre ambas listas

        for x in divisores_1:
            for idx,y in enumerate(divisores_2):
                if x == y:
                    coincidencias.append(x)
                    divisores_2.pop(idx)
                    break
                else:
                    continue

        for x in coincidencias:             # Obtenemos el Maximo Comun Divisor
            mcd *= x
        for x in factores_primos:           # Obtenemos el Minimo Comun Multiplo
            mcm *= x


    print(f'Maximo Comun Divisor entre {numero1} y {numero2}: {mcd}\nMinimo Comun Multiplo entre {numero1} y {numero2}: {mcm}')
    return

#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def decimal_a_binario():

    temp= int(input('Ingresa un numero: '))
    numero= temp
    restos= []
    cadena= None

    while numero != 0:
        restos.append(str(numero%2))
        numero= numero//2

    for x in restos:
        if cadena == None:
            cadena = x
        else:
            cadena += x

    binario= int(cadena[::-1])

    return binario

def binario_a_decimal(binario):

    temp= str(binario)
    numero= [x for x in temp]
    resultados= []

    for idx,x in enumerate(temp[::-1]):
        resultados.append(int(x)*(2**idx))

    return sum(resultados)

#----------------------------------------------------------------------------------------------------------
# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def contador_palabras():

    cadena= input('Ingrese una frase: ').lower().split()
    dicc= {}
    llaves= set(cadena)

    for x in llaves:
            valor= cadena.count(x)
            dicc.setdefault(x,valor)

    return dicc

def moda():

    dicc= contador_palabras()
    maximo= max(dicc.values())

    for llave,valor in dicc.items():
        if valor == maximo:
            print(f'La moda de este conjunto de datos es: {(llave,valor)}')

    return


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# Ejercicios de Programación Funcional


#----------------------------------------------------------------------------------------------------------
# Ejercicio 1
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 2
# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 3
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 4
# Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 5
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 6
# Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 7
# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 8
# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 9
# Escribir una función que calcule el módulo de un vector.

#----------------------------------------------------------------------------------------------------------
# Ejercicio 10
# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

# Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
# Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
#----------------------------------------------------------------------------------------------------------
# Ejercicio 11
# Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
def main():
    return


if __name__ == '__main__':
    main()