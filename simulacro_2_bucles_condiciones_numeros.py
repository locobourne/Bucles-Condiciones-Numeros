import random

random.seed(49)

mult_5 = mult_7 = mult_9 = pares_menores_15k = 0

numero_entre_5_8= None

sucesion = 20000

while sucesion > 0:
    rand_num = random.randint(1, 45000)
    print(rand_num)

    if rand_num % 5 == 0:
        mult_5 += 1

    if rand_num % 7 == 0:
        mult_7 += 1

    if rand_num % 9 == 0:
        mult_9 += 1


    if   rand_num % 10 >= 5 and rand_num % 10 <= 8:
        if numero_entre_5_8 is None or rand_num > numero_entre_5_8:
            numero_entre_5_8 = rand_num

    if rand_num < 15000:
        if rand_num % 2 == 0:
           pares_menores_15k += 1

    sucesion -= 1


porcentaje= (pares_menores_15k * 100) // 20000


print("el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8:", numero_entre_5_8)
print("multiplos 5" , mult_5)
print("multiplos 7" , mult_7)
print("multiplos 9" , mult_9)
print("pares menores a 15000 son =" , pares_menores_15k)
print("porcentaje =", porcentaje )