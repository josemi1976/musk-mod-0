#cambios para github

#1. Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b. 
# Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.
num =int(input("Introduce un número:"))
num2 =int(input("Introduce un número:"))

if num < num2 :
    for num_enteros in range(num, num2 + 1):
        print(num_enteros)
else:
    for num_enteros in range(num, num2-1, -1):
        print(num_enteros)
        
        
#2. Haz un programa que lea una secuencia de 10 números y que escriba la media.
num1=0

for secuencia in range (0,10):
    num2=int(input("introduce un numero "))
    num1 += num2
print(f"media es: {num1/10}")

#3Haz un programa que dada una lista de naturales de tamaño n, 
#indique la posición del primer número par.
n = int(input("Introduce el tamaño de la lista: "))
posicion = 0


for numero in range(1, n + 1):
    num = int(input("Introduce el número : "))
    if num % 2 == 0 and posicion == 0:
        posicion = numero
        primer_par = num


if posicion != 0:
    print(f"El primer número par es {primer_par} y su posición es {posicion}")
else:
    print("No se encontró ningún número par.")
    
    
    

#4. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.
num=int(input("escribe un numero: "))
for num2 in range(1,11):
    print(f"{num}x{num2}= {num*num2}")
    
print("ejercicio github")
