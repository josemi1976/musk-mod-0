n = int(input('Introduce la longitud de la secuencia: '))

suma = 0
secuencia = None
for i in range(0, n + 1):
    suma += pow(i, 2)
    
    if i == 0:
        secuencia = '{}^{}'.format(i, 2)
    else:
        secuencia += ' + {}^{} '.format(i, 2)
    
print('El resultado de la secuencia {} es {}'.format(secuencia, suma))
print("ejercicio github")
    

    
    



    
    
