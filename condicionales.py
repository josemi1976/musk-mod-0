#1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. 
# Escribe en una línea indicando si a < b, a > b o a = b. Ejemplo: a = Anna, b = Javier, Anna < Javier.
palabra=input("escribe palabra ")
palabra2=input("escribe palabra ")
if palabra<palabra2:
    print(f"{palabra}<{palabra2}")
elif palabra>palabra2:
    print(f"{palabra}>{palabra2}")
else:
    print("intentalo de nuevo")

    
#2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula,
#  si es una minúscula, si es una vocal, y si es una consonante.

letra=input("escribe una letra ")
letra=input("escribe una letra ")
if letra == "a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("vocal")
elif letra.lower() in ("a,e,i,o,u"):
        print("vocal")
else:
    print("consonante")
if letra.isupper():
    print("mayuscula")
else:
    print("minuscula")
   
#3. Haz un programa que lea un entero que representa una temperatura en grados Celsius, y que diga si hace calor,
#  si hace frío, o si se está bien. Suponed que hace calor si la temperatura es más alta que 30 grados,
#  que hace frío si es más baja que 10 grados, y que se está bien en otro caso.

temperatura=int(input("grados "))
if temperatura < 10:
    print("hostia que frio")
elif temperatura > 30:
    print("hostia que calo")
else:
    print("hay que agustito toy")

#4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la intersección o indique que esta es vacía.

x1 = int(input("Introduce un intervalo:"))
x2 = int(input("Introduce un intervalo:"))

y1 = int(input("Introduce un intervalo:"))
y2 = int(input("Introduce un intervalo:"))

valor1= x1
if x1<y1:
    valor1=y1
    
valor2=x2
if x2 > y2:
    valor2 = y2

if valor1 <= valor2:
    print(f"{valor1,valor2}")
else:
    print("vacio")

#5. Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días. 
# Después de la reforma gregoriana, los años bisiestos son los múltiplos de cuatro que no acaban en dos ceros,
#  y también los acabados en dos ceros tales que el número que queda después de sacar los dos ceros finales es divisible por cuatro.
#  Así, 1800 y 1900, a pesar de ser múltiples de cuatro, no fueran bisiestos; en cambio, 2000 lo fue.
x =int(input("introduce un año: "))
if (x % 4 == 0 and x % 400 == 0) or x % 100 !=0:
    print("año bisiesto")
else:
    print("no bisiesto")

#6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.
s = int(input("Introduce los segundos: "))
m = int(input("Introduce los minutos: "))            
h = int(input("Introduce las horas: "))


if s + 1 > 59:
    s = 0
    m += 1
    if m > 59:
        m = 0
        h += 1
else:
    s += 1
        
print(f"{s,m,h}")

