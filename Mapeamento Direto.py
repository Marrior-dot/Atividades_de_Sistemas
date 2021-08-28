#Mapeamento Direto
#def counter(arraycount):
 # start = 0
  #for x in arraycount:
   # start = start + 1
  #if start == len(arraycount):
   # break


MC = [[],
      [],
      [],
      []]

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

for bloco in MP:
  for cel in bloco:
      if cel == "0000":
        MC[0].append(MP[0][1])
        MC[0].append(MP[0][2])

      elif cel == "0001":
        MC[1].append(MP[1][1])
        MC[1].append(MP[1][2])

      elif cel == "0010":
        MC[2].append(MP[2][1])
        MC[2].append(MP[2][2])

      elif cel == "0011":
        MC[3].append(MP[3][1])
        MC[3].append(MP[3][2])

      elif cel == "0100":
        MC[0].append(MP[4][1])
        MC[0].append(MP[4][2])

      elif cel == "0101":
        MC[1].append(MP[5][1])
        MC[1].append(MP[5][2])

      elif cel == "0110":
        MC[2].append(MP[6][1])
        MC[2].append(MP[6][2])

      elif cel == "0111":
        MC[3].append(MP[7][1])
        MC[3].append(MP[7][2])

      elif cel == "1000":
        MC[0].append(MP[8][1])
        MC[0].append(MP[8][2])

      elif cel == "1001":
        MC[1].append(MP[9][1])
        MC[1].append(MP[9][2])

      elif cel == "1010":
        MC[2].append(MP[10][1])
        MC[2].append(MP[10][2])

      elif cel == "1011":
        MC[3].append(MP[11][1])
        MC[3].append(MP[11][2])
      elif cel == "1100":
        MC[0].append(MP[12][1])
        MC[0].append(MP[12][2])

      elif cel == "1101":
        MC[1].append(MP[13][1])
        MC[1].append(MP[13][2])

      elif cel == "1110":
        MC[2].append(MP[14][1])
        MC[2].append(MP[14][2])

      elif cel == "1111":
        MC[3].append(MP[15][1])
        MC[3].append(MP[15][2])                      

  if len(MC[0])==2 and len(MC[1])==2 and len(MC[2])==2 and len(MC[3])==2:

    print("\n{}".format(MC[0]))
    print(MC[1])
    print(MC[2])
    print("{}\n".format(MC[3]))

    MC[0] = []
    MC[1] = []
    MC[2] = []
    MC[3] = []
