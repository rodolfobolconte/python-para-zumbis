arquivo = open('Arquivos 1.txt')
notas = []
for linha in arquivo:
	nome, pontos = linha. split()
	notas.append(float(pontos))

arquivo.close()

notas.sort()
notas.reverse()
print(notas[0])
print(notas[1])
print(notas[2])