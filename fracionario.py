from math import pow, modf


def counter(variable):
    start = 0
    while start < len(variable) - 1:
        start = start + 1
        yield start


def binonot(var):
    o = "01."
    for char in var:
        if char not in o:
            return False
        else:
            return True


n = 0
while n == 0:
  p = int(
        input(
            "Qual conversão você deseja fazer?\n1- Binário para Real\n2- Real para binário\n"
        ))
  intnumber = []
  floatnumber = []
  soma = 0
  soma1 = 0

  if p == 1:
    n = 1
    r = str(input("Insira o valor desejado: "))
    while binonot(r) == False:
        print("Insira um valor que contenha apenas os números 0 ou 1")
        r = str(input("Insira o valor desejado: "))
    if r.isdigit() == True:
        for x in r:
            intnumber.append(x)
        floatnumber = [float(z) for z in intnumber][::-1]
        for c in counter(floatnumber):
            soma = soma + floatnumber[c] * pow(2, c)
    else:
        intnumber.append(float(r[0]))
        for x in counter(r):
            if x > r.index("."):
                floatnumber.append(float(r[x]))
            elif x < r.index("."):
                intnumber.append(float(r[x]))
        for c in counter(intnumber):
            soma = soma + intnumber[::-1][c] * pow(2, c)
        for z in counter(floatnumber):
            soma1 = soma1 + floatnumber[z] * pow(2, -(z + 1))
    print("O valor binário {} convertido em decimal é:{} ".format(
        r, (soma + soma1)))

  elif p == 2:
    n = 1
    r = str(input("Insira o valor desejado: "))
    while r.isalpha() == True:
        print("Insira um valor qu possua apenas numeros")
        r = str(input("Insira o valor desejado: "))
    if r.isdigit() == True:
        intr = int(r)
        while intr / 2 >= 1:
            intnumber.append(int(intr % 2))
            intr = intr / 2
        intnumber.append(1)
        strnumber = [str(x) for x in intnumber][::-1]
        print("O número decimal {} convertido para binário é: {}".format(
            r, ''.join(strnumber)))
    else:
        print(modf(float(r))[1])
        integerR = modf(float(r))[1]
        floatR = modf(float(r))[0]
        while integerR / 2 >= 1:
            intnumber.append(int(integerR % 2))
            integerR = integerR / 2
        intnumber.append(1)
        intnumber.insert(0, ".")
        print(intnumber[::-1])
        while floatR < 1:
            if floatR * 2 < 1:
                intnumber.insert(0, "0")
            elif floatR * 2 > 1:
                intnumber.insert(0, "1")
            floatR = floatR * 2
        intnumber.insert(0, "1")
        print(intnumber[::-1])
        strnumber = [str(x) for x in intnumber][::-1]
        print("O número {} em binário é:{} ".format(r, "".join(strnumber)))
  else:
    print("Escolha some 1 ou 2")      
