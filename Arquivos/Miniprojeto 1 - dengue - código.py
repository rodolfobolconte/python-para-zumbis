arquivo = open('Miniprojeto 1 - dengue.txt')

vnome = list() ; vidade = list() ; vsexo = list() ; vcidade = list() ; vdengue = list()

for linha in arquivo.readlines():
    nome, idade, sexo, cidade, dengue = linha[:-1].split(',')
    vidade.append(int(idade))
    vsexo.append(sexo)
    vcidade.append(cidade)
    vdengue.append(dengue)

#Média das idades
media_idades = sum(vidade) / len(vidade)

print("Média da idade das pessoas: %.2f" %media_idades)

#Mulheres com dengue
feminino_dengue = 0
for i in range(len(vsexo)):
    if vsexo[i] == 'f' and vdengue[i] == 's':
        feminino_dengue += 1

print("Quantidade de mulheres que já tiveram dengue:", feminino_dengue)

#Homens que moram em Campina Grande
masculino_cg = 0
for i in range(len(vsexo)):
    if vsexo[i] == 'm' and vcidade[i] == 'Campina Grande':
        masculino_cg += 1

print("Quantidade de homens que moram em Campina Grande:", masculino_cg)