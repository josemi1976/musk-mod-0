#	Número Positivo o Negativo:
#  Escribe un programa que solicite al usuario ingresar un número e imprima si el número es positivo, negativo o cero.
numero=int(input("escribe un numero "))
if numero<0:
    print("negativo")
elif numero>0:
    print("positivo")
else:
    print("cero")

#2.	Mayor de Dos Números: Solicita al usuario que ingrese dos números y determina cuál es el mayor.

numero=int(input("escribe un numero "))
numero2=int(input("escribe un numero "))
if numero<numero2:
    print(f"el numero mayor es {numero2}")
elif numero>numero2:
    print(f"el numero mayor es {numero}")
else:
    print("igual")

#3.	Día de la Semana: 
# Pide al usuario que ingrese un número del 1 al 7 que represente un día de la semana, e imprime el nombre del día.
numero=int(input("escribe un numero "))
if numero==1:
    print("lunes")
elif numero==2:
    print("martes")
elif numero==3:
    print("miercoles")
elif numero==4:
    print("juevess")
elif numero==5:
    print("viernes")
elif numero==6:
    print("sabado")
elif numero==7:
    print("domingo")
else:
    print("no es un dia")

4.#Calculadora Simple:
#Crea una calculadora simple que solicite al usuario ingresar dos números y una operación (+, -, *, /). 
#Realiza la operación e imprime el resultado.
numero=int(input("escribe un numero "))
numero2=int(input("escribe un numero "))
signo_mat= input("escribe signo matematico (+, -, *, /)")

if signo_mat=="+":
    print(numero+numero2)
elif signo_mat=="-":
    print(numero-numero2)
elif signo_mat=="*":
    print(numero*numero2)
elif signo_mat=="/":
    print(numero/numero2)
else:
    print("no hay operacion")

#5.	Clasificación de Edad: Solicita al usuario que ingrese su edad y clasifícala en "niño" (0-12 años),·
# # "adolescente" (13-17 años), "adulto joven" (18-25 años), "adulto" (26-64 años), o "adulto mayor" (65 años en adelante).
edad=int(input("escribe tu edad "))
if edad<12:
    print("niño")
elif edad<17:
    print("joven")
elif edad<25:
    print("adulto joven")
elif edad<64:
    print("adulto")
elif edad>65:
    print("mayor")

#6.	Categoría de Peso: Crea un programa que solicite al usuario ingresar su peso y altura,
#  y determine su categoría de peso según el índice de masa corporal (IMC).
#  Puedes usar fórmulas aproximadas para las categorías de peso.

peso=int(input("cual es tu peso "))
estatura=int(input("cual es tu estaura "))
if (peso/estatura)<0.30:
    print("estas delgado")
elif (peso/estatura)<0.70:
    print("estas en forma")
elif(peso/estatura)<=1:
    print("estas fofo")

# 7.	Comparación de Tres Números: Pide al usuario que ingrese tres números e imprime el mayor de ellos.
num1=int(input("escribe un numero "))
num2=int(input("escribe un numero "))
num3=int(input("escribe un numero "))
if (num1>num2>num3):
    print(num1)
elif (num2>num1>num3):
    print(num2)
elif (num3>num1>num2):
    print(num3)

8.	#Orden de Números: Solicita al usuario que ingrese tres números e imprime los números en orden ascendente.

num1=int(input("escribe un numero "))
num2=int(input("escribe un numero "))
num3=int(input("escribe un numero "))
if (num1<num2<num3):
    print(num1,num2,num3)
elif (num1<num3<num2):
    print(num1,num3,num2)
elif (num2<num1<num3):
    print(num2,num1,num3)
elif (num3<num2<num1):
    print(num3,num2,num1)
elif (num3<num1<num2):
    print(num3,num1,num2)
print("ejercicio github")