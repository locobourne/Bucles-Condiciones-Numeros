import random

random.seed(20220512)

mul_3 = mul_5_no_3 = mul_de_nada = mul_nada = pares_mul_11 = contador_pares_11 = 0

mayor = None

sucesion = 25000


while sucesion > 0:
    num = random.randint(1, 45000)

    print(num)

    if num % 3 == 0:
        mul_3 += 1

    if num % 5 == 0 and num % 3 != 0:
        mul_5_no_3 += 1

    if num % 5 != 0 and num % 3 != 0:
        mul_de_nada += 1

    aux = str(num)
    if aux[0] == "1":
        if mayor is None or mayor < num:
            mayor = num

    if num % 2 == 0 and num % 11 == 0:
        pares_mul_11 += num
        contador_pares_11 += 1


    sucesion -= 1


promedio_pares= pares_mul_11 // contador_pares_11


porcentaje_numeros_3 = (mul_3 * 100) // 25000
porcentaje_numeros_5_no_3 = (mul_5_no_3 * 100) // 25000
porcentaje_numeros_nada= (mul_de_nada * 100) // 25000

print("numeros multiplios de 3 son =" , mul_3)

print("numeros multiplios de 5 y no son de 3 son =" , mul_5_no_3)

print("numeros multiplios de nada son =" , mul_de_nada)

print("el numero mayor que empieza en 1 es =" , mayor)

print("el promedio entero truncado de 11 es:", promedio_pares)


print("porcentaje de los 3ces=", porcentaje_numeros_3)
print("porcentaje de los 5 no 3 asd=",porcentaje_numeros_5_no_3 )
print("porcentaje de los nada=", porcentaje_numeros_nada)

