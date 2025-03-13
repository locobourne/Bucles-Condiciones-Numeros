import random
random.seed(49)
numeros5 = 0
numeros7 = 0
numeros9 = 0
sumatoria= 0

cont= 20000
while cont > 0:
    numerorandom = random.randint(1, 45000)

    if numerorandom % 5 == 0:
        numeros5 +=1

    if numerorandom % 7 == 0:
        numeros7 +=1

    if numerorandom % 9 == 0:
        numeros9 +=1

    if numerorandom %10 >= 5 or <= 8
        nummayor= numerorandom

    sumatoria += numerorandom
    cont -= 1


print(sumatoria)
print( "suma 5:" , numeros5)
print( "suma 7:" , numeros7)
print( "suma 9:" , numeros9)









