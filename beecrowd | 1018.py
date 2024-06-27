cedula = [100,50,20,10,5,2,1]
dinheiro = int(input())

print(dinheiro)


notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

for i in range(1000000):

  if dinheiro >= cedula[0]:
    dinheiro -= cedula[0]
    notas100 += 1



  elif dinheiro >= cedula[1]:
    dinheiro -= cedula[1]
    notas50 += 1



  elif dinheiro >= cedula[2]:
    dinheiro -= cedula[2]
    notas20 += 1



  elif dinheiro >= cedula[3]:
    dinheiro -= cedula[3]
    notas10 += 1



  elif dinheiro >= cedula[4]:
    dinheiro -= cedula[4]
    notas5 += 1



  elif dinheiro >= cedula[5]:
    dinheiro -= cedula[5]
    notas2 += 1



  elif dinheiro >= cedula[6]:
    dinheiro -= cedula[6]
    notas1 += 1

print("{} nota(s) de R$ 100,00".format(notas100))
print("{} nota(s) de R$ 50,00".format(notas50))
print("{} nota(s) de R$ 20,00".format(notas20))
print("{} nota(s) de R$ 10,00".format(notas10))
print("{} nota(s) de R$ 5,00".format(notas5))
print("{} nota(s) de R$ 2,00".format(notas2))
print("{} nota(s) de R$ 1,00".format(notas1))
