from math import pow


def counter(variable):
    start = 0
    while start <= len(variable) - 1:
        yield start
        start = start + 1


def binonot(varyable):
    o = "01"
    for char in varyable:
        if char not in o:
            return False
        else:
            return True
n = 0
while n == 0 : 
  r = int(
    input(
        "Qual conversão você deseja realizar?\n1 - hexadecimal para binário\n2 - octal para binário\n3 - binário para hexadecimal\n4 - binário para octal\n"
    ))
  repeat = 0
  finalnumber = []
  soma = 0

  if r == 1:
      n = 1
      print("Você escolheu converter de hexadecimal para binário\n")
      while repeat == 0:
          num = str(input("Entre como número que deseja converter: \n"))
          for char in num:
            if char == "0":
                finalnumber.append("0000")
            elif char == "1":
                finalnumber.append("0001")
            elif char == "2":
                finalnumber.append("0010")
            elif char == "3":
                finalnumber.append("0011")
            elif char == "4":
                finalnumber.append("0100")
            elif char == "5":
                finalnumber.append("0101")
            elif char == "6":
                finalnumber.append("0110")
            elif char == "7":
                finalnumber.append("0111")
            elif char == "8":
                finalnumber.append("1000")
            elif char == "9":
                finalnumber.append("1001")
            elif char == "A":
                finalnumber.append("1010")
            elif char == "B":
                finalnumber.append("1011")
            elif char == "C":
                finalnumber.append("1100")
            elif char == "D":
                finalnumber.append("1101")
            elif char == "E":
                finalnumber.append("1110")
            elif char == "F":
                finalnumber.append("1111")
            else:
                print(
                    "O digito possui uma alternativa inválida\nDigite uma alternativa válida\n"
                )
                finalnumber = []
                break
          if len(finalnumber) == len(num):
                repeat = 1

      print("O {} número convertido para Binário é: {}".format(
        num, ''.join(finalnumber)))
      decarray = [int(x) for x in ''.join(finalnumber)][::-1]
      for c in counter(decarray):
        soma = soma + decarray[c] * pow(2, c)
      print("O número {} convertido para Decimal é: {}".format(num, int(soma)))

  elif r == 2:
    n = 1
    print("Você escolheu converter de octal para binário\n")
    while repeat == 0:
        num = str(input("Entre como número que deseja converter: \n"))
        for char in num:
            if char == "0":
                finalnumber.append("000")
            elif char == "1":
                finalnumber.append("001")
            elif char == "2":
                finalnumber.append("010")
            elif char == "3":
                finalnumber.append("011")
            elif char == "4":
                finalnumber.append("100")
            elif char == "5":
                finalnumber.append("101")
            elif char == "6":
                finalnumber.append("110")
            elif char == "7":
                finalnumber.append("111")
            else:
                print(
                    "O digito possui uma alternativa inválida\nDigite uma alternativa válida\n"
                )
                finalnumber = []
                break
        if len(finalnumber) == len(num):
            repeat = 1

    print("\nO {} número convertido para Binário é: {}".format(
        num, ''.join(finalnumber)))
    decarray = [int(x) for x in ''.join(finalnumber)][::-1]
    for c in counter(decarray):
        soma = soma + decarray[c] * pow(2, c)

    print("\nO número {} convertido para Decimal é: {}\n".format(
        num, int(soma)))

  elif r == 3:
    n = 1
    print("\nVocê escolheu converter de binário para hexadecimal\n")
    while repeat == 0:
        num = str(input("\nEntre com o número que deseja converter\n"))
        if len(num) % 4 == 0 and binonot(num) == True:
            hexarray = []
            numarray = []
            repeat = 1
            for x in num:
                hexarray.append(x)
                if len(hexarray) == 4:
                    numarray.append(hexarray)
                    hexarray = []                
        else:
            print("\nEntre com um numero que possua somente 0 e 1\n")
    for x in numarray:
      if ''.join(x) == "0000":
        finalnumber.append("0")
      elif ''.join(x) == "0001":
        finalnumber.append("1")
      elif ''.join(x) == "0010":
        finalnumber.append("2")
      elif ''.join(x) == "0011":
        finalnumber.append("3")
      elif ''.join(x) == "0100":
        finalnumber.append("4")
      elif ''.join(x) == "0101":
        finalnumber.append("5")
      elif ''.join(x) == "0110":
        finalnumber.append("6")
      elif ''.join(x) == "0111":
        finalnumber.append("7")
      elif ''.join(x) == "1000":
        finalnumber.append("8")
      elif ''.join(x) == "1001":
        finalnumber.append("9")
      elif ''.join(x) == "1010":
        finalnumber.append("A")
      elif ''.join(x) == "1011":
        finalnumber.append("B")
      elif ''.join(x) == "1100":
        finalnumber.append("C")
      elif ''.join(x) == "1101":
        finalnumber.append("D")
      elif ''.join(x) == "1110":
        finalnumber.append("E")
      elif ''.join(x) == "1111":
        finalnumber.append("F")                            
    print("\nO número {} em hexadecimal é: {}".format(num,''.join(finalnumber)))

    finalnumber = [int(d) for d in num][::-1]
    for x in counter(finalnumber):
      soma = soma + finalnumber[x] * pow(2,x)
    print("\nO número {} em decimal é: {}".format(num,int(soma)))  

  elif r == 4:
    n = 1
    print("\nVocê escolheu converter de binário para octal\n")
    while repeat == 0:
        num = str(input("\nEntre com o número que deseja converter\n"))
        if len(num) % 3 == 0 and binonot(num) == True:
            octarray = []
            intarray = []
            repeat = 1
            for x in num:
                octarray.append(x)
                if len(octarray) == 3:
                    intarray.append(octarray)
                    octarray = []
        else:
            print("\nEntre com um numero que possua somente 0 e 1\n")
    for x in intarray:
        if ''.join(x) == "000":
          finalnumber.append("0")
        elif ''.join(x) == "001":
          finalnumber.append("1")
        elif ''.join(x) == "010":
          finalnumber.append("2")
        elif ''.join(x) == "011":
          finalnumber.append("3")
        elif ''.join(x) == "100":
          finalnumber.append("4")
        elif ''.join(x) == "101":
          finalnumber.append("5")
        elif ''.join(x) == "110":
          finalnumber.append("6")
        elif ''.join(x) == "111":
          finalnumber.append("7") 
    print("\nO número {} em octal é: {}".format(num,''.join(finalnumber)))

    finalnumber = [int(d) for d in num][::-1]
    for x in counter(finalnumber):
      soma = soma + finalnumber[x] * pow(2,x)
    print("\nO número {} em decimal é: {}".format(num,int(soma)))

  else:
   print("Opção inválida\nEscolha uma opção de 1 a 4")