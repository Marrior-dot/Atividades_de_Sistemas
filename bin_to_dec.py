from math import pow
def binonot(varyable):
    o = "01"
    for char in varyable:
      if char not in o:
        return False
      else:
        return True

def counter(variable):
  start = 0
  while start <= len(variable)-1:
    yield start;
    start = start + 1;
    
r = input("Entre com um número binário: ")
while binonot(r) == False:
  print("Valor inválido")
  r = input("Entre com um número binário: ")
z = [int(x) for x in r][::-1]
soma = 0

for c in counter(z):
  soma = soma + z[c]*pow(2,c)

print("O número binário {} convertido para decimal tem o valor de {}".format(r,int(soma)))
