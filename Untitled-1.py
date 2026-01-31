lista=[]
diccionario={}
for num in range(1,101):
    if num %3==0 and num %5==0:
        print("fizzbuzz")
        lista.append("fizzbuzz")
        diccionario[num]=("fizzbuzz")
    elif num %3==0: 
        print("fizz")
        lista.append("fizz")
        diccionario[num]=("fizz")
    elif num %5 ==0:
        print("buzz")
        lista.append("buzz")
        diccionario[num]=("buzz")
else:
    print(num)
    lista.append(num)
    diccionario[num]
print("ejercicio github")