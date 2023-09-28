# Escribir un programa que permita que el usuario ingrese su nombre. El programa debe emitir una salida con un
#mensaje de bienvenida que incluya el nombre ingresado. 


a= input("Hola! porfavor ingrese su nombre: ").lower()
lista= ["a",'b','c','d','e','f'               ## en este caso creamos una lista con los valores del diccionario, para realizar una comparacion 
        ,'g','h','i','j','k','l',             ## de cada caracter del valor obtenido y evitar que se mezclen caracteres erroneos
        'm','n','ñ','o','p','q','r'
        ,'s','t','u','v','w','x','y','z']
ejecucion= True
for letra in a: 
    if letra not in lista:
        ejecucion= False
        break
    else:
        continue

if ejecucion == False:
    print("caracter incorrecto")
else:
    print(f"Bienvenido {a.capitalize()} a IT Masters!!\n\n")


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


# Escribir un programa que solicite al usuario su nombre y su edad, y luego muestre por pantalla un mensaje que diga 
# "Hola, [nombre]. Tu edad es [edad] años."


a= str(input("Buenas tardes, ingrese su nombre: "))
edad= int(input("tambien ingrese su edad con numeros: "))
print("perfecto!")
print(f"hola {a.capitalize()}. Tu edad es {edad} años.\n\n")
# print("hola {}. Tu edad es {} años.". format(a,edad))

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que solicite al usuario su nombre y su edad, después pida una cantidad de años y muestre por pantalla un 
# mensaje que indique cuántos años tendrá la persona después de sumarle a su edad la cantidad de años ingresada. 
# El mensaje debe tener el siguiente formato: 'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".


a= str(input("Buenas tardes, ingrese su nombre: "))
edad= int(input("y edad xD: "))
cantidad= int(input("ahora, ingresa un numero que seran los años que quieres sumar a tu edad: "))
resultado= edad + cantidad
print('Hola, {}. Dentro de {} años tendrás {} años\n\n'.format(a.capitalize(), cantidad, resultado))

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar 
# los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".

print("Hola, porfavor ingrese los numeros en sucesion:\n")
numero1= int(input('el primero: '))
numero2= int(input('el segundo: '))
numero3= int(input('el tercero: '))
resultado= numero1+ numero2+ numero3
print(f'la operacion es: {numero1} + {numero2} + {numero3}= {resultado}\n\n')

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que solicite al usuario ingresar dos notas de un alumno. El programa debe mostrar por pantalla el promedio de las notas de la siguiente 
# manera: "Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".

print("Ingrese las notas del alumno:\n")
nota1= int(input("Primera nota-- "))
nota2= int(input("Segunda nota-- "))
promedio= float((nota1+nota2)/2)

print(f'Notas: {nota1}, {nota2}.  promedio= {promedio}\n\n')

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



#Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas separadas por comas en un 
#renglón y el promedio de las notas en el siguiente renglon.

print('Del alumno requerido:\n')
nota1=int(input("ingrese la primera calificacion: "))
nota2=int(input("ingrese la segunda calificacion: "))
nota3=int(input("ingrese la tercera calificacion: "))
promedio= (nota1+ nota2+ nota3)/3
print(f'las notas son: {nota1}, {nota2}, {nota3}\ny el promedio del alumno es: {promedio}\n\n')

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------




# Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
# a. Multiplicado por 10. (utilizar el operador *) 
# b. Dividido por 10. (utilizar el operador /) 
# c. Elevado al cuadrado. (utilizar el operador **)
# Cada resultado debe mostrarse en una línea distinta.


numero= int(input("Ingresar un numero: "))
print(f'el resultado del numero multiplicado por 10 es {numero*10}\nsi lo dividieramos por 10 seria {numero/10}\ny si realizamos la potencia al cuadrado su resultado seria {numero**2}\n\n')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



#Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas trabajadas por día, para calcular el salario 
# semanal de un trabajador que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, suponiendo que todas las horas tienen el mismo 
# valor."

pagaxhora= float(input("ingrese la paga por hora: $"))
horas_trabajadas= int(input('ingrese las horas laborales trabajadas por dia: '))

pagaxsemana= ((pagaxhora * horas_trabajadas)* 6) - (pagaxhora * horas_trabajadas)/2
print(f'el empleado gana ${pagaxsemana} de salario semanal\n\n')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



#Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. Una vez cargadas, mostrar ambas variables por pantalla, 
# intercambiá sus valores (que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.

num1=input("ingresar un valor: ")
num2=input("ingresa un segundo valor: ")

if type(num1) != type(num2):
    type(num2) == type(num1)

print(f'los valores ingresados son:\nvalor1--- {num1}\nvalor2--- {num2}\n')

temp= num1
num1= num2
num2=temp
print(f'Actualizamos con un intercambio los valores y quedaron asi:\nvalor1--- {num1}\nvalor2--- {num2}\n\n')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa para resolver el siguiente problema:
# Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.
# Escribir un programa que permita resolver el siguiente problema:
# Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una 
# (indicando nombre y porcentaje).
# Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido 
# previamente.


persona1= int(input("persona1, invierte $"))
persona2= int(input("persona2, invierte $"))
persona3= int(input("persona3, invierte $"))
inversores= [persona1, persona2, persona3]
nombres= ["persona1", "persona2", "persona3"]


for persona, nombre in zip(inversores, nombres):
    porcentaje= persona/sum(inversores)
    print(f"el inversor {nombre} realizo una inversion de {persona}, que representa el {round((porcentaje*100), 2)}% del total de la inversion")

# tambien se puede hacer asi:

def porcentaje_inversores(a,b,c): ## creamos una funcion

    """Esta funcion obtiene 3 valores como parametros y
    obtiene el porcentaje que cada uno de los valores representa sobre la suma total de todos
    devuelve una cadena especificando el numero de inversor, y su participacion en porcentaje 
     en la inversion total"""

    lista=[a,b,c]
    a= []
    for idx, inversor in enumerate(lista, 1):
        porcentaje= round((float(inversor/sum(lista))*100), 2)   
        a.append(f'el inversor N° {idx} tiene un porcentaje del {porcentaje}% del total de la inversion realizada\n')
    return a



#o asi

class inversor:  ## creamos la clase inversor
    def __init__(self, nombre, inversion):
        self.nombre= str(nombre)
        self.inversion= float(inversion)

a= inversor("Martin", 8000)### creamos los objetos inversor
b= inversor('Julian', 4030)
c= inversor('Esteban', 10500)

porcentaje= porcentaje_inversores(a.inversion, b.inversion, c.inversion)
inversor1, inversor2, inversor3= porcentaje ## desempaquetamos cada uno de los valores que nos devuelve la funcion porcentaje_inversores y asignamos cada uno a una variable
print(f'\nen la fundacion de la empresa, {a.nombre} {inversor1},\n{b.nombre} {inversor2},\ny {c.nombre} {inversor3}\n\n')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos 
# interiores de un triángulo. Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.
# Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. Es decir, la suma de los ángulos 
# internos de un triángulo siempre es igual a 180 grados. Por lo tanto, para calcular el ángulo restante es necesario restar la suma de 
# los dos ángulos interiores ingresados al valor 180."
# Para pensar:
# ¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?
# ¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?

print("\ningresar los valores queridos uno despues del otro:\n")
angulo1= abs(int(input("1°: ")))
angulo2= abs(int(input("2°: ")))
# la suma de todos los angulos interiores de un triangulo es de 180°

angulo_restante= 180-angulo1-angulo2
print(f"el angulo restante es de {angulo_restante} gradosn\n\n")

# ¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?----- los angulos negativos se empiezan a medir desde el eje positivo x
# para todo angulo negativo existe su correspondiente positivo, es decir, se puede obtener su valor absoluto como angulo

# ¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?---- ya no serian angulos pertenecientes a un traingulo, 
# seria otra figura geometrica


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------




# Escribir un programa para calcular el importe a cobrar por un vendedor, considerando su sueldo fijo de $200000 pesos más el 16% del monto total de ventas realizadas durante un mes.
# Pensando los pasos para resolver el problema:
# Solicitar al usuario que ingrese el monto total de ventas realizadas por el vendedor durante el mes en una variable correspondiente.
# Calcular el 16% del monto total de ventas realizadas y almacenar el resultado en una variable.
# Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.
# Mostrar el importe a cobrar por el vendedor.
# Para pensar:
# ¿Qué pasaría si se modificara el sueldo fijo del vendedor?
# Si se modifica el sueldo fijo del vendedor, entonces la fórmula utilizada para calcular el salario total debería ser actualizada para 
# reflejar el nuevo sueldo fijo. En este caso, si el sueldo fijo aumenta, entonces el salario total también aumentaría. De igual manera, 
# si el sueldo fijo disminuye, entonces el salario total también disminuiría. Es importante actualizar la fórmula en el programa para 
# asegurarse de que el cálculo del salario total sea preciso y refleje el cambio en el importe a cobrar por del vendedor.
# ¿Hay que modificar el programa cada vez? ¿Cómo lo soluciono?



ventas= int(input("ingrese el monto mensual de ventas del vendedor: "))
sueldo_fijo= 200000
comision= (ventas/100)*16
a_cobrar= sueldo_fijo + ventas + comision

print(f'a cobrar: ${a_cobrar}')

# ¿Qué pasaría si se modificara el sueldo fijo del vendedor?--- modificaria el monto fijo y tambien el saldo absoluto de la comision

# Si se modifica el sueldo fijo del vendedor, entonces la fórmula utilizada para calcular el salario total debería ser actualizada para 
# reflejar el nuevo sueldo fijo. En este caso, si el sueldo fijo aumenta, entonces el salario total también aumentaría. De igual manera, 
# si el sueldo fijo disminuye, entonces el salario total también disminuiría. Es importante actualizar la fórmula en el programa para 
# asegurarse de que el cálculo del salario total sea preciso y refleje el cambio en el importe a cobrar por del vendedor.
# ¿Hay que modificar el programa cada vez? ¿Cómo lo soluciono?------ asignando variables a la operacion en lugar de constantes, el programa
# va a actualizar el sueldo a cobrar automaticamente aunque se modifiquen los valores de las variables.


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros, junto con el valor del metro cuadrado de 
# tierra. El programa debe calcular y mostrar el valor total del terreno. Además, debe calcular la cantidad de metros de alambre necesarios 
# para cercar completamente el terreno a tres alturas distintas.



ancho=int(input("Ingresar el ancho en mts. del terreno: "))
largo=int(input("Ingresar el largo en mts. del terreno: "))
valor_mts2=float(input("Valor x metro cuadrado: $"))

valor_total= (ancho*largo)*valor_mts2 ## valor total de la superficie

perimetro= (ancho*2) + (largo*2)## lados del terreno.perimetro--------(suponiendo que los lados opuestos miden lo mismo)
superficie= ancho*largo  ##superficie en mts²

valor_alambre_mts= int(input("ingresar el valor del alambre a comprar: $"))## valor x metro
alambrado= perimetro*3 ##total de mts que necesitamos de alambre para el terreno para tres alturas diferentes
costo_alambrado= alambrado*valor_alambre_mts

print(f'el valor del terreno de {superficie}mts² es de ${valor_total}')
print(f'mientras que el presupuesto que nos dieron para {alambrado}mts de alambre, que necesitamos para alambrar a 3 alturas es de ${costo_alambrado}')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas 
# ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.
# Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
# ¿Sobran datos? ¿Qué datos sobran?


vendedor= input("Vendedor: ").capitalize()
salario_base= 200000 ## asignamos el salario base, en todo caso lo puede ingresar el usuario a traves de un input
comision_fija= 0.10### la comision fija esta supeditada a la cantidad de ventas realizadas por el vendedor, deberia existir una tabla con el rango de ventas y la comision asignada para cada rango
comision_relativa= 0.05
cant_ventas= int(input("Cant. de ventas realizadas este mes: "))
total_monto_ventas= float(input("Valor total de las ventas: $"))
salario_total= int(salario_base + (total_monto_ventas * (comision_fija+comision_relativa)))

print(f'Al vendedor {vendedor}, le corresponde este mes cobrar de salario ${salario_total}')


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


# Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. Luego, el programa debe convertir ese período de 
# tiempo a una forma más legible y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. El resultado 
# se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados y su equivalente en días, horas, minutos y segundos.


segundos= int(input("ingresa la cantidad de segundos: "))
minutos= 0
horas= 0
dias= 0

while segundos >= 60:
    minutos += 1
    segundos -= 60
    if minutos >= 60:
        horas += 1
        minutos -= 60
        if horas >= 24:
            dias += 1
            horas -= 24
else:
    print(f"Mensaje: {dias}--{horas}:{minutos}:{segundos}")



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

# ¡Ayuda! Se me rompió el programa que convierte una cantidad de dinero en la cantidad mínima de billetes y monedas necesarios. 
# Tengo todas las instrucciones necesarias, pero están todas mezcladas. ¿Podrías ayudarme a ordenarlas de manera correcta para que 
# funcione el programa como debería? A lo mejor se me perdieron algunas instrucciones, ¿podrías agregarlas?

cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
resto = cantidad_total
billetes_cien = resto // 100
billetes_cinco = resto // 5
billetes_mil = resto // 1000
billetes_cincuenta = resto // 50
billetes_doscientos = resto // 200
billetes_diez = resto // 10
billetes_docientos = resto // 200
billetes_uno = resto // 1
moneda_1peso= resto // 1
moneda_50cent= (resto //0.5)
print("Para la cantidad de  ",cantidad_total,"se necesitan:")
print(billetes_mil,"billetes de 1000")
print(billetes_doscientos, "billetes de  200")
print(billetes_cien,"billetes de 100")
print(billetes_cincuenta, "billetes de  50")
print(billetes_diez,"billetes de 10")
print(billetes_cinco, "billetes de  5")
print(billetes_uno,"billetes de 1")
print(moneda_1peso,"monedas de 1 peso")
print(moneda_50cent, "monedas de 50 centavos")



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita al usuario ingresar un número entero y luego muestre un mensaje indicando si el número es par o impar.

try:
    numero= abs(int(input("ingrese un numero: ")))
    if numero == 0:
        print("no se puede realizar la accion con valor 0, ingrese otro numero")
    elif numero % 2 == 0:
        print(f"{numero} es un numero par")
    else:
        print(f"{numero} es inpar")
except ValueError:
        print("valor invalido, debe ingresar solo numeros enteros")


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos.


num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa el segundo numero: "))

if num1-num2 == 0:
    print("Los numeros son iguales")
else:
    print("Los numeros son distintos")



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.

primera= input("Ingresa la primera cadena: ")
segunda= input("Ingresa la segunda cadena: ")


if primera == segunda:
    print("Las cadenas son iguales")
else:
    print("Las cadenas son diferentes")




#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------




# Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.


num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa el segundo numero: "))

if num1 > num2 :
    print(f"{num1} es mayor a {num2}")
elif num1 < num2:
    print(f'{num1} es menor a {num2}')
else:
    print("Los numeros son iguales")


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.


num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa el segundo numero: "))
num3= int(input("Ingresa el tercer numero: "))
if num1 > num2 :
    if num1 > num3:
        print(f"el numero mayor es {num1}")
elif num2 > num3:
    if num2 > num1:
        print(f'el numero mayor es {num2}')
else:
    print(f'el numero mayor es el {num3}')



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y el valor que esta en medio.
# Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 5 como el menor, el número 7 como el mayor y el número 3 como el que esta en medio.
# Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas?



num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa el segundo numero: "))
num3= int(input("Ingresa el tercer numero: "))

lista= [num1, num2, num3]

lista.sort(reverse= True)
for n in lista:
    if max(lista) == n:
        print(f"El mayor es {n}")
    elif min(lista) == n:
        print(f"el menor es {n}")
    else:
        print(f"el del medio es {n}")

## usando el codigo que nos pasaron para el ejercicio:


numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))

mayor = numero_uno
medio = numero_dos
menor = numero_tres

if numero_tres > mayor:
    mayor = numero_tres
    medio = numero_uno
    menor = numero_dos
if medio < menor:
    auxiliar = medio
    medio = menor
    menor = auxiliar
if numero_dos > mayor:
    mayor = numero_dos
    medio = numero_uno
    menor = numero_tres
if numero_dos > mayor:
    mayor = numero_dos
    medio = numero_uno
    menor = numero_tres

print("El mayor es: ", mayor)
print("El medio es: ", medio)
print("El menor es: ", menor)



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



# Para acceder a cierta atracción, es necesario cumplir con dos requisitos: tener al menos 10 años de edad y medir más de 1,60 metros.
# Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con
# ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje 
# que indique el motivo por el cual no puede subir. Por ejemplo, si no cumple con el requisito de la edad, el programa debe imprimir "Lo siento, eres demasiado 
# joven para acceder." Si no cumple con el requisito de la estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para acceder"





altura_minima=1.61
edad_minima= 10


altura_usuario= float(input("Ingrese su altura: "))
edad_usuario= int(input("Ingrese su edad: "))

if altura_usuario >= altura_minima and edad_usuario >= edad_minima:
    print("¡Puede acceder!")
elif altura_usuario < altura_minima:
    print("Lo siento, eres demasiado bajo para acceder")
if edad_usuario < edad_minima:
    print("Lo siento eres demasiado joven para acceder")



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


# Para acceder a cierta atracción, alcanza con que se cumpla solamente una de las siguientes condiciones: ser mayor de 6 años o medir más de 1,50 metros.
# Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple 
# con al menos una de las condiciones, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con ninguna de las condiciones, el programa debe 
# imprimir un mensaje que lo indique.


altura=1.50
edad= 6


altura_usuario= float(input("Ingrese su altura: "))
edad_usuario= int(input("Ingrese su edad: "))

if altura_usuario > altura or edad_usuario > edad:
    print("¡Puede acceder!")
else:
    print("Lo siento no cumples con la condicion para acceder")












