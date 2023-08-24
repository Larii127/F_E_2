alturaF = []
alturaM = []
generoF = []
generoM = []


i = 0
while i < 5:
    varGenero = input("informe F OU M ")

    if varGenero == "F":
        varAltura = float(input("inforome sua altura: "))
        generoF.append(varGenero)
        alturaF.append(varAltura)
    elif varGenero == "M":
        varAltura = float(input("inforome sua altura: "))
        alturaM.append(varAltura)
    else:
        print("Precisa ser um genero valido")


    i += 1



maiorAltura = 0

for i in alturaF:
    if i > maiorAltura:
        maiorAltura = i


for i in alturaM:
    if i > maiorAltura:
        maiorAltura = i

menorAltura = 0

for i in alturaF:
    if menorAltura == 0:
        menorAltura = i
    elif i > maiorAltura:
        maiorAltura = i

for i in alturaM:
    if menorAltura == 0:
        menorAltura = i
    elif i > maiorAltura:
        maiorAltura = i

media = sum(alturaM) / len(alturaM)

print("Maior altura: ", maiorAltura)
print("Menor altura: ", menorAltura)
print("Media da altura masculina: ", media)
print("Quantas mulheres: ", len(alturaF))
