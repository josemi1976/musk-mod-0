#1.	Par o Impar y Positivo o Negativo: Pide al usuario que ingrese un número. 
# Imprime si el número es par e positivo, par e negativo, impar y positivo, o impar y negativo
num=int(input(" escribe un numero "))
if num>0 and num%2==0:
   print("par y positivo ")
elif num<0 and num%2==0:
   print("par y negativo ")
elif num>0 and num%2!=0:
   print("impar y positivo")
elif num<0 and num%2!=0:
   print("impar y negativo")

#2.	Rango de Números: Solicita al usuario que ingrese un número. 
# Verifica si el número está en el rango de 10 a 50 (inclusive) o si es menor que 0.
num=int(input(" escribe un numero "))
if num<0:
   print("correcto")
elif num>10 and num<50:
   print("correcto")
else:
   print("incorrecto")

#3.	Nombre de Usuario y Contraseña: 
# Crea un programa que solicite al usuario ingresar un nombre de usuario y una contraseña. Imprime un mensaje si ambos son correctos.
usuario="noah"
contraseña="viva er betis"
user=input("escribe usuario ")
password=input("escribe contraseña ")
if usuario==user and contraseña==password:
   print("correcto")
else:
   print("incorrecto")

#Comprobación de Día y Mes: 
# Solicita al usuario que ingrese un día del mes y un número de mes. Imprime si la combinación es válida o no
#  (considerando febrero con máximo 29 días).
mes="marzo"
dia=10
di_mes=input("escribe un mes ")
di_dia=input("escribe un dia ")
if mes==di_mes and dia==di_dia:
      print("correcto")
else:
   print("incorrecto")

#5.	Año de Nacimiento y Edad: Pide al usuario que ingrese su año de nacimiento y verifica si tiene al menos 18 años. 
# Imprime un mensaje indicando si es mayor de edad.
año="2006"
año_nac=input("ingresa tu año nacimiento ")

if año<año_nac:
   print("mayor de edad")
else:
   print("eres menor edad")

6.	#Año Bisiesto o Par: Solicita al usuario que ingrese un año. Imprime si el año es bisiesto o si su último dígito es par.

7.	#Comparación de Tres Números con or: Solicita al usuario que ingrese tres números e imprime si al menos uno de ellos es positivo.
num1=int(input("escribe un numero "))
num2=int(input("escribe un numero "))
num3=int(input("escribe un numero "))
if num1>0 or num2>0 or num3>0:
   print(" al menos uno de ellos es positivo")
if num1>0:
   print(num1)
if num2>0:
   print(num2)
if num3>0:
   print(num3)

#8.	Ingreso de Edades: 
# Solicita al usuario que ingrese dos edades y verifica si al menos una de ellas es menor de 12 o mayor de 65 años.
edad1=int(input("escribe una edad "))
edad2=int(input("escribe una edad "))
if edad1<12 or edad2<12:
   print("uno de ellos es menor 12") 
   if edad1>65 or edad2>65:
      print("uno elllos es mayor que 65")

#9.	Menú de Opciones: Crea un pequeño menú con opciones numeradas. 
# Pide al usuario que elija una opción (1, 2, 3) y realiza acciones diferentes según la opción elegida.
num1=int(input("elige numero 1,2,3 "))

if num1==1:
   print("elegiste 1")
elif num1==2:
   print("elegiste 2")
elif num1==3:
   print("elegiste 3")
print("ejercicio github")

