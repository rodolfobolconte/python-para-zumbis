ips = open('ips.txt')
ips_validos = open('ips_validos.txt', 'w')

def valida_ips(ip):
	octetos = ip.split(".")
	valido = True

	if len(octetos) == 4:
		for octeto in octetos:
			if int(octeto) < 0 or int(octeto) > 255:
				valido = False
				break
	else:
		valido = False

	if valido:
		ips_validos.write('.'.join(octetos)+'\n')

for linha in ips.readlines():
	valida_ips(linha[:-1])