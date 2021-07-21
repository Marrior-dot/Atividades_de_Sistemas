from math import pow,modf

def counter(variable):
  start = 0
  while start <= len(variable)-1:
    yield start;
    start = start + 1;

print("Exercicio 1")
r1 = "01110"
for x in counter(r1):
  if x == 0:
    print("1.)O bit menos significativo é o bit o 0 0\nCovertido para decimal: {}".format(int(r1[x])*pow(2,x)))
  elif x == 3:
    print("\n1.)O bit mais significativo é o 3\nConvertido para decimal: {}".format(int(r1[x])*pow(2,x))) 
r2 = "1010"
r3 = "1100110001"
somar2 = 0
somar3 = 0
for o in counter(r2):
    somar2 = somar2 + int(r2[::-1][o])*pow(2,o)
print("\n2.)O número {} em decimal é :{}".format(r2,somar2))

for i in counter(r3):
    somar3 = somar3 + int(r3[::-1][i])*pow(2,i)
print("\n3.)O número {} em decimal é :{}".format(r3,somar3))

print("\nExercicio 2\nConverta esse números binário para decimais")
r = [[1,1,0,1,0,1,0,1][::-1], [1,0,1,0,0,0,0,0][::-1],[1,1,0,0,0,1,1][::-1],[1,0,1,0,0,1,1,1][::-1],[1,1,0,1,1,1,1,1][::-1],[1,0,1,1,1,1,0,1][::-1],[0,1,1,1,0,0,0,0][::-1],[1,0,0,0,1,1,1,0][::-1],[0,1,1,0,1,1,1,0][::-1],[1,1,1,1,0,0,0,0][::-1],[1,1,0,0,1,0,0,0][::-1],[1,0,0,0,0,0,1,1][::-1],[0,0,0,0,0,0,0,1][::-1],[1,0,0,0,0,0,1,0][::-1],[1,1,1,0,1,1,1,0][::-1],[1,0,1,0,1,0,1,0][::-1],[0,1,1,0,0,0,1,1][::-1],[0,0,0,1,1,1,0,0][::-1],[0,0,1,1,0,0,0,1][::-1],[1,1,1,0,0,0,1,1][::-1],[1,1,0,1,1,0,0,0][::-1],[1,0,0,1,0,0,0,0][::-1],[0,1,0,1,0,1,0,0][::-1],[1,1,1,0,1,0,1,1][::-1]]
soma = 0
n = 0
for x in r:
  soma = 0
  for c in counter(x):
    soma = soma + x[c]*pow(2,c)
  n = n + 1  
  print("{}){} = {}".format(n,''.join([str(e) for e in x][::-1]),soma))

print("\nExercicio 3")
arrays = [21,552,715]
num = []
n = 0
for unit in arrays:
  while unit/2 >= 1:
    num.append(int(unit%2))
    unit = unit/2
  num.append(1)
  print("{}.{} = {}".format(n+1,arrays[n] ,''.join([str(c) for c in num][::-1])))
  n = n + 1
  num = []

print("\nExercicio 4")
exercise = "111.001"
intnumber = []
floatnumber = []
soma0 = 0
soma1 = 0
for x in counter(exercise):
  if x > exercise.index("."):
    floatnumber.append(float(exercise[x]))
  elif x < exercise.index("."):
    intnumber.append(float(exercise[x]))   
for c in counter(intnumber):
  soma0 = soma0 + intnumber[::-1][c] * pow(2, c)
for z in counter(floatnumber):
  soma1 = soma1 + floatnumber[z] * pow(2, -(z + 1))
print("O valor binário {} convertido em decimal é:{} ".format(exercise, (soma0 + soma1)))

print("\nExercicio 5")
exercise5 = ["4.8", "3.125"]
exnumber = []
for ex in exercise5:
        integerR = modf(float(ex))[1]
        floatR = modf(float(ex))[0]
        while integerR / 2 >= 1:
            exnumber.append(int(integerR % 2))
            integerR = integerR / 2
        exnumber.append(1)
        exnumber.insert(0, ".")
        while floatR < 1:
            if floatR * 2 < 1:
                exnumber.insert(0, "0")
            elif floatR * 2 > 1:
                exnumber.insert(0, "1")
            floatR = floatR * 2
        exnumber.insert(0, "1")
        strnumber = [str(x) for x in exnumber][::-1]
        exnumber = []
        print("O número {} em binário é:{} ".format(ex, "".join(strnumber))) 

print("\nExercicio 6")
r = "3A7"
result = []
newresult = []
final_result = []
for x in r:
  if x == "3":
    result.append("0")
    result.append("0")
    result.append("1")
    result.append("1")
  elif x == "A":
    result.append("1")
    result.append("0")
    result.append("1")
    result.append("0") 
  elif x == "7":
    result.append("0")
    result.append("1")
    result.append("1")
    result.append("1")
for x in result:
  newresult.append(x)
  if len(newresult) == 3:
    if newresult == ["1","1","1"]:
      final_result.append("7")
    elif newresult == ["1","0","0"]:
      final_result.append("4")
    elif newresult == ["1","1","0"]:
      final_result.append("6")
    elif newresult == ["0","0","1"]:
      final_result.append("1")      
    newresult = []
print("1) O número {} em octal é: {}".format(r,''.join(final_result)))

z = ["1100011","001011000000"]
resarray = []
final_array = []
lastarray = []
for c in z:
  for v in c:
    resarray.append(v)
  while (len(resarray)%4) != 0:
    resarray.insert(0,"0")
  final_array.append(resarray)  
  resarray = []

for b in final_array:
    for char in b:
      lastarray.append(char)
      if lastarray == [ "0","1","1","0"]:
        resarray.append("6")
        lastarray = []
      elif lastarray == [ "0","0","1","1"]:
        resarray.append("3")
        lastarray = []
      elif lastarray == [ "0","0","0","0"]:
        resarray.append("0")
        lastarray = []
      elif lastarray == ["0","0","1","0"]:
        resarray.append("2")
        lastarray = []
      elif lastarray == ["1","1","0","0"]:
        resarray.append("C")
        lastarray = []
    if resarray == ["6","3"]:
      print("2.a)O número {} em hexadecimal é:{}".format(z[0],''.join(resarray)))
      resarray = []          
    elif resarray == ["2","C","0"]:
      print("2.b)O número {} em hexadecimal é:{}".format(z[1],''.join(resarray)))
      resarray = []    
 
       



