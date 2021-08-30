from random import randint,randrange
#Mapeamento Direto
#Memória Cache
MC = [[],#Linha 00
      [],#Linha 01
      [],#Linha 10
      []]#Linha 11

#Memória Principal
#[Bloco,endereço,endereço]
MP = [["0000","00000","00001"],
      ["0001","00010","00011"],
      ["0010","00100","00101"],
      ["0011","00110","00111"],
      ["0100","01000","01001"],
      ["0101","01010","01011"],
      ["0110","01100","01101"],
      ["0111","01110","01111"],
      ["1000","10000","10001"],
      ["1001","10010","10011"],
      ["1010","10100","10101"],
      ["1011","10110","10111"],
      ["1100","11000","11001"],
      ["1101","11010","11011"],
      ["1110","11100","11101"],
      ["1111","11110","11111"]]

for bloco in MC:
  L00 = randrange(0,12,4)#00
  L01 = randrange(1,13,4)#01
  L10 = randrange(2,14,4)#10
  L11 = randrange(3,15,4)#11
  if bloco == MC[0]:
      MC[0].append(MP[L00][1])
      MC[0].append(MP[L00][2])
      #print("Linha00 {}".format(MC[0]))
  elif bloco == MC[1]:
      MC[1].append(MP[L01][1])
      MC[1].append(MP[L01][2])
      #print("Linha01 {}".format(MC[1]))
  elif bloco == MC[2]:       
      MC[2].append(MP[L10][1])
      MC[2].append(MP[L10][2])
      #print("Linha10 {}".format(MC[2]))
  elif bloco == MC[3]:
      MC[3].append(MP[L11][1])
      MC[3].append(MP[L11][2])
      #print("Linha11 {}".format(MC[3]))

print(MC[0])
print(MC[1])
print(MC[2])
print(MC[3])

print("\nLendo endereço:\ntag(2 bits)/linha(2 bits)/byte(1 bit)\n")

tag = input("Tag:")
while len(tag) != 2:
    print("Digite somente 2 bits para a tag:")
    tag = input("Tag:")
line = input("\nLinha:")
while len(line) != 2:
    print("Digite somente 2 bits para a linha:")
    line = input("Linha:")
byte = input("\nByte:")
while len(byte) != 1:
    print("Digite somente 1 bit para a célula:")
    byte = input("Byte:")    

cel = tag+line+byte

print("\nEndereço:{}\n".format(cel)) 

for L in MC:
  if cel in L:
    #print("Célula na linha {}".format(line))
    exit("Célula na linha {}".format(line))

print("Miss \nProcurando célula na memória principal:")
for bloco in MP:
  if cel in bloco:
    print("A célula está no bloco {}".format(bloco[0]))  
