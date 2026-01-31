# ejercicio github

#6. Haz un programa que lea un número y que escriba el número de dígitos.
num1 = int(input("esceribe  un número: "))
num2 = num1
cont =0
while num1 > 0:
    num1 = num1 // 10
    cont +=1
  
print(f"{num2} tiene {cont} digitos")

#7. Haz un programa que diga si un natural n es capicua o no.
num1 = int(input("escribe  un número: "))
num2=num1
num_reves=""
while num1 > 0:
    num_reves += str(num1 % 10)
    num1 = num1//10

if num_reves==str(num2):
    print(f"{num2} es capicua")
else:
    print(f"{num2} no es capicua")

#8. Haz un programa que dada una secuencia de años acabada en 0 nos diga cuántos hay del siglo 20.
cont=0
for años in range (0,5):
    
    num = int(input("Introduce un año: "))
    num2 = num // 100
    
    if num2 + 1 == 20:
        cont += 1
   
print(f"hay {cont} años correspondiente siglo XX ")

#9. Haz un programa que reciba una secuencia de naturales de tamaño n
# y nos devuelva cuál es el primer natural que tiene un valor inferior al primer natural leído.
n = int(input("Introduce el tamaño de la secuencia: "))
num2 = int(input("Introduce el primer número de la secuencia: "))

for i in range(1, n):
    num1 = int(input(f"Introduce el número: "))
    if num1 < num2:
        print(f"El primer número menor que {num2} es {num1}")
        break
else: 
    print(f"no hay numero menor que {num2}")

#10. Haz un programa que cuente cuántos valores hay en una secuencia de enteros acabada en 0.
num=int(input("introduce un numero "))
cont=0
while num !=0:
    cont+=1
    num=int(input("escribe un numero :"))
    
print(f"(la secuencia tiene {cont} valores)")

#11. Haz un programa que devuelva el máximo de una secuencia de temperaturas acabada en 1000.
num=int(input("escribe numero "))
num2=0
while num !=1000:
    if num >num2:
        num2=num
    num=int(input("escribe numero "))
print (f" el numero mayor es {num2} ")

#12. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50. 
num=int(input("escribe un numero "))

while num !=0:
    if num>50: 
        print("hay un elemneto superior a 50")
        break
    elif num<50:
        num=int(input("escribe un numero "))
else:
    print("no hay un elemneto superior a 50")
        
    
    

#13. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50
# y que no hay más de tres que superen 40.0. 
num=int(input("escribe numero "))

cont=0

while num !=0:
    num=int(input("escribe numero "))
    if num >50:
        print("hay valores mayor que 50")
        break
    elif num ==0 :
        print("no hay valores mayor que 50")
        
    if num > 40:
        cont +=1
    if cont > 3 :
        print("hay tres valores mayores que 40")
        print("no hay valores mayores 50")
        break

else:
    print("no hay tres valores mmayores de 40 ")
    
#14. Haz un programa que dada una secuencia de valores acabada en 0 diga si hay más positivos o negativos.
num = int(input("Introduce un número: "))
num_pos=0
num_neg=0
while num !=0:
    if num>0:
        num_pos +=1
        num = int(input("Introduce un número: "))
    elif num<0:
        num_neg +=1
        num = int(input("Introduce un número: "))
if num_pos>num_neg:
    print("hay mas numero positivos que negaticos")
elif num_pos<num_neg:
     print("hay menos numero positivos que negativos")
    
else: 
    print("hay mismos numeros positivos que negativos")

#15. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuál es el número que hay antes de primer negativo encontrado.
num = int(input("Introduce un número: "))  
num_previo = None 

while num != 0:  
    if num > 0:  
        num_previo = num
        num = int(input("Introduce un número: ")) 
        
    elif num<0:
        if num_previo is not None:  
            print(f"El número anterior al primer negativo es: {num_previo}")
            break  
else:
    print("No hay número negativo en la secuencia.") 

#16. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuántos son múltiples del primero.
num=int(input("Introduce el primer número: "))
primer_num=None 
contador=0

while num !=0:
    if primer_num is None:
        primer_num=num
    elif num % primer_num==0:
        contador +=1
    num = int(input("Introduce  número: "))
print(f" hay {contador} numeros multiplos de {primer_num}")

#17. Haz un programa que lea varias descripciones de rectángulos y de círculos, y que para cada una escriba el área correspondiente.
#La entrada empieza con un número n, seguido de n descripciones. Si es de un rectángulo, se tiene la palabra “rectángulo” seguida de dos reales 
# estrictamente positivos que indican la longitud y la anchura. 
#Si es de un círculo, se tiene la palabra “círculo” seguida de un real estrictamente positivo que indica el radio.
import math
n = int(input("Introduce veces quieres hacer el ejercicio: "))

for i in range(0, n):
    figura= (input (" introduce el nombre de la figura: "))
    
    if figura == "rectangulo":
        longitud = float(input("Introduce la longitud del rectángulo: "))
        anchura = float(input("Introduce la anchura del rectángulo: "))
        area = longitud * anchura
        
    elif figura == "circulo":
        radio = float(input("Introduce el radio del círculo: "))
        area = math.pi * radio**2
        
    print(f"el {figura} tiene un area de {area}") 
    
#18. Haz un programa que lea un natural n, y que escriba el resultado de la suma siguiente: 1^2 + 2^2 + … + (n−1)^2 + n^2 y el aspecto de la secuencia. 
n=int(input("escribe un numero "))
suma=0
for reales in range(0,n+1):
    suma+=pow(reales,2)
    n = int(input("Introduce un número natural: "))
    if reales <= n:
        print(f"{reales**2}")
   
print(f"La suma es: {suma}")
print("ejercicio github")