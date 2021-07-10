from itertools import product, repeat
from math import log2

n = 0
while n == 0:
    ask = int(input("Quantos niveis de quantização você deseja? "))

    amount = log2(ask)
    if amount.is_integer() == True:
        print("Número de bits: ", int(amount))
        print("\nCombinações possiveis:")
        for i in product(range(2), repeat=int(amount)):
            print(i)
            n = 1

    else:
        print("Escolha um número de base 2")
