num = int(input("ingrese numero"))

mul_5_no_3 = mul_3 = mul_de_nada = 0

while num != 0:
    num = int(input("ingrese numero"))

    if num % 3 == 0:
        mul_3 += 1

    if num % 5 == 0 and num % 3 != 0:
        mul_5_no_3 += 1

    if num % 5 != 0 and num % 3 != 0:
        mul_de_nada += 1

print("numeros multiplios de 3 son =" , mul_3)

print("numeros multiplios de 5 y no son de 3 son =" , mul_5_no_3)

print("numeros multiplios de nada son =" , mul_de_nada)



