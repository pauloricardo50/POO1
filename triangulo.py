# dado 3 numeros inteiros verificar se os 3 numeros podem formar um triangulo
# eh triangulo se l1+l2 < l3, l1 + l3 < l2, l2 + l3 < l1
l1 = int(input("informe um lado do triangulo - 1\n"))
l2 = int(input("informe um lado do triangulo - 2\n"))
l3 = int(input("informe um lado do triangulo - 3\n"))
if ((l1+l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1 ):
    print("eh triangulo")
else:
    print("false")
