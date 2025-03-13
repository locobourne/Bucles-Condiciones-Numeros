import random

random.seed(10)

num_negativos = suma_may_0_men_600 = may_igual_200 = imp_7 = contador_4 = numeros_4 = neg_par =  0

men_7 = None

sucesion = 30

while sucesion > 0:

    num = random.randint(-5000, 5000)
    print(num)

    if num > 0:
        num_negativos += 1

    if num >= 0 and num < 600:
        suma_may_0_men_600 += num

    if num >= 200 and (num % 10 == 3 or num % 10 == 2):
        may_igual_200 += 1

    if num % 2 != 0 and num % 7 != 0:
        if men_7 is None or  men_7 > num:
            men_7 = num

    if num < 0 and num % 4 == 0:
        contador_4 += 1
        numeros_4 += num

    if num < 0 and num % 2 == 0:
        neg_par += 1

    sucesion -= 1

porcentaje= (neg_par * 100) // 30
promedio= numeros_4 // contador_4

print("hay tantos numeros negativos:", num_negativos)
print("la suma de los mayores a 0 y men q 600:", suma_may_0_men_600)
print("mayores o iguales a 200:", may_igual_200)
print("el menor de los 7 asd= ", men_7)
print("el porcentaje de la cantidad de números negativos pares " , porcentaje)
print("el promedio de los numeros 4 es:", promedio
      )