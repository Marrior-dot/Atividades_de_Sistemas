def CI(rem):
  if rem == 0:
    return rem
  elif rem == 1:
    return rem
  elif rem == 2:
    return rem
  elif rem == "B4":
    return rem
  elif rem == "B5":
    return rem    

def RI(rdm):
  if rdm == "AB5":
    print("Imprimir valor em B5: {}".format(b5))
  elif rdm == "1B5":
    print("Carregando valor em B5")  
  elif rdm == "3B4":
    return CI("B4")

ci = CI(0)
b5 = int(input("Escolha o número: "))
b4 = b5
N = int(input("Determine o número para o produto: "))
RDM = ""

while b5<b4*N:
  if ci == 0:
    RDM = "AB5"
    print(RI(RDM))
    ci = CI(1)
  elif ci == 1:
    RDM = "1B5"
    print(RI(RDM))
    ci = CI(2)
  elif ci == 2:
    RDM = "3B4"
    print("incrementando o valor em B5 em {}".format(b4))
    ci = RI("3B4")
  elif ci == "B4":
    b5 += b4
    print("Valor de B5: {}".format(b5)) 
    ci = CI(0)
  print("Recomeçando processo")
