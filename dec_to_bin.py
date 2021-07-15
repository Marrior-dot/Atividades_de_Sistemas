
narr = input("Entre com um número inteiro: ")
while narr.isdigit() == False:
  print("Valor inválido")
  narr = input("Entre com um número inteiro: ")
num = []
half = int(narr)

while half/2 >=1:
  num.append(int(half%2))
  half = half/2

num.append(1)
numstr = ''.join(str(x) for x in num[::-1])

print("O número decimal {} convertido em binário é: {}".format(narr,numstr)) 
